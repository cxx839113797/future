# -*- coding:utf-8 -*-
# @Time  : 2019/3/22 19:24
# @Author: xiaoxiao
# @File  : TestSuite_requests.py


from class_0321.requests_module_TestCase import * #导入模块
class TestSuite_Testcase_1():

    suite=unittest.TestSuite() #创建一个用例集
    suite.addTest(Test_Nomal("test_getNormal"))#用例集直接添加类下面的一条用例
    suite.addTest(Test_Nomal("test_postNormal"))
    suite.addTest(Test_Error("test_getNonePhone"))
    suite.addTest(Test_Error("test_getNonePwd"))

    runner=unittest.TextTestRunner()#创建一个执行者
    runner.run(suite)#执行用例




