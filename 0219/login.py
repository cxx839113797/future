# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 15:17
# @Author: xiaoxiao
# @File  : login.py

d={'name':'huahua','pwd':'123456'}
for count in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username ==d['name'] and password == d['pwd']:
        print('登录成功')
        break
    else:
        print('用户名或密码错误,你还有{}次机会！！'.format(2-count))