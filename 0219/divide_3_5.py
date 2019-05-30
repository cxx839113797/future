# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 11:36
# @Author: xiaoxiao
# @File  : divide_3_5.py
def divide():
    num = int(input('请任意输入一个数：'))
    if num%3==0 and num%5==0:
        print('%d能同时被3和5整除'%num)
    else:
        print('%d不能同时被3和5整除' % num)
    return divide()

divide()
