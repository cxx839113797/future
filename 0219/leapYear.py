# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 11:50
# @Author: xiaoxiao
# @File  : leapYear.py

def leapYear():
    year = int(input("请输入一个年份："))
    if (year%4==0 and not year%100==0) or year%400==0:
        print('{}是闰年'.format(year))
    else:
        print('{}不是闰年'.format(year))
    return leapYear()

leapYear()