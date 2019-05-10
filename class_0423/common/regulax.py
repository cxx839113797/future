# -*- coding:utf-8 -*-
# @Time  : 2019/4/22 3:17
# @Author: xiaoxiao
# @File  : regulax.py

import re
import configparser
from class_0423.common.my_config import config
from class_0423.common.log_config import log_config
log=log_config(__name__)

class Regulax:
    loanId=None

def regulax(data,p="#(.*?)#"):
    while re.search(p,data):
        result=re.search(p,data).group(1)
        try:
            params=config.get("member",result)
        except configparser.NoOptionError as e:
            if hasattr(Regulax,result):
                params=getattr(Regulax,result)
            else:
                print("找不到参数",result)
                log.error("报错：{}".format(e))
                raise e
        data = re.sub(p, params, data, count=1)
    return data




