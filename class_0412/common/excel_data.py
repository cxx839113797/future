# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 2:03
# @Author: xiaoxiao
# @File  : excel_data.py

from class_0412.common.do_excel import do_excel
from class_0412.common.filename import filename

def excel_data(sheetname):
    s=do_excel(filename,sheetname)
    params=s.read(column=6)
    s.close()
    return params

login_params=excel_data("login")
print(login_params)
register_params=excel_data("register")
lubandai=excel_data("lubandai")
print(lubandai)
