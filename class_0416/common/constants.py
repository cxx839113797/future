# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 0:06
# @Author: xiaoxiao
# @File  : filename.py
import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_name=os.path.join(base_dir,"data","cases.xlsx")
report_name=os.path.join(base_dir,"report","testRepost.html")
global_name=os.path.join(base_dir,"config","global.conf")
online_name=os.path.join(base_dir,"config","online.conf")
test_name=os.path.join(base_dir,"config","test.conf")

login_sheet="login"
register_sheet="register"
recharge_sheet="recharge"
addloan_sheet="add"
audit_sheet="audit"
bidloan_sheet="bidloan"


