# -*- coding:utf-8 -*-
# @Time  : 2019/3/8 12:38
# @Author: xiaoxiao
# @File  : User.py

class User:
    first_name="xiaoxiao"
    last_name="chen"
    sex="女"
    age=18
    @classmethod
    def describe_user(cls):
        print("用户的姓名：",cls.last_name+cls.first_name)
        print("用户的性别：",cls.sex)
        print("用户的年龄：",cls.age)
    @classmethod
    def greet_user(cls):
        return "{}，你好！".format(cls.last_name+cls.first_name)


User.describe_user()
res=User.greet_user()
print(res)

