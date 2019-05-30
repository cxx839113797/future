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
    def http_request(self,cookies=None):
        if self.method.lower()=="post":
            req=requests.post(self.url,data=self.params,cookies=cookies)
        elif self.method.lower()=="get":
            req=requests.get(self.url,params=self.params,cookies=cookies)
        return req

if __name__ == '__main__':

    #注册接口
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    # params={"mobilephone":"18685621588" ,"pwd":"123456789012345678"}
    # register=submit_method("get",url,params)
    # print("get的响应头：",register.http_request().headers)
    # print("get的响应状态码：",register.http_request().status_code)
    # print("get的响应报文：", register.http_request().text)

    #登录接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    params={"mobilephone":"18680073467" ,"pwd":"123456"}
    login=submit_method("get",url,params)
    print("get的响应头：",login.http_request().headers)
    print("get的响应状态码：",login.http_request().status_code)
    print("get的响应报文：",login.http_request().text)
    cookies=login.http_request().cookies

    #充值接口
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    # params = {"mobilephone":"18680073467" ,"amount":"100"}
    # recharge=submit_method("get",url,params)
    # print("充值的响应头：", recharge.http_request(cookies).headers)
    # print("充值的响应状态码：", recharge.http_request(cookies).status_code)
    # print("充值的响应报文：", recharge.http_request(cookies).text)
    # #
    # #获取用户列表
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/list"
    # login = submit_method("get", url)
    # print("get的响应头：", login.http_request(cookies).headers)
    # print("get的响应状态码：", login.http_request(cookies).status_code)
    # print("get的响应报文：", login.http_request(cookies).json())

    #新增标的
    url = "http://test.lemonban.com/futureloan/mvc/api/loan/add"
    params={"memberId":"558","title":"借款100万","amount":"100000.00","loanRate":"1.0",
            "loanTerm":"6","loanDateType":"0","repaymentWay":"4","biddingDays":"9"}
    add=submit_method("get",url,params)
    print("get的响应报文：", add.http_request(cookies).text)








