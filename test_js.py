# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/21 17:34
from base.base_page import BasePage
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
'''
driver.get("http://www.baidu.com")
driver.execute_script('document.getElementById("kw").value="selenium"')
print(driver.execute_script('return document.getElementById("kw").value'))
print(driver.execute_script('return document.title;'))
driver.execute_script('document.getElementById("su").click()')


driver.get("https://www.12306.cn/index/")
#取消readonly属性
driver.execute_script("dat=document.getElementById('train_date'); dat.removeAttribute('readonly')")
driver.execute_script("document.getElementById('train_date').value='2020-10-01'")
time.sleep(3)
now_time = driver.execute_script("return document.getElementById('train_date').value")
print(now_time)
assert '2020-10-01' == now_time
'''
class JsTest(BasePage):

    def js_test1(self):
        self.open_url("https://www.12306.cn/index/")
        self.js_excute("dat=document.getElementById('train_date'); dat.removeAttribute('readonly')")
        self.js_excute("document.getElementById('train_date').value='2020-10-01'")
        self.sleep(2)
        now_time=self.js_excute("return document.getElementById('train_date').value")
        assert now_time[0]=="2020-10-01"
