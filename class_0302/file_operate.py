# -*- coding:utf-8 -*-
# @Time  : 2019/3/3 14:31
# @Author: xiaoxiao
# @File  : file_operate.py

import io

def file_operate(file):
    file1 = open(file, "r")
    f = file1.readlines()
    c=[]
    for i in f:
        s=i.strip().split("@")
        d = {}
        for j in s:
            l=j.split(":",1)
            d[l[0]]=l[1]
        c.append(d)
    print(c)


file_operate(r"C:\Users\Administrator\Desktop\file文件.txt")




# for intem in res:
#     intem = intem.strip("\n").split(",")
#     dict={}
#     L=[]
#     for a in intem:
#         b=a.split('@')
#         for c in b:
#             d=c.split(':',1)
#             dict[d[0]] =d[1]
#         L.append(dict)
#         print(L)