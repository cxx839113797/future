# -*- coding:utf-8 -*-
# @Time  : 2019/3/22 21:02
# @Author: xiaoxiao
# @File  : load_TestModule.py


import unittest
from class_0321 import requests_module_TestCase #导入用例模块

loader=unittest.TestLoader() #创建一个加载器
suite=unittest.TestSuite() #创建一个用例集
suite.addTest(loader.loadTestsFromModule(requests_module_TestCase))#用例集通过加载器添加测试模块

runner=unittest.TextTestRunner()#创建一个执行者
runner.run(suite)#执行用例