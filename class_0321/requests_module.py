# -*- coding:utf-8 -*-
# @Time  : 2019/3/12 22:05
# @Author: xiaoxiao
# @File  : post.py

import requests

class submit_method:
    def __init__(self,method,url,params=None):
        self.method=method
        self.url=url
        self.params=params
    def http_request(self):
        if self.method.lower()=="post":
            req=requests.post(self.url,data=self.params)
        elif self.method.lower()=="get":
            req=requests.get(self.url,params=self.params)
        return req

if __name__ == '__main__':
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    params={"mobilephone":"186887734671" ,"pwd":""}

    result_G=submit_method("get",url,params)
    print("get的响应头：",result_G.http_request().headers)
    print("get的响应状态码：",result_G.http_request().status_code)
    print("get的响应报文：",result_G.http_request().text)
    result_P=submit_method("post", url, params)
    print("post的响应头：", result_P.http_request().headers)
    print("post的响应状态码：", result_P.http_request().status_code)
    print("post的响应报文：", result_P.http_request().text)


