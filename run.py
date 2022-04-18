'''
Description: 
Author: xiaoming
Date: 2022-01-21 19:33:42
'''

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from main import autoProgram
from util.userInput import glogin
# from autoSet import gpassword,guser

sched =BlockingScheduler(timezone='Asia/Shanghai')
# sched.add_job(my_job, 'interval', seconds=5)


password,user = glogin()
# print(gpassword,guser )
sched.add_job(autoProgram, 'cron', minute="50,20", hour="*",args=[password,user])
# sched.add_job(autoProgram, 'cron', second="*", minute="*",args=[password,user])

while True:
    try:
        print("Ikanban自动截图任务自动执行中...")
        sched.start()
    except:
        print("Ikanban自动截图任务执行失败，请关闭Ikanban再重启！")

