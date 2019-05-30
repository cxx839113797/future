# -*- coding:utf-8 -*-
# @Time  : 2019/3/29 23:06
# @Author: xiaoxiao
# @File  : send_Email.py

import smtplib #负责发送邮件
import ssl
from class_0329 import qqemail,qqpwd #导入配置的邮件用户名和密码
from email.mime.text import MIMEText #构造邮件
from email.mime.multipart import MIMEMultipart #将正文和附件作为不同部分添加的模块
from email.mime.application import MIMEApplication #邮件附件模块

class sendEmail:
    def __init__(self,addrs,msg,subject=None,host="smtp.qq.com",emailname=qqemail,emailpwd=qqpwd):
        self.toaddrs=addrs
        self.msg=msg
        self.host=host
        self.subject=subject
        self.emailname=emailname
        self.emailpwd=emailpwd
        self.context=ssl.create_default_context()
        self.sever=smtplib.SMTP(self.host,25)#初始化一个邮件服务商
        self.sever.login(self.emailname, self.emailpwd)  # 登录用户名和密码
    #简单发送邮件
    def sendSimple(self):
        self.sever.sendmail(qqemail,self.toaddrs,self.msg)#发送邮件

    #加密模式TLS发送邮件
    def sendTLS(self):
            self.sever.starttls(context=self.context)  # 将邮件设置为加密模式
            self.sever.sendmail(qqemail,self.toaddrs,self.msg)
    #加密模式SSL发送邮件
    def sendSSL(self):
        with smtplib.SMTP_SSL(self.host,465) as sever:#使用SMTP_SSL类，更改成SSL端口465
            sever.login(self.emailname, self.emailpwd)
            sever.sendmail(qqemail,self.toaddrs,self.msg)
    #通过MIME构造邮件的组成部分，邮件正文可以分为text/html或text/plain两种文本方式发送
    def sendMIME(self):
        msg=MIMEText(self.msg,"html")  #创建一个text/html或text/plain的正文文本
        msg["Subject"]=self.subject  #添加subject使subject在邮件中显示
        msg["From"]=qqemail   #添加发件人使发件人在邮件中显示
        msg["To"]=self.toaddrs  #添加收件人使收件人在邮件中显示
        self.sever.sendmail(qqemail,self.toaddrs,msg.as_string())#将msg对象转换为字符串发送
    def sendApplication(self):
        msg=MIMEMultipart() #创建一个多部分对象
        msg["Subject"] = self.subject  # 添加subject使subject在邮件中显示
        msg["From"] = qqemail  # 添加发件人使发件人在邮件中显示
        msg["To"] = self.toaddrs  # 添加收件人使收件人在邮件中显示
        msg_raw= MIMEText(self.msg, "html")
        msg.attach(msg_raw) #添加正文模块
        file=MIMEApplication(open("demo.xlsx","rb").read()) # 将附件保存在一个file文件
        file.add_header("Content-Disposition","attachment",filename="demo.xlsx") #添加附件的头信息
        msg.attach(file) #添加文件作为附件模块
        self.sever.sendmail(qqemail,self.toaddrs,msg.as_string())#发送邮件

    def quit_sever(self):
        self.sever.quit()

# msg = '''\\
# From:xiaoxiao
# Subject:testing
#
# This is a test '''
#
# s=sendEmail("839113797@qq.com",msg)
#
# s.sendSimple()
# s.quit_sever()
#
# s.sendTLS()
# s.quit_sever()
#
# s.sendSSL()
# s.quit_sever()


msg_raw="""<p style="color:red">你好</p>"""

s=sendEmail("839113797@qq.com",msg_raw,"这是我的主题")
#
# s.sendMIME()
# s.quit_sever()

s.sendApplication()
s.quit_sever()

