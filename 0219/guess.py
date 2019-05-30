# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 14:51
# @Author: xiaoxiao
# @File  : guess.py
import random

def guess():
    computer = random.randint(1,9)
    n = input('请输入一个数字：')
    print('computer={}'.format(computer))
    if n.isdigit():
        b = int(n)
        if computer<b:
            print("bigger")
        elif computer>b:
            print('less')
        elif computer==b:
            print('equal')
    return guess()

guess()