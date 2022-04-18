'''
Description: 
Author: xiaoming
Date: 2022-01-15 12:37:08
'''
from asyncio import Handle, sleep
from cgitb import handler
from socket import timeout
import time
from turtle import title
from pywinauto.application import Application
import pywinauto
from PIL import ImageGrab,ImageSequence


# 开发环境
app = Application(backend='win32').start(r'..\..\iKanban\iKanban.exe')
# app = Application(backend='win32').start(r'C:\Users\xiaoming\Desktop\iKanban\iKanban.exe')

if app.window(title_re = 'iKanbanStart',class_name = "#32770").exists(timeout=2):
    print("请检查网络！")

app2 = Application(backend='uia')
app2 = app2.connect(title_re ='Form',class_name_re="WindowsForms10")
app2.window(title_re ='Form',class_name_re="WindowsForms10").wait('ready', timeout=10)
print(app2.window(title ='Form1',class_name_re="WindowsForms10").print_control_identifiers())

main = app2.window(title ='Form1',class_name_re="WindowsForms10").child_window(auto_id="WbsMain", control_type="Pane")
main.child_window(title="user", auto_id="txtAccount", control_type="Edit").set_text('xiaoming') 
main.child_window(title="password", auto_id="txtPassword", control_type="Edit").set_text('password')
main.child_window(title="Login", auto_id="btnLogin", control_type="Button").click()


Production = app2.window(title ='Form1',class_name_re="WindowsForms10")
Production=Production.child_window(title="Production", auto_id="btnLib1", control_type="Hyperlink")
Production.wait('ready',timeout=10)
Production.click_input(button='left', double=True)


app2["Form1"]["NB\r\n生产效率\r\n看板"].wait('visible')
app2["Form1"]["NB\r\n生产效率\r\n看板"].click_input()

set = app2.window(title ='Form1',class_name_re="WindowsForms10")
set = set.child_window(title="", auto_id="LblSetting", control_type="Text").click_input()

paneSet = app2.window(title ='Form1',class_name_re="WindowsForms10")

paneSet.child_window(title="图表", auto_id="rbtLine", control_type="RadioButton").click()

if paneSet.child_window(title="WarRoom", auto_id="rbtWarRoom", control_type="RadioButton").exists(timeout = 3):
    pass

paneSet.child_window(title="WarRoom", auto_id="rbtWarRoom", control_type="RadioButton").click()
paneSet.child_window(title="关闭", control_type="Button").wait("ready")
paneSet.child_window(title="关闭", control_type="Button").click_input()

if paneSet.child_window(title="关闭", control_type="Button").exists(timeout=1):
    time.sleep(2)

time.sleep(2)

app2.window(title ='Form1').child_window(auto_id="WbsMain", control_type="Pane").capture_as_image().save(r'../picture/NBWarRoom.png')

# print(app2.window(title ='Form1',class_name_re="WindowsForms10").print_control_identifiers())

app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").click_input()
