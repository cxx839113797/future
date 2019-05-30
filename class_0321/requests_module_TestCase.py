# -*- coding:utf-8 -*-
# @Time  : 2019/3/21 21:12
# @Author: xiaoxiao
# @File  : test.py

import unittest
from class_0321.requests_module import submit_method

#正常用例
class Test_Nomal(unittest.TestCase):
    # get正常登录
    def test_getNormal(self):
        expected=[200,"登录成功"]
        res=submit_method("get","http://47.107.168.87:8080/futureloan/mvc/api/member/login"
                      ,params={"mobilephone":"18688773467" ,"pwd":"123456"}).http_request()
        self.assertEqual(expected[0],res.status_code)
        self.assertIn(expected[1],res.text)
    # post正常登录
    def test_postNormal(self):
        expected=[200,"登录成功"]
        res=submit_method("post","http://47.107.168.87:8080/futureloan/mvc/api/member/login"
                      ,params={"mobilephone":"18688773467" ,"pwd":"123456"}).http_request()
        self.assertEqual(expected[0],res.status_code)
        self.assertIn(expected[1],res.text)
#异常用例
class Test_Error(unittest.TestCase):
    # 手机号码为空
    def test_getNonePhone(self):
        expected=[200,"手机号不能为空"]
        res=submit_method("get","http://47.107.168.87:8080/futureloan/mvc/api/member/login"
                      ,params={"mobilephone":"" ,"pwd":"123456"}).http_request()
        self.assertEqual(expected[0],res.status_code)
        self.assertIn(expected[1],res.text)
    # 密码为空
    def test_getNonePwd(self):
        expected=[200,"密码不能为空"]
        res=submit_method("get","http://47.107.168.87:8080/futureloan/mvc/api/member/login"
                      ,params={"mobilephone":"18688773467" ,"pwd":""}).http_request()
        self.assertEqual(expected[0],res.status_code)
        self.assertIn(expected[1],res.text)