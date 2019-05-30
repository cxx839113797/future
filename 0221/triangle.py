# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 17:20
# @Author: xiaoxiao
# @File  : triangle.py

#直角三角形
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()

for i in range(5):
    print("*"*(i+1))

#等边三角形


for i in range(5):
    print(" " * (4 - i) + "*" + " *" * i)


for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()


