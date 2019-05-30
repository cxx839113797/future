# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 22:30
# @Author: xiaoxiao
# @File  : run_testsuite.py

import HTMLTestRunnerNew
from class_0416.common.constants import report_name
from class_0416.testsuite.testsuite import testsuite

with open(report_name,"wb") as f:
    runner=HTMLTestRunnerNew.HTMLTestRunner\
        ( stream=f, verbosity=2,title="这是xiaoxiao的测试报告",description="测试添加标的、审核、投资接口",tester="xiaoxiao")
    runner.run(testsuite)
