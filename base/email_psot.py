# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/3 15:12
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('Hello Boy!')   # 邮件内容
message['From'] = Header('小爱')   # 邮件发送者名字
message['To'] = Header('小南zhao')   # 邮件接收者名字
message['Subject'] = Header('来自异世界的一封信!')   # 邮件主题

mail = smtplib.SMTP()
mail.connect("smtp.qq.com")   # 连接 qq 邮箱
mail.login("763462254@qq.com", "kamodwrvmpgvbbcd")   # 账号和授权码
mail.sendmail("763462254@qq.com", ["jiang.wu@weihongtech.cn"], message.as_string())   # 发送账号、接收账号和邮件信息
"""

import os
import unittest
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import time

#自动发送邮件
def send_email(new_report):
    #读取测试报告中的内容作为邮件的内容
    with open(new_report,'r',encoding='utf8') as f:
        mail_body = f.read()
    #发件人地址
    from_addr = '123456789@126.com'
    #收件人地址
    to_addr = '123456@qq.com,'
    #发送邮箱的服务器地址
    mail_server = 'smtp.126.com'
    #邮件的标题
    subject = 'qq登录测试报告'
    #发件人的邮箱地址
    username = '123456789@126.com'
    password = '123456'
    #邮箱的内容和标题
    message = MIMEText(mail_body,'html','utf8')
    message['Subject'] = Header(subject,charset='utf8')
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(username,password)
    smtp.sendmail(from_addr,to_addr.split(','),message.as_string())
    smtp.quit()

#获取最新报告的地址
def acquire_report_address(reports_address):
    #测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    #按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    #获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    #最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address,the_last_report)
    return the_last_report_address


if __name__ == '__main__':
    # 生成测试报告并发送邮件
    #测试报告文件夹地址
    test_reports_address = 'F:\\python_selenium\\soft_test_selenium2.0\\test_report'
    #测试用例的文件夹地址
    test_cases_dir = r'F:\python_selenium\soft_test_selenium2.0\test_cases'
    #获取所有的测试用例
    test_cases = unittest.defaultTestLoader.discover(test_cases_dir,pattern='*.py')
    #获取当前时间
    now = datetime.now().strftime('%Y%m%d%H%MM%f')
    #生成以当前时间命名的测试报告文件名
    test_report_name = r'{}\report_{}.html'.format(test_reports_address,datetime.now().strftime('%Y%m%d%H%M%f'))
    #生成以当前时间命名的测试报告文件
    file_report = open(test_report_name,'w',encoding='utf8')
    #生成html形式的报告
    runner = HTMLTestRunner(stream=file_report,title='测试报告',description='QQ登录测试报告结果：')
    #运行
    runner.run(test_cases)
    #关闭打开的测试报告文件
    file_report.close()

    time.sleep(5)
    #查找最新生成的测试报告地址
    new_report_addr = acquire_report_address(test_reports_address)
    #自动发送邮件
    send_email(new_report_addr)