# -*- coding:utf-8 -*-
# @Time  : 2019/5/5 2:38
# @Author: xiaoxiao
# @File  : sendMCode.py

import unittest
import json
import suds.WebFault
from suds.client import Client
from webservice.common.do_excel import DoExcel
from ddt import data,ddt,unpack
@ddt
class SendMCode(unittest.TestCase):
    s=DoExcel()
    @data(s)
    def test_SendMCode(self,case):
        webservice=Client(case.url)
        try:
            result=webservice.service.sendMCode(case.t)
            self.assertEqual(str(result.retCode),json.loads(case.expected)["retCode"])
            self.assertEqual(str(result.retInfo), json.loads(case.expected)["retInfo"])

        except suds.WebFault as e:
            self.assertIn(str(e), json.loads(case.expected))




