'''
Description: 
Author: xiaoming
Date: 2022-01-25 14:29:55
'''
import time
import logging
# from autoSet import glog
# glog = "./log/"
#输出日志
def grablog(a):
    date = time.strftime("%Y-%m-%d", time.localtime())
    logging.basicConfig(level=logging.INFO,filename=f"log/{date}.log")
    logging.info(a)

if __name__ =="__main__":
    grablog(3)