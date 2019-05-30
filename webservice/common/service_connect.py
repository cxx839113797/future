# -*- coding:utf-8 -*-
# @Time  : 2019/5/5 2:15
# @Author: xiaoxiao
# @File  : service_connect.py

from suds.client import Client

def WebService(url,t):
    webservice= Client(url)
    print(type(webservice))
    result = webservice.service.sendMCode(t)
    print(result)


import pymysql
import time

class DoMysql:
    def __init__(self):
        self.mysql=pymysql.connect(host="120.24.235.105",user="python",password="python666",port=3306)
        self.cursor=self.mysql.cursor(cursor=pymysql.cursors.DictCursor)
    def fetchOne(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
    def fetchAll(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.mysql.close()


#
#
# url="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
# t={"client_ip":"1","tmpl_id":"1","mobile":"18999633653"}
# WebService(url,t)
# mysql=DoMysql()
# sql="select Fverify_code from sms_db_53.t_mvcode_info_6 where Fmobile_no=18999633653"
# s=mysql.fetchOne(sql)["Fverify_code"]
# mysql.close()
url="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
t={"verify_code":"854236","user_id":"45682","channel_id":"3","pwd":"123456","mobile":"17618542653","ip":"172.126.1.2"}

webservice= Client(url)

print(webservice)
#
# url="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
# t={"uid":"123457","true_name":"嘻嘻","cre_id":"440582199508113087"}
# webservice=Client(url)
# result=webservice.service.verifyUserAuth(t)
# print(result)

# import time
# #获得当前时间时间戳
# now = int(time.time())
# #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
# timeStruct = time.localtime(now)
# strTime = time.strftime("%Y%m%d", timeStruct)
# strTime=int(strTime)-200000
# birth_time=str(strTime)
# print(strTime)


{"uid":"#uid#","pay_pwd":"123456","mobile":"$(mobile)","cre_id":"#cre_id#",
 "user_name":"#true_name#","cardid":"6217003090003112001","bank_type":"1001","bank_name":"建设银行"
 ,"bank_area":"广东省","bank_city":"深圳"}





