# -*- coding:utf-8 -*-
# @Time  : 2019/2/16 13:12
# @Author: xiaoxiao
# @File  : dict_task_0216.py

#从控制台的输出可以发现，d中两个键True和False的值分别显示为d 中另外两个键1和0的值，且1和0的键值对未显示在控制台。
#结论：True和False 在python中的值为1和0，与d中 0和1  键值对的键相同，而字典中的键具有唯一性，不能存在相同的键，
#      所以只显示了前面的True和False的键而不显示后面0和1的键，但是0和1的值会覆盖True和False的值
d = {"name": '华华',
     'hobby': '学Python',
     'age': 18,
     'score': {'en':120,'math':99.99,'ch':'A'},
     'friend': ['bay max','小CC','如意'],
     True: 'good_man',
     0.02: 'python',
     False: '这个value对应的key是布尔值',
     (1, 2, 3): '我就是元组大大！！！',
     0: '这是真爱呀',
     1: 'score is 99.9'}

print(0 in d.keys())