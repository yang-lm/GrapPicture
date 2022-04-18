'''
Description: 
Author: xiaoming
Date: 2022-01-25 08:59:31
'''

import getpass
import requests
import json
url = r'http://***.com/public/comm/publics/login'
def glogin():
    passd = True
    while passd:
        print("请输入拥有Ikanban权限的账号密码")
        user = input('ItCode: ')
        password = getpass.getpass('password: ')

        response = requests.post(url=url, data={"account":user,"password":password,"captcha":"eaje"})
        # response.enconding = "utf-8"
        res = response.content.decode("utf-8")
        
        # print(response.status_code)
        res = json.loads(res)
        if res.get("code",1) != 0:
            print(response.text)
            print("账号与密码无法识别,请重新输入...")
        if res.get("code",1) == 0:
            passd = False
    return user,password
