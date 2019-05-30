# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 16:52
# @Author: xiaoxiao
# @File  : soccer.py

sex={"m":"男性","f":"女性"}
count = 0
for i in range(10):
    try:
        s=input("请输入第{}个用户性别(m代表男性，f代表女性)：".format(i+1))
        age=int(input("请输入第{}个年龄：".format(i+1)))
    except ValueError:
        print("输入错误")
    else:
        if s=='f'and age>=10 and age <=12:
            count+=1
            print('这个人可以加入球队')
        else:
            print('这个人不可以加入球队')
print("满足条件的总人数为：{}".format(count))
