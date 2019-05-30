# -*- coding:utf-8 -*-
# @Time  : 2019/4/13 23:42
# @Author: xiaoxiao
# @File  : http_requests.py
import requests
import json
class context:
    token=None
class http_requests:
    def method(self,method,url,params=None,token=None):
        headers={"token":token }
        if type(params)==str:
            params=json.loads(params)
        if method.upper()=="GET":
            resp=requests.get(url,params=params,headers=headers)
            return resp
        elif method.upper()=="POST":
            resp=requests.post(url,data=params,headers=headers)
            return resp
        else:
            print("只支持get和post请求")

if __name__ == '__main__':
    url="http://api.admin.lbd.magicodetech.com/login"
    params={"account":"admin","password":"123456"}

    s=http_requests()
    resp=s.method("post",url,params,token=getattr(context,"token"))
    print(resp.json())
    print(resp.text)
    print(resp)
    print(resp.headers["token"])
    setattr(context,"token",resp.headers["token"])

    url="http://api.admin.lbd.magicodetech.com/regions"
    resp=s.method("get",url,token=getattr(context,"token"))
    print(type(resp.json()))







