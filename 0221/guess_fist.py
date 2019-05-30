# -*- coding:utf-8 -*-
# @Time  : 2019/2/22 14:56
# @Author: xiaoxiao
# @File  : guess_fist.py

import random
role = {1:"曹操",2:"张飞",3:"刘备"}
guess= {1:"剪刀",2:"石头",3:"布"}
try:
    name= int(input("请输入数字选择你的角色：1曹操,2张飞,3刘备\n"))
    if name <1 or name >3:
        print("请输入1-3的数字")
    else:
        a=0
        b=0
        c=0
        isContinue='y'
        while 1:
            player=int(input("请输入数字选择猜拳：1剪刀,2石头,3布\n"))
            if player >=1 and player <=3:
                computer=random.randint(1,3)
                print('电脑出拳结果为：{}'.format(guess[computer]))
                if(player==computer):
                    a += 1
                    print("平局")
                elif player==2 and computer==1 or player==3 and computer==2 or player ==1 and computer ==3:
                    b += 1
                    print("赢")
                else:
                    c+=1
                    print("输")
                isContinue=input("是否继续？按y继续，按n退出\n")
                while isContinue not in ['y','n']:
                    isContinue = input("是否继续？按y继续，按n退出\n")
                if isContinue=='n':
                    print("%s赢%d局，电脑赢%d局，平局%d次"%(role[name], b, c, a))
                    break
                else:
                    continue
            else:
                print("请输入1-3的数字")
                break
except ValueError:
    print("请输入正确的值")
