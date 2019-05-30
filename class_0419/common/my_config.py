# -*- coding:utf-8 -*-
# @Time  : 2019/4/18 16:19
# @Author: xiaoxiao
# @File  : myConfig.py

import configparser
from class_0419.common.constants import global_name,online_name,test_name

class myConfig:
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(global_name)
        switch=self.config.getboolean("switch","on")
        if switch:
            self.config.read(online_name)
        else:
            self.config.read(test_name)

    def get(self,section,option):
        return self.config.get(section,option)

config=myConfig()
