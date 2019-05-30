# -*- coding:utf-8 -*-
# @Time  : 2019/3/22 20:53
# @Author: xiaoxiao
# @File  : load_TestCase.py

from class_0321.requests_module_TestCase import * #导入类

loader=unittest.TestLoader()#创建一个加载器
suite=unittest.TestSuite()#创建一个用例集
suite.addTest(loader.loadTestsFromTestCase(Test_Nomal))#用例集通过加载器添加测试用例类
suite.addTest(loader.loadTestsFromTestCase(Test_Error))

runner=unittest.TextTestRunner()#创建一个执行者
runner.run(suite)#执行用例