from selenium import webdriver
from base.logger import Logger
from until.read_ini import ReadIni
import unittest
logger = Logger(logger="TestBase").getlog()

class TestBase(unittest.TestCase,ReadIni):
    def setUp(self):
        logger.info("开始执行测试。")
        browser_type=self.get_ini_data("browser_type","browser")
        if browser_type.upper()=="CHROME":
            self.driver=webdriver.Chrome()
        elif browser_type.upper()=="FIREFOX":
            self.driver = webdriver.Firefox()
        else:
            logger.error("没有该浏览器类型配置，请检查！")
        self.driver.implicitly_wait(10)  #设置隐式等待
        self.driver.maximize_window()    #最大化浏览器

    def tearDown(self):
        self.driver.quit()
        logger.info("结束测试并关闭浏览器。")
 
if __name__=='__main__':
    unittest.main()