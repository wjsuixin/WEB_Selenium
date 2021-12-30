from selenium import webdriver
from base.logger import Logger
from until.read_ini import ReadIni
import unittest,os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
logger = Logger(logger="TestBase").getlog()

class TestBase(unittest.TestCase):
    def setUp(self):
        logger.info("开始执行测试。")
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)  #设置隐式等待
        self.driver.maximize_window()    #最大化浏览器

    def tearDown(self):
        self.driver.quit()
        logger.info("结束测试并关闭浏览器。")
 
if __name__=='__main__':
    unittest.main()