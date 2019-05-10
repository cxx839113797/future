# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 18:58
# @Author: xiaoxiao
# @File  : recharge_case.py

from class_0423.common.http_requests import http_requests
from class_0423.common.do_excel import do_excel
from class_0423.common.constants import excel_name,recharge_sheet
from class_0423.common.regulax import regulax
from class_0423.common.do_mysql import DoMysql
from class_0423.common.log_config import log_config
from ddt import ddt,data
import unittest
import json
log=log_config(__name__)
@ddt
class rechargeTestcase(unittest.TestCase):
    case = do_excel(excel_name,recharge_sheet)
    cases=case.read()
    @classmethod
    def setUpClass(cls):
        cls.session=http_requests()
        cls.mysql=DoMysql()
        cls.datafill = do_excel(excel_name, recharge_sheet)
    @data(*cases)
    def test_recharge(self,case):
        log.info("测试标题：{}".format(case.title))
        case.data = regulax(case.data)
        if case.check_sql:
            case.check_sql = regulax(case.check_sql)
            before=self.mysql.fetch_One(case.check_sql)["leaveamount"]
        resp=self.session.Session(case.method,case.url,case.data)
        self.datafill.write(resp.text,case.caseid + 1, 7)
        try:
            self.assertEqual((json.loads(case.expected)["status"]),resp.json()["status"])
            self.assertEqual((json.loads(case.expected)["code"]), resp.json()["code"])
            self.assertEqual((json.loads(case.expected)["msg"]), resp.json()["msg"])
            self.datafill.write("PASS", case.caseid + 1, 8)
            if case.check_sql:
                after=self.mysql.fetch_One(case.check_sql)["leaveamount"]
                self.assertEqual(before+int(json.loads(case.data)["amount"]),after)
        except AssertionError as e:
            datafill.write("FAIL",case.caseid+1,8)
            log.error("报错：{}".format(e))
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.mysql.close()

if __name__ == '__main__':
    unittest.main()