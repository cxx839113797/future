# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 0:06
# @Author: xiaoxiao
# @File  : filename.py
import os


base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_name=os.path.join(base_dir,"data","cases.xlsx")

login_sheet="login"
register_sheet="register"
recharge_sheet="recharge"


