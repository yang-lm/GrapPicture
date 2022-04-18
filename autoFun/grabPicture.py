'''
Description: 
Author: xiaoming
Date: 2022-01-15 12:37:08
'''
from asyncio import Handle, sleep
from cgitb import handler
from itertools import product
from socket import timeout
import time
from turtle import title
from pywinauto.application import Application
import pywinauto
from PIL import ImageGrab,ImageSequence
from autoSet import *
import logging
import os
# from util.Grablogout import grabLog
from util.grabLog import grablog

def autograb(
    user,  
    password,
    productionAction,
    chartAction,
    pictureName,
    overtime=2,
    
 ):
    try:
        # 打开应用 gdir 是应用的路径名称，该应用是win32 程序
        app = Application(backend='win32').start(gdir)

        # 根据title_re 和 class_name 判断程序是否正常打开
        if app.window(title_re = 'iKanbanStart',class_name = "#32770").exists(timeout=2):
            print("请检查网络！")

        # 链接到对应的页面，该应用打开后的页面是`uia` 类型
        app2 = Application(backend='uia')
        app2 = app2.connect(title_re ='Form',class_name_re="WindowsForms10")

        # 等待应用完全打开，设置超时等待最长时间10s
        app2.window(title_re ='Form',class_name_re="WindowsForms10").wait('ready', timeout=10)
        app2 = app2.connect(title_re ='Form',class_name_re="WindowsForms10")
           
        # 获取客户端的元素
        main = app2.window(title ='Form1',class_name_re="WindowsForms10").child_window(auto_id="WbsMain", control_type="Pane")
        # 输入账号密码
        main.child_window(title="user", auto_id="txtAccount", control_type="Edit").set_text(user) 
        main.child_window(title="password", auto_id="txtPassword", control_type="Edit").set_text(password)
        # 触发click()点击事件，登录客户端
        main.child_window(title="Login", auto_id="btnLogin", control_type="Button").click()

        # 登录后获取客户端的主页面
        Production = app2.window(title ='Form1',class_name_re="WindowsForms10")
        # 获取要操作的页面元素，该元素是超链接
        Production=Production.child_window(title="Production", auto_id="btnLib1", control_type="Hyperlink")
        Production.wait('ready',timeout=10)
        # 超链接没有click事件在这里模拟鼠标点击，这里的click_input 事件是调用了电脑鼠标，进行操作
        Production.click_input(button='left', double=True)
        
        # 等待页面在桌面显示后点击元素
        app2["Form1"][productionAction].wait('visible')
        app2["Form1"][productionAction].click_input()

        set = app2.window(title ='Form1',class_name_re="WindowsForms10")
        set = set.child_window(title="", auto_id="LblSetting", control_type="Text").click_input()

        paneSet = app2.window(title ='Form1',class_name_re="WindowsForms10")
        paneSet.child_window(title="图表", auto_id="rbtLine", control_type="RadioButton").wait('ready', timeout=10)
        paneSet.child_window(title="图表", auto_id="rbtLine", control_type="RadioButton").click()

        # 这里的**chartAction 是python拆解字典的语法
        if paneSet.child_window(**chartAction).exists(timeout = 3):
            pass

        paneSet.child_window(**chartAction).click()
        paneSet.child_window(title="关闭", control_type="Button").wait("ready")
        paneSet.child_window(title="关闭", control_type="Button").click_input()

        i = 0
        while i<8:
            if paneSet.child_window(title="关闭", control_type="Button").exists(timeout=2):
                time.sleep(overtime) 
            else:
                break

        time.sleep(3)
        # 截图存放的路径
        gpictureDir = gpicture + pictureName

        # 截图并保存图片
        app2.window(title ='Form1').child_window(auto_id="WbsMain", control_type="Pane").capture_as_image().save(gpictureDir)
        
        # print(app2.window(title ='Form1',class_name_re="WindowsForms10").print_control_identifiers())
        # app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").click_input()

        # 以关闭进程的方式通过cmd 关闭程序，可以避免客户端卡死。
        os.system(f"taskkill /F /IM iKanban.exe")
    except Exception as e:
        # 日志打印
        logging.exception(e)
        
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
        os.system(f"taskkill /F /IM iKanban.exe")
        # pywinauto.keyboard.send_keys('%{F4}')

        grablog(e)
        grablog(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return 0
    grablog(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 返回截取到的图片名称以及路径，用于发送到数据库。
    grablog([gpictureDir,pictureName])
    return [gpictureDir,pictureName]
