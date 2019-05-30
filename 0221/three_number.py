# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 18:39
# @Author: xiaoxiao
# @File  : three_number.py
count=0
s=[]
for a in [1,2,3,4]:
    for b in [1,2,3,4]:
        for c in [1,2,3,4]:
            if a!=b and a!=c and b!=c:
                count+=1
                s.append(a*100+b*10+c)
print("互不相同且无重复数字的三位数有{}个，为{}".format(count,s))

