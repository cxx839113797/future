# -*- coding:utf-8 -*-
# @Time  : 2019/3/21 17:01
# @Author: xiaoxiao
# @File  : log_config.py

import logging
from configparser import ConfigParser
class log_config:
    def __init__(self):
        config=ConfigParser()
        config.read("py.conf",encoding="utf-8")
        self.log_out_level = config.get("LOG", "log_out_level")
        self.out_method=config.get("LOG","out_method")
        self.fmt=config.get("LOG","format",raw=True)
        self.fileName=config.get("LOG","fileName")

        self.ch = logging.getLogger("py15")
        format = logging.Formatter(self.fmt)
        if self.out_method == "file":
            fh = logging.FileHandler(self.fileName, encoding="utf-8")
            fh.setLevel(self.log_out_level)
            fh.setFormatter(format)
            self.ch.addHandler(fh)
        elif self.out_method == "console":
            ph = logging.StreamHandler()
            ph.setLevel(self.log_out_level)
            ph.setFormatter(format)
            self.ch.addHandler(ph)
    def debug(self,msg):
         return self.ch.debug(msg)
    def info(self,msg):
         return self.ch.info(msg)
    def warning(self,msg):
        return self.ch.warning(msg)
    def error(self,msg):
        return self.ch.error(msg)
    def critical(self,msg):
        return self.ch.critical(msg)











