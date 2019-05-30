# -*- coding:utf-8 -*-
# @Time  : 2019/5/22 17:10
# @Author: xiaoxiao
# @File  : lubandai.py

import json
import unittest

from ddt import ddt, data, unpack

from class_0412.common import http_requests
from class_0412.common.do_excel import do_excel
from class_0412.common.excel_data import lubandai
from class_0412.common.filename import filename
import time



@ddt
class lubandai_Testcase(unittest.TestCase):
    print(lubandai)
    @data(*lubandai)
    @unpack
    def test_login(self,caseid,title,url,data,method,expected):
        resp=http_requests.http_requests()
        resp=resp.method(method,url,params=data,token=getattr(http_requests.context,"token"))
        f=do_excel(filename,"lubandai")
        f.write(resp.text, caseid + 1, 7)
        try:
            self.assertEqual(json.loads(expected),resp.json())
            setattr(http_requests.context,"token",resp.headers["token"])
            time.sleep(60)
            print("休眠60s")
        except AssertionError as e :
            f.write("FAIL",caseid+1,8)
            raise e
        else:
            f.write("pass", caseid + 1, 8)
        finally:
            f.close()

if __name__ == '__main__':
    unittest.main()