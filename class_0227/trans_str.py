# -*- coding:utf-8 -*-
# @Time  : 2019/2/27 0:32
# @Author: xiaoxiao
# @File  : trans_str.py


def trans_str(s):
    res=s.swapcase()
    str1="asdfASDF"
    str2="zhwuZHWU"
    tran_table=str.maketrans(str1,str2)
    tran_str=res.translate(tran_table)
    print(tran_str)

s="sdSdsfdAdsdsdfsfdsdASDSDFDSFa"
trans_str(s)