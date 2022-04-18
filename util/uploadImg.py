# -*- coding: utf-8 -*- 
'''
Description: 
Author: xiaoming
Date: 2022-01-21 13:54:41
'''
import requests
url = r'http://***/public//efficiency/Kanban/uploadImg'
def sendImg(img_path, img_name, img_type='png/jpg'):
    """
    :param img_path:图片的路径
    :param img_name:图片的名称
    :param img_type:图片的类型,这里写的是image/jpeg，也可以是png/jpg
    """
    files = {"file":(img_name,open(img_path,'rb'),img_type)}
    
    response = requests.post(url=url, files=files)
    return response


if __name__=='__main__':
# 上传图片
    res = sendImg(r'../picture/NBP1.png','NBP1.png') # 调用sendImg方法
    print(res)