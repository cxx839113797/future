# -*- coding:utf-8 -*-
# @Time  : 2019/4/21 19:23
# @Author: xiaoxiao
# @File  : do_mysql.py
import pymysql
from class_0419.common.my_config import config

class DoMysql:
    def __init__(self):
        host=config.get("database","host")
        user=config.get("database","user")
        password=config.get("database","password")
        self.mysql=pymysql.connect(host=host,user=user,password=password)
        self.cursor=self.mysql.cursor()
    def fetch_One(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetch_All(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    sql="select max(mobilephone) from future.member"
    mysql=DoMysql()
    s=mysql.fetch_All(sql)
    print(s)
    mysql.close()



