# -*- coding:utf-8 -*-
# @Time  : 2019/5/11 15:06
# @Author: xiaoxiao
# @File  : class_0511.py

# import re
# def analysis(str):
#     d={}
#     str=str.replace(" ","")
#     p1="[\u4e00-\u9fa5]*"
#     chinese=re.findall(p1, str)
#     d["中文"]=chinese
#     p2="[1-9]\d*|0"
#     digits=re.findall(p2,str)
#     d["数字"] = digits
#     p3="[A-Za-z]*"
#     english=re.findall(p3,str)
#     d["拼音"] = english
#     p4="[^a-zA-Z0-9\u4e00-\u9fa5]"
#     punctuation=re.findall(p4,str)
#     d["符号"] = punctuation
#     for key in d:
#         value = ""
#         for column in d[key]:
#             if column:
#                 value+=column+" "
#         d[key]=value
#     print("搜索引擎分析'{}'".format(str))
#     print("数字：",d["数字"])
#     print("中文：", d["中文"])
#     print("拼音：", d["拼音"])
#     print("符号：", d["符号"])
# def star(n):
#     if n>1:
#         column=int(n/2)
#         if n%2==0:
#             for i in range(column):
#                 print(" "*(column-i-1),end="")
#                 print("*" * (2 * i + 1))
#         else:
#             for i in range(column):
#                 print(" "*(column-i),end="")
#                 print("*" * (2 * i + 1))
#         for j in range(n-column):
#             print(" "*j,end="")
#             print("*"*(2*(n-column-j-1)+1))
# import json
# # def json_to_dict(data):
# #     while len(re.findall(".{.*?:.*?}",str(data)))>0:
# #         result = {}
# #         for key,value in data.items():
# #             if type(value)==str:
# #                 try:
# #                     if json.loads(value)==dict:
# #                         value = json.loads(value)
# #                         for k, v in value.items():
# #                             result[k] = v
# #                 except json.decoder.JSONDecodeError:
# #                     result[key] = value
# #             elif type(value)==int:
# #                 result[key]=value
# #             elif type(value)==dict:
# #                 for k,v in value.items():
# #                     result[k]=v
# #             elif type(value) == list:
# #                 l=[]
# #                 for item in value:
# #                     if type(item)==dict:
# #                         for k,v in item.items():
# #                             result[k]=v
# #                     elif type(item)==str and type(json.loads(item))==dict:
# #                         for k,v in json.loads(item).items():
# #                             result[k]=v
# #                     elif type(item)==list:
# #                         l.extend(item)
# #                         result[key]=l
# #         data=result
#
# def json_to_dict(data):
#         result = {}
#         isDict = False
#         for key,value in data.items():
#             if type(value)==str:
#                 result[key] = value
#             elif type(value)==int:
#                 result[key]=value
#             elif type(value)==dict:
#                 for k,v in value.items():
#                     result[k]=v
#                 isDict = True
#             elif type(value) == list:
#                 value=open(value)
#                 for item in value:
#                     result.update(json_to_dict(item))
#                 isDict = True
#         if isDict==True:
#             return json_to_dict(result)
#         else:
#             return result
# def open(l):
#     isList = False
#     for item in l:
#         if isinstance(item,str):
#             dict=json.loads(item)
#             l.append(dict)
#             l.remove(item)
#         if isinstance(item,list):
#             l.extend(item)
#             l.remove(item)
#             isList=True
#     if isList==True:
#         open(l)
#     else:
#         return l

def f(n):
    if 1<=n<=2:
        return n-1
    if n>2:
        return (n-1)*(f(n-1)+f(n-2))
if __name__ == '__main__':
    # print("n=5")
    # star(5)
    # print("n=6")
    # star(6)
    # data={"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
    # print(json_to_dict(data))
    # str = "我的名字是ha,今年20岁。"
    # analysis(str)
    print(f(4))























