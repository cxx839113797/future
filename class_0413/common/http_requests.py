# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 17:08
# @Author: xiaoxiao
# @File  : http_requests.py


import requests

# params1={"mobilephone":"18680073467" ,"pwd":"123456"}
# session=requests.session()
# resp=session.request("get","http://test.lemonban.com/futureloan/mvc/api/member/login",params1)
# print(resp.cookies)
#
# url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# params2 = {"mobilephone":"13542892623" ,"amount":"1"}
# resp=session.request("post",url,params2)
# print(resp.text)
# session.close()
import json

class http_requests:
    def __init__(self):
        self.session=requests.session()
    def Session(self,method,url,params=None):
        if type(params)==str:
            params=json.loads(params)
        if method.upper() == "GET" or "POST":
            method=method.upper()
            resp = self.session.request(method, url, params)
        return resp
    def close(self):
        self.session.close()

if __name__ == '__main__':

    #注册接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    params={"mobilephone":"18685620265" ,"pwd":"12345678901234"}
    register=http_requests()
    print("get的响应头：",register.Session("get",url,params).headers)
    print("get的响应状态码：",register.Session("get",url,params).status_code)
    print("get的响应报文：", register.Session("get",url,params).text)

    #登录接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    params={"mobilephone":"18680073467" ,"pwd":"123456"}
    login=http_requests()
    login.Session("post",url,params)


    #充值接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    params = {"mobilephone":"18685620265" ,"amount":"100000"}
    print("充值的响应头：", login.Session("get",url,params).headers)
    print("充值的响应状态码：", login.Session("get",url,params).status_code)
    print("充值的响应报文：", login.Session("get",url,params).text)
    # #
    # #获取用户列表
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/list"
    # print("get的响应头：", login.Session("get", url).headers)
    # print("get的响应状态码：",login.Session("get", url).status_code)
    # print("get的响应报文：", login.Session("get", url).json())

    #新增标的
    # url = "http://test.lemonban.com/futureloan/mvc/api/loan/add"
    # params={"memberId":"558","title":"借款100万","amount":-1,"loanRate":1.0,
    #         "loanTerm":6,"loanDateType":0,"repaymentWay":4,"biddingDays":9}
    # s=login.Session("post",url,params)
    # print("get的响应报文：", s.text)

    # url = "http://test.lemonban.com/futureloan/mvc/api/loan/audit"
    # params = {"id":123, "status":7}
    # s = login.Session("post", url, params)
    # print("get的响应报文：", s.text)

    url = "http://test.lemonban.com/futureloan/mvc/api/loan/bidLoan"
    params = {"memberId": 558, "password": "123456", "loanId": 93, "amount": 1500000}
    s = login.Session("post", url, params)
    print(s.status_code)
    print("get的响应报文：", s.text)

