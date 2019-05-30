# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 18:58
# @Author: xiaoxiao
# @File  : recharge_case.py

from class_0419.common.http_requests import http_requests
from class_0419.common.do_excel import do_excel
from class_0419.common.constants import excel_name,recharge_sheet
from class_0419.common.regulax import Regulax
from ddt import ddt,data
import unittest
import json
@ddt
class rechargeTestcase(unittest.TestCase):
    case = do_excel(excel_name,recharge_sheet)
    cases=case.read()
    case.close()
    @classmethod
    def setUpClass(cls):
        cls.session=http_requests()
    @data(*cases)
    def test_recharge(self,case):
        case.data=Regulax(case.data)
        resp=self.session.Session(case.method,case.url,case.data)
        datafill=do_excel(excel_name,recharge_sheet)
        datafill.write(resp.text,case.caseid + 1, 7)
        try:
            self.assertEqual((json.loads(case.expected)["status"]),resp.json()["status"])
            self.assertEqual((json.loads(case.expected)["code"]), resp.json()["code"])
            self.assertEqual((json.loads(case.expected)["msg"]), resp.json()["msg"])
        except AssertionError as e:
            datafill.write("FAIL",case.caseid+1,8)
            raise e
        else:
            datafill.write("PASS",case.caseid + 1, 8)
        finally:
            datafill.close()
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

if __name__ == '__main__':
    unittest.main()