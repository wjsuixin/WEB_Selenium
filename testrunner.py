#encoding='utf-8'
import unittest
#from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import  BeautifulReport
import time
import os
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


current_time=time.strftime("%Y%m%d%H%M%S")
report_path=os.path.join(os.path.dirname(__file__),"report")
file_name="研学ERP_UI自动化测试_"+str(current_time)
discover=unittest.defaultTestLoader.discover(start_dir=os.path.dirname(__file__)+r"\testsuites",pattern="test_*.py")
BeautifulReport(discover).report(description="研学ERP系统自动化测试",filename=file_name,report_dir=report_path)

