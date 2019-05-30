# -*- coding:utf-8 -*-
# @Time  : 2019/4/22 3:17
# @Author: xiaoxiao
# @File  : regulax.py

import re
from class_0419.common.my_config import config
def Regulax(data,p=None):
    if not p:
        p="#(.*?)#"
    while re.search(p,data):
        result=re.search(p,data).group(1)
        params=config.get("member",result)
        data=re.sub(p,params,data,count=1)
    return data


