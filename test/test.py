'''
Description: 
Author: xiaoming
Date: 2022-01-16 12:40:08
'''
from pywinauto import application
from time import sleep
import ctypes
import sys
import win32api
import os

if ctypes.windll.shell32.IsUserAnAdmin():
    i = 1
    allexp = everyexp = 0
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

print('请将此脚本和新平台快捷方式放在一起')
print('5秒后开始运行')
sleep(1)

app = application.Application(backend='uia')
xx = os.getcwd() + '\新平台.lnk'
win32api.ShellExecute(0, 'open', xx, '', '', 1)
sleep(4)

app.connect(title_re='公测平台', class_name='Window')
app.window(title_re="公测平台")['登录'].wait('ready', timeout=10)
app.window(title_re="公测平台")['登录'].click()

app.window(title='MainWindow', class_name='Window').wait('visible')
app.connect(title='MainWindow', class_name='Window')
app['MainWindow']['关闭'].wait('ready')
app['MainWindow']['关闭'].click()
sleep(2)
app['MainWindow'].listbox['Client.ListItemProp_Lobby'].select().click_input(button='left', double=True)

while i:
    i += 1
    app['MainWindow'].child_window(title="创建房间", control_type="Button").wait('ready')
    app['MainWindow']['创建房间'].click()

    app.window(title='创建房间', class_name='Window').wait('ready')
    app.connect(title='创建房间', class_name='Window')

    app['创建房间'].child_window(auto_id="pwd", control_type="Edit").type_keys('1')
    app['创建房间'].child_window(title="创建房间（Enter）", auto_id="createButton", control_type="Button").wait('ready')
    app['创建房间']['创建房间（Enter）'].click()

    os.system("time 1:00:00")
    app.window(title='MainWindow', class_name='Window').wait('ready')
    app.connect(title='MainWindow', class_name='Window')
    app['MainWindow'].child_window(title="开始游戏", control_type="Button").wait('ready')
    app['MainWindow']['开始游戏'].click()
    sleep(2)
    os.system("time 2:00:00")
    os.system("taskkill /im gamemd-spawn.exe /f")
    print('\n')
    while 1:
        sleep(0.5)
        lst = app['MainWindow'].child_window(auto_id="Frame_Right_Lobby", control_type="Pane").Static.texts()
        if lst[0] != '等待程序结束中.....':
            break
    list1 = list(lst[0])
    print('第', i - 1, '局')
    if list1[-4] == '经':
        loop = input('本局经验已上限 是否停止 y/n \n')
        if loop == 'y':
            print('脚本结束,运行了', i - 1, '局，经验增加', int(everyexp) * (i - 2))
            print('本脚本是免费的，作者b站ID:67here,记得修正系统时间')
            sleep(5)
            break
        else:
            app['MainWindow']['返回大厅'].wait('ready')
            app['MainWindow']['返回大厅'].click()
    else:
        allexp_startloaction = list1.index('验') + 2
        allexp_endloaction = list1.index('(')
        everyexp_startlocation = list1.index('(') + 2
        everyexp_endlocation = list1.index(')')

        allexp = ''.join(list1[allexp_startloaction:allexp_endloaction])
        everyexp = ''.join(list1[everyexp_startlocation:everyexp_endlocation])

        print('当前总经验为:', allexp)
        print('本局经验增加:', everyexp)
        app['MainWindow']['返回大厅'].wait('ready')
        app['MainWindow']['返回大厅'].send_keys("{VK_SHIFT down}")