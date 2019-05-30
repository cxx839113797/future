# -*- coding:utf-8 -*-
# @Time  : 2019/3/18 20:05
# @Author: xiaoxiao
# @File  : configParse.py

from configparser import ConfigParser

class config:
    def __init__(self,fileName,encoding="utf-8"):
        self.cf=ConfigParser()
        self.cf.read(fileName,encoding=encoding)
    #读取所有的sections
    def read_sections(self):
        return self.cf.sections()
    #读取指定section下的所有options名称
    def read_options(self,section_name):
        return self.cf.options(section_name)
    #读取指定section下的指定option值
    def read_option(self,section_name,option_name):
        return self.cf.get(section_name,option_name)
    #读取的option值为int类型
    def read_int(self,section_name,option_name):
        return self.cf.getint(section_name,option_name)
    #读取的option值为bool类型
    def read_bool(self,section_name,option_name):
        return self.cf.getboolean(section_name,option_name)
    #读取的option值为float类型
    def read_float(self,section_name,option_name):
        return self.cf.getfloat(section_name,option_name)
    #读取指定section的所有option键值对
    def read_items(self,section_name):
        return self.cf.items(section_name)



if __name__ == '__main__':
    cf=config("py.conf")
    print(cf.read_sections())
    print(cf.read_options("db"))
    print(cf.read_option("excel","sex"))
    res_int=cf.read_int("db", "db_port")
    print("res_int的值为{}，类型为{}".format(res_int,type(res_int)))
    res_bool=cf.read_bool("excel", "res")
    print("res_bool的值为{}，类型为{}".format(res_bool,type(res_bool)))
    res_float=cf.read_float("excel", "row")
    print("res_float的值为{}，类型为{}".format(res_float,type(res_float)))
    print(cf.read_items("excel"))