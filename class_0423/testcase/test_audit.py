# -*- coding:utf-8 -*-
# @Time  : 2019/4/18 22:56
# @Author: xiaoxiao
# @File  : audit_testcase.py

from class_0423.common.http_requests import http_requests
from class_0423.common.do_excel import do_excel
from class_0423.common.constants import excel_name,audit_sheet
from class_0423.common.log_config import log_config
from class_0423.common.regulax import regulax,Regulax
from class_0423.common.do_mysql import DoMysql
from ddt import ddt,data
import unittest
import json

log=log_config(__name__)
@ddt
class auditTestcase(unittest.TestCase):
    case = do_excel(excel_name,audit_sheet)
    cases=case.read()
    @classmethod
    def setUpClass(cls):
        cls.session=http_requests()
        cls.mysql=DoMysql()
        cls.datafill=do_excel(excel_name,audit_sheet)
    @data(*cases)
    def test_audit(self,case):
        log.info("测试标题：{}".format(case.title))
        if case.data.find("$(memberId)") > -1:
            sql = "SELECT MAX(id) FROM future.member "
            data = self.mysql.fetch_One(sql)["MAX(id)"] + 1
            case.data = case.data.replace("$(memberId)", str(data))
        if case.data.find("$(loanId)")>-1:
            sql="SELECT MAX(id) FROM future.loan"
            data=self.mysql.fetch_One(sql)["MAX(id)"]+1
            case.data=case.data.replace("$(loanId)", str(data))
        case.data=regulax(case.data)
        log.debug("请求地址：{}".format(case.url))
        log.debug("请求参数：{}".format(case.data))
        resp=self.session.Session(case.method,case.url,case.data)
        log.debug("响应结果:{}".format(resp.text))
        self.datafill.write(resp.text,case.caseid + 1, 7)
        try:
            self.assertEqual((json.loads(case.expected)["status"]),resp.json()["status"])
            self.assertEqual((json.loads(case.expected)["code"]), resp.json()["code"])
            self.assertEqual((json.loads(case.expected)["msg"]), resp.json()["msg"])
            if resp.json()["msg"]=="加标成功":
                sql="SELECT id FROM future.loan WHERE memberid = 1124 ORDER BY loan.id DESC LIMIT 1"
                loanId=self.mysql.fetch_One(sql)
                loanId=loanId["id"]
                setattr(Regulax,"loanId",str(loanId))
            self.datafill.write("PASS", case.caseid + 1, 8)
        except AssertionError as e:
            self.datafill.write("FAIL",case.caseid+1,8)
            log.error("报错：{}".format(e))
            raise e
    @classmethod
    def tearDownClass(cls):
        log.info("审核标的测试结束")
        cls.session.close()
        cls.datafill.close()
        cls.mysql.close()
if __name__ == '__main__':
    unittest.main()
