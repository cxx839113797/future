# -*- coding:utf-8 -*-
# @Time  : 2019/4/13 23:57
# @Author: xiaoxiao
# @File  : login_testcase.py

from class_0423.common.http_requests import http_requests
from class_0423.common.do_excel import do_excel
from class_0423.common.constants import excel_name,login_sheet
from class_0423.common.log_config import log_config
from ddt import ddt,data
from class_0423.common.regulax import regulax
import unittest
import json
log=log_config(__name__)
@ddt
class loginTestcase(unittest.TestCase):
    case = do_excel(excel_name, login_sheet)
    cases=case.read()
    @classmethod
    def setUpClass(cls):
        cls.session=http_requests()
        cls.datafill = do_excel(excel_name, login_sheet)
    @data(*cases)
    def test_login(self,case):
        log.info("测试标题：{}".format(case.title))
        case.data=regulax(case.data)
        resp=self.session.Session(case.method,case.url,case.data)
        self.datafill.write(resp.text,case.caseid + 1, 7)
        try:
            self.assertEqual((json.loads(case.expected)["status"]),resp.json()["status"])
            self.assertEqual((json.loads(case.expected)["code"]), resp.json()["code"])
            self.assertEqual((json.loads(case.expected)["msg"]), resp.json()["msg"])
            self.datafill.write("PASS", case.caseid + 1, 8)
        except AssertionError as e:
            self.datafill.write("FAIL",case.caseid+1,8)
            log.error("报错：{}".format(e))
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.datafill.close()

if __name__ == '__main__':
      unittest.main()





