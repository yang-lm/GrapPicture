'''
Description: 
Author: xiaoming
Date: 2022-01-22 11:06:35
'''
import msvcrt, sys, os
print('password: ', end='', flush=True)

ch = msvcrt.getch()
#回车
msvcrt.putch(b'\n')
print('输入的密码是：%s' % b''.join(li).decode())
     