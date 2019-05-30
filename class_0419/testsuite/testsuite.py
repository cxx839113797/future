# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 21:14
# @Author: xiaoxiao
# @File  : testsuite.py

import unittest
from class_0419.testcase import login_testcase
from class_0419.testcase import recharge_testcase
from class_0419.testcase import register_testcase
from class_0419.testcase import addloan_testcase
from class_0419.testcase import audit_testcase
from class_0419.testcase import bidloan_testcase



testsuite=unittest.TestSuite()
loader=unittest.TestLoader()
testsuite.addTest(loader.loadTestsFromModule(register_testcase))
testsuite.addTest(loader.loadTestsFromModule(login_testcase))
testsuite.addTest(loader.loadTestsFromModule(recharge_testcase))
testsuite.addTest(loader.loadTestsFromModule(addloan_testcase))
testsuite.addTest(loader.loadTestsFromModule(audit_testcase))
testsuite.addTest(loader.loadTestsFromModule(bidloan_testcase))



