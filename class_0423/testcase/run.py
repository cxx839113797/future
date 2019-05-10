# -*- coding:utf-8 -*-
# @Time  : 2019/5/10 7:26
# @Author: xiaoxiao
# @File  : run.py

import sys

sys.path.append("./")
import unittest
from class_0423.common import constants
import HTMLTestRunnerNew


case=unittest.defaultTestLoader.discover(constants.case_dir,"test_*.py")


with open(constants.report_dir+"\\future.html","wb") as f:
    runner=HTMLTestRunnerNew.HTMLTestRunner\
        ( stream=f, verbosity=2,title="这是前程贷的测试报告",description="测试前程贷接口",tester="xiaoxiao")
    runner.run(case)