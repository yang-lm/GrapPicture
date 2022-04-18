'''
Description: 
Author: xiaoming
Date: 2022-01-21 10:41:33
'''

from autoFun.grabPicture import autograb
from util.uploadImg import sendImg
import time
from autoSet import gaction
# from run import user,password
    

def autoProgram(user,password):
    
    begin_time =time.time()
    for i in gaction:
        # print(i)
        result = autograb(user,password,**i)
        k = 0

        #如果无法抓取页面尝试多1次
        while k<1 and result == 0:
            time.sleep(10)
            k = k+1
            result = autograb(user,password,**i)
             
        if result != 0:
            path,name = result
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print(path,name)
            sendImg(path,name)
        time.sleep(2)
    end_time = time.time()

    run_time = end_time-begin_time
    print(run_time)
    

if __name__ == "__main__":
    #操作指令
    autoProgram(1,2)
    

    
    
    