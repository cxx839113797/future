# -*- coding:utf-8 -*-
# @Time  : 2019/3/8 11:30
# @Author: xiaoxiao
# @File  : Restaurant.py
class Restaurant:
    def __init__(self,restaurant,cooking_type):
        self.restaurant_name=restaurant
        self.cooking_type = cooking_type
    def describe_restaurant(self):
        print("餐馆的名字是{}".format(self.restaurant_name))
        print("餐馆会做{}".format(self.cooking_type))
    @staticmethod
    def open_restaurant():
        print("餐馆正在营业！")
if __name__ == '__main__':
    r=Restaurant("川菜馆","麻婆豆腐")
    print(r.restaurant_name)
    print(r.cooking_type)
    r.describe_restaurant()
    Restaurant.open_restaurant()





