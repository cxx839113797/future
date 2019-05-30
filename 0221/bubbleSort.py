# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 18:08
# @Author: xiaoxiao
# @File  : bubbleSort.py

a=[1,7,4,89,34,2]
for k in range(len(a)-1):
    for i in range(len(a)-1):
       if a[i+1]>a[i]:
           continue
       else:
           a[i],a[i+1]=a[i+1],a[i]
print(a)
