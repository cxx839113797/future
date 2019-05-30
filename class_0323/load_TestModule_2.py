# -*- coding:utf-8 -*-
# @Time  : 2019/3/22 21:02
# @Author: xiaoxiao
# @File  : load_TestModule.py


import unittest
from class_0323 import requests_module_TestCase #导入用例模块

class unit_test():
    def loader_testcase(self):
        loader=unittest.TestLoader() #创建一个加载器
        suite=unittest.TestSuite() #创建一个用例集
        suite.addTest(loader.loadTestsFromModule(requests_module_TestCase))
        runner=unittest.TextTestRunner()
        runner.run(suite)#执行用例

if __name__ == '__main__':
    unit_test().loader_testcase()
