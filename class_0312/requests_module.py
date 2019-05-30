# -*- coding:utf-8 -*-
# @Time  : 2019/3/12 22:05
# @Author: xiaoxiao
# @File  : post.py

import requests

class submit_method:
    def __init__(self,method,url,params=None,cookie=None):
        self.method=method
        self.url=url
        self.params=params
    def http_request(self,cookies=None):
        if self.method.lower()=="post":
            req=requests.post(self.url,data=self.params,cookies=cookies)
        elif self.method.lower()=="get":
            req=requests.get(self.url,params=self.params,cookies=cookies)
        return req

if __name__ == '__main__':
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    params={"mobilephone":"18688773467" ,"pwd":"123456"}

    result_G=submit_method("get",url,params)
    # print("get的响应头：",result_G.http_request().headers)
    # print("get的响应状态码：",result_G.http_request().status_code)
    print("get的响应报文：",result_G.http_request().cookies)
    # result_P=submit_method("post", url, params)
    # print("post的响应头：", result_P.http_request().headers)
    # print("post的响应状态码：", result_P.http_request().status_code)
    # print("post的响应报文：", result_P.http_request().text)


