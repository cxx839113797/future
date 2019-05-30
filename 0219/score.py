# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 10:09
# @Author: xiaoxiao
# @File  : score.py

def print_score():
    score = input("请输入学生的成绩：")
    if score.isdigit():
        s=int(score)
        if s>100 or s<0:
            print("超出范围，成绩应在0-100内")
        elif s>=90:
            print("优秀")
        elif s>=80:
            print("良好")
        elif s>=70:
            print("一般")
        elif s>=60:
            print("及格")
        else:
            print("不及格")
    else:
        print("请输入正确的学生成绩")
    return print_score()

print_score()