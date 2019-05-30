# -*- coding:utf-8 -*-
# @Time  : 2019/2/20 10:44
# @Author: xiaoxiao
# @File  : market_sale.py
def sale():
    price = (input("请输入购买价格："))
    if price.isdigit() or (price.count('.')==1 and price.split('.')[0].isdigit() and price.split('.')[1].isdigit()):
        p = float(price)
        if p > 100 :
            print('折扣为%d%%，最终价格为%.2f'%(20,p - p * 0.2))
        elif p>=50 and p<=100:
            print('折扣为%d%%，最终价格为%.2f'%(10, p - p * 0.1))
        else:
            print("无折扣，请原价购买")
    else:
        print("请输入正确的购买价格")
    return sale()
sale()