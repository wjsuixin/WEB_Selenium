# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/22 13:51
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from base.base_page import BasePage
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
# 搜索 selenium
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
# 等待元素可见
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='selenium滑动页面的滚动条']")))
# 1.先找到元素
#element = driver.find_element_by_xpath('//*[@id="5"]/h3/a')
element = driver.find_element_by_xpath("//a[@title='selenium滑动页面的滚动条']")

# 2.利用js将元素拖动到可见区域
driver.execute_script("arguments[0].scrollIntoView(false);", element)  # 可见元素与页面“底端”对齐
"""
class JsTest(BasePage):

    def js_test1(self):
        self.open_url("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        self.scroll_window_getElement("snns")
if __name__ == '__main__':
    jst=JsTest()
    jst.js_test1()