#encoding='utf-8'
import unittest
#from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import  BeautifulReport
from base.email_psot import SendEmail
import time
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
"""
# 定义输出的文件位置和名字
DIR = os.path.dirname(os.path.abspath(__file__))
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
print(DIR)
print(now)
 
filename =now+"report.html"
print(filename)
#discover方法执行测试套件
testsuite = unittest.defaultTestLoader.discover(
   start_dir='./testsuites',
   pattern='*case.py',
   top_level_dir=None
   )
 
with open(DIR+'/test_report/'+filename,'wb') as f:
    runner = HTMLTestRunner(
       stream=f,
       verbosity=2, 
       title='gateway UI report',
       description='执行情况'
   )
    runner.run(testsuite)
"""

class RunMain(SendEmail):
    def run_main(self):
        current_time=time.strftime("%Y%m%d%H%M%S")
        report_path=os.path.join(os.path.dirname(__file__),"report")
        file_name="研学ERP_UI自动化测试_"+str(current_time)
        discover=unittest.defaultTestLoader.discover(start_dir=os.path.dirname(__file__)+r"\testsuites",pattern="test_*.py")
        BeautifulReport(discover).report(description="研学ERP系统自动化测试",filename=file_name,report_dir=report_path)
        #查找最新生成的测试报告地址
        new_report_addr =self.acquire_report_address(report_path)
        print(new_report_addr)
        #自动发送邮件
        self.send_email(new_report_addr)

if __name__ == '__main__':
    run=RunMain()
    run.run_main()

