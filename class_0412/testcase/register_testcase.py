# -*- coding:utf-8 -*-
# @Time  : 2019/4/14 2:27
# @Author: xiaoxiao
# @File  : register_testcase.py

import json
import unittest

from ddt import ddt, data, unpack

from class_0412.common import http_requests
from class_0412.common.do_excel import do_excel
from class_0412.common.excel_data import register_params
from class_0412.common.filename import filename


@ddt
class Login_Testcase(unittest.TestCase):
    @data(*register_params)
    @unpack
    def test_login(self,caseid,title,url,param,method,expected):
        resp=http_requests.http_requests()
        resp=resp.method(method,url,param)
        f=do_excel(filename,"register")
        f.write(resp.text, caseid + 1, 7)
        try:
            self.assertEqual(json.loads(expected),resp.json())
        except AssertionError:
            f.write("FAIL",caseid+1,8)
        else:
            f.write("pass", caseid + 1, 8)
        finally:
            f.close()

if __name__ == '__main__':
    unittest.main()