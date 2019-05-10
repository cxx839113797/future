# -*- coding:utf-8 -*-
# @Time  : 2019/4/15 17:08
# @Author: xiaoxiao
# @File  : http_requests.py


import requests
import json
from class_0423.common.my_config import config
from class_0423.common.log_config import log_config



class http_requests:
    def __init__(self):
        self.session=requests.session()
    def Session(self,method,url,params=None):
        url=config.get("api","pre_url")+url
        if type(params)==str:
            params=json.loads(params)
        if method.upper() == "GET" or "POST":
            method=method.upper()
            resp = self.session.request(method, url, params)
        return resp
    def close(self):
        self.session.close()



