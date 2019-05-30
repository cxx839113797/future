# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 2:27
# @Author: xiaoxiao
# @File  : register_testcase.py

from class_0419.common.http_requests import http_requests
from class_0419.common.do_excel import do_excel
from class_0419.common.constants import excel_name,register_sheet
from class_0419.common.do_mysql import DoMysql
from class_0419.common.regulax import Regulax
from ddt import ddt,data
import unittest
import json
@ddt
class registerTestcase(unittest.TestCase):
    case = do_excel(excel_name,register_sheet)
    cases=case.read()
    def setUp(self):
        self.session=http_requests()
        self.mysql=DoMysql()
    @data(*cases)
    def test_register(self,case):

        if case.data.find("$mobilephone")>-1:
            sql="select max(mobilephone) from future.member"
            data=int(self.mysql.fetch_One(sql)[0])+1
            case.data=case.data.replace("$mobilephone",str(data))
        case.data=Regulax(case.data)
        resp=self.session.Session(case.method,case.url,case.data)
        datafill=do_excel(excel_name, register_sheet)
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
    def tearDown(self):
        self.session.close()
        self.mysql.close()

if __name__ == '__main__':
    unittest.main()