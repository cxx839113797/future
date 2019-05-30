# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 17:59
# @Author: xiaoxiao
# @File  : multiplucation.py

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,j*i),end='\t')
    print()