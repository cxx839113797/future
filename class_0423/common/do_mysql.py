# -*- coding:utf-8 -*-
# @Time  : 2019/4/21 19:23
# @Author: xiaoxiao
# @File  : do_mysql.py
import pymysql
from class_0423.common.my_config import config

class DoMysql:
    def __init__(self):
        host=config.get("database","host")
        user=config.get("database","user")
        password=config.get("database","password")
        self.mysql=pymysql.connect(host=host,user=user,password=password)
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)
    def fetch_One(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
    def fetch_All(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    mobilephone = 13600000000
    mysql=DoMysql()
    s=mysql.fetch_One("SELECT leaveamount FROM future.member WHERE id=1303")
    print(s)

    mysql.close()



