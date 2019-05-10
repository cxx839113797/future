# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 2:27
# @Author: xiaoxiao
# @File  : register_testcase.py

from class_0423.common.http_requests import http_requests
from class_0423.common.do_excel import do_excel
from class_0423.common.constants import excel_name,register_sheet
from class_0423.common.do_mysql import DoMysql
from class_0423.common.regulax import regulax
from class_0423.common.log_config import log_config
from ddt import ddt,data
import unittest
import json
log=log_config(__name__)
@ddt
class registerTestcase(unittest.TestCase):
    case = do_excel(excel_name,register_sheet)
    cases=case.read()
    @classmethod
    def setUpClass(cls):
        cls.session=http_requests()
        cls.mysql=DoMysql()
        cls.datafill=do_excel(excel_name,register_sheet)
    @data(*cases)
    def test_register(self,case):
        log.info("测试标题：{}".format(case.title))
        if case.check_sql:
            case.check_sql = regulax(case.check_sql)
            before=self.mysql.fetch_One(case.check_sql)["MAX(id)"]
        if case.data.find("136$(mobilephone)")>-1:
            mobilephone=13600000000
            while self.mysql.fetch_One("select mobilephone from future.member where mobilephone="+str(mobilephone)):
                mobilephone+=1
            case.data=case.data.replace("136$(mobilephone)",str(mobilephone))
        case.data=regulax(case.data)
        resp=self.session.Session(case.method,case.url,case.data)
        self.datafill.write(resp.text,case.caseid + 1, 7)
        try:
            self.assertEqual((json.loads(case.expected)["status"]),resp.json()["status"])
            self.assertEqual((json.loads(case.expected)["code"]), resp.json()["code"])
            self.assertEqual((json.loads(case.expected)["msg"]), resp.json()["msg"])
            self.datafill.write("PASS", case.caseid + 1, 8)
            if case.check_sql:
                after=self.mysql.fetch_One(case.check_sql)["MAX(id)"]
                self.assertEqual(int(before)+1,int(after))
        except AssertionError as e:
            self.datafill.write("FAIL",case.caseid+1,8)
            log.error("报错：{}".format(e))

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.mysql.close()
        cls.datafill.close()

if __name__ == '__main__':
    unittest.main()