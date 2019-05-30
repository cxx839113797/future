# -*- coding:utf-8 -*-
# @Time  : 2019/3/21 21:12
# @Author: xiaoxiao
# @File  : test.py

import unittest
from class_0323.requests_module import submit_method
from ddt import ddt,data,unpack
from class_0323.excel_read_write import excel_read_write
import HTMLTestRunnerNew
import json
from openpyxl import load_workbook

@ddt
class ddt_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cookies=None

    s=excel_read_write("TestData.xlsx","test_data").excel_read()

    @data(*s)
    @unpack
    def test_http(self,row,method,url,params,msg):
        res=submit_method(method,url,json.loads(params)).http_request(ddt_TestCase.cookies)
        if res.cookies:
            ddt_TestCase.cookies=res.cookies
        self.assertEqual(msg,int(res.json()["code"]))


