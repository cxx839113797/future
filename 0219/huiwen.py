# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 12:42
# @Author: xiaoxiao
# @File  : huiwen.py
def huiwen():
    num = input('请输入一个数：')
    l=len(num)
    if l==1:
        print('{}是回文数'.format(num))
    elif num[0]=='0':
        print('{}不是回文数'.format(num))
    elif num[0]!='0':
        for n in range(l):
            if num[n]==num[l-n-1]:
                if n==l//2-1:
                    print('{}是回文数'.format(num))
                    break
            else:
                print('{}不是回文数'.format(num))
                break
    return huiwen()
huiwen()