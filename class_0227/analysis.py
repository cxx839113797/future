# -*- coding:utf-8 -*-
# @Time  : 2019/2/27 0:52
# @Author: xiaoxiao
# @File  : analysis.py

import re

def analysis(str):
    L=["","","",""]
    l = []
    n1=''
    c1=''
    e1=''
    s1=''
    s=str.replace(" ","")
    for i in range(len(s)):
        if re.match(r"[0-9]",s[i]):
            if i == len(s) - 1:
                L[0]+=n1+s[i]
                break
            else:
                n1 += s[i]
            if not re.match(r"[0-9]",s[i+1]):
                L[0]+=n1+'、'
                n1 = ''
                continue
        if re.match(r"[\u4e00-\u9fa5]",s[i]):
            # s[i]<=u'\u9fff'and s[i]>=u'\u4e00':
            if i == len(s) - 1:
                L[1] += c1 + s[i]
                break
            else:
                c1 += s[i]
            if not re.match(r"[\u4e00-\u9fa5]",s[i+1]):
                # s[i+1]>u'\u9fff'or s[i+1]<u'\u4e00':
                L[1] += c1 + '、'
                c1=''
                continue
        if re.match(r"[a-z|A-Z]",s[i]):
            if i == len(s) - 1:
                L[2] += e1+s[i]
                break
            else:
                e1 += s[i]
            if not re.match(r"[a-z|A-Z]",s[i+1]):
                L[2] += e1 + '、'
                e1=''
                continue
        if not s[i].isalnum():
            if i == len(s) - 1:
                L[3] += s1+s[i]
                break
            else:
                s1 += s[i]
            if s[i+1].isalnum():
                L[3] += s1
                s1=''
    for i in L:
        l.append(i.strip("、"))
    print("语法分析后得到结果如下： ")
    print("数字:",l[0])
    print("中文:", l[1])
    print("拼音:", l[2])
    print("符号:", l[3])
s="我的名字叫xiaoxiao，今年18岁。"
analysis(s)
