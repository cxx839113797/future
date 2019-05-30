# -*- coding:utf-8 -*-
# @Time  : 2019/3/10 17:11
# @Author: xiaoxiao
# @File  : Restaurant_1.py

from class_0309.Restaurant import Restaurant
class Restaurant_1(Restaurant):
    def discount(self,discount):
        self.discount=discount
    def pay_money(self,*args):
        sum=0
        for item in args:
            sum+=item
        print("需要支付餐费用：",sum*self.discount)
    def open_restaurant(self):
        print("{}欢迎您！".format(self.restaurant_name))
if __name__ == '__main__':
    r = Restaurant_1("川菜馆", "麻婆豆腐")
    r.open_restaurant()
    r.discount(0.8)
    r.pay_money(23,17,40)


