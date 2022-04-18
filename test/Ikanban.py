'''
Description: 
Author: xiaoming
Date: 2022-01-15 12:37:08
'''
from asyncio import Handle
from cgitb import handler
import time
from turtle import title
from pywinauto.application import Application
import pywinauto
from PIL import ImageGrab,ImageSequence


# 开发环境
app = Application(backend='win32').start(r'C:\iKanban\iKanban.exe')

#正式环境
# app = Application(backend='win32').start(r'C:\Users\xiaoming\Desktop\iKanban\iKanban.exe')

# edit_window = app['iKanbanStart']


if app.window(title_re = 'iKanbanStart',class_name = "#32770").exists(timeout=2):
    print("请检查网络！")
# app.window(title_re = 'iKanbanStart',class_name = "#32770").wait('ready', timeout=10)
# print(app.window(title_re = 'iKanbanStart',class_name = "#32770").print_control_identifiers())
# tool = app.window(title_re = 'iKanbanStart',class_name = "#32770")
# app.window(title_re = 'iKanbanStart',class_name = "#32770").Button.click()
# time.sleep(4)

app2 = Application(backend='uia')
app2 = app2.connect(title_re ='Form',class_name_re="WindowsForms10")
app2.window(title_re ='Form',class_name_re="WindowsForms10").wait('ready', timeout=10)
# if app2.window(title ='Form1',class_name_re="WindowsForms10").exists(timeout=2):
#     print("kk")

# app2['Form1']['Kanban'].capture_as_image().save('123.png')
# app2.window(title ='Form1',class_name_re="WindowsForms10").capture_as_image().save('123.png')

# ImageGrab.grab(include_layered_windows = True).save('kk.png')
# print("test-test")
# print(ImageSequence.all_frames(ImageGrab.grab(), lambda im_frame: im_frame.rotate(90)))

# print("loginOut")
# print(app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").print_control_identifiers())
# app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").wait('ready', timeout=10)
# app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").capture_as_image().save('123.png')

main = app2.window(title ='Form1',class_name_re="WindowsForms10").child_window(auto_id="WbsMain", control_type="Pane")
main.child_window(title="user", auto_id="txtAccount", control_type="Edit").set_text('xiaoming') 
main.child_window(title="password", auto_id="txtPassword", control_type="Edit").set_text('password')
main.child_window(title="Login", auto_id="btnLogin", control_type="Button").click()
# time.sleep(3)

# print(app2.window(title ='Form1',class_name_re="WindowsForms10").print_control_identifiers())
# app2['Form1']['Production'].wait('ready')
# app2['Form1']['Production'].click_input(button='left', double=True)

# app2['Form1']['Production'].wait('ready',10)
# app2['Form1']['Production'].click_input(button='left', double=True)
Production = app2.window(title ='Form1',class_name_re="WindowsForms10")
Production=Production.child_window(auto_id="WbsMain", control_type="Pane")
Production=Production.child_window(auto_id="ulItems", control_type="List").child_window(title="Production", auto_id="btnLib1", control_type="Hyperlink")
Production.wait('ready',timeout=10)
Production.click_input(button='left', double=True)

# NB = app2.window(title ='Form1',class_name_re="WindowsForms10")
app2["Form1"]["NB\r\n生产效率\r\n看板"].wait('visible')
app2["Form1"]["NB\r\n生产效率\r\n看板"].click_input()


app2.window(title ='Form1').child_window(auto_id="WbsMain", control_type="Pane").wait('visible',timeout = 10)
app2.window(title ='Form1').child_window(auto_id="WbsMain", control_type="Pane").capture_as_image().save('123.png')

# print(app2.window(title ='Form1',class_name_re="WindowsForms10").print_control_identifiers())
app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").wait('ready')
app2.window(title ='Form1').child_window(title="", auto_id="LblSignOut", control_type="Text").click_input()

# # print(app.connect(auto_id="PnlMove", control_type="UIA_PaneControlTypeId (0xC371)"))


