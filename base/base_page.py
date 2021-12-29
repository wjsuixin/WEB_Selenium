# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/6 16:47
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
import os
from base.logger import Logger
from until.my_yaml import read_yaml

# 创建一个日志实例
logger = Logger(logger="BasePage").getlog()
 
class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
    """
    def __init__(self):
        self.driver =webdriver.Chrome()
        #self.driver=driver
        self.driver.maximize_window()

    def open_url(self,url):
        """
        打开网页
        """
        try:
            if "https://" not in url:
                url="https://"+url
            self.driver.get(url)
            logger.info(f"打开网页：'{url}'成功。")
        except Exception as e:
            logger.error(f"打开网页：'{url}'失败，请检查！错误信息：'{e}'")
            self.get_screen_shot()

    def quit(self):
        """
        关闭浏览器
        """
        try:
            self.driver.quit()
            logger.info(f"关闭浏览器成功。")
        except Exception as e:
            logger.error(f"关闭浏览器失败，错误信息：'{e}'")

    def handle_browser(self,key):
        """
        操作浏览器
        """
        if key=="F5":
            self.driver.refresh()
            logger.info("页面刷新成功。")
        elif key=="back":
            self.driver.back()
            logger.info("浏览器后退成功。")
        elif key=="forward":
            self.driver.forward()
            logger.info("浏览器前进成功。")
        else:
            logger.error(f"该'{key}'无对应操作，请检查！")

    def element_wait(self,info,seconds=10):
        """
        显示等待
        """
        if read_yaml.split(info)!=None:
            type,value=read_yaml.split(info)[0],read_yaml.split(info)[1]
            try:
                if type.upper()=="ID":
                    #WebDriverWait(self.driver,seconds,0.5).until(EC.visibility_of_element_located((By.ID,value)))
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.ID,value)))
                elif type.upper()=="NAME":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.NAME,value)))
                elif type.upper()=="XPATH":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.XPATH,value)))
                elif type.upper()=="TAG_NAME":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.TAG_NAME,value)))
                elif type.upper()=="CLASS":
                    #WebDriverWait(self.driver,seconds,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,value)))
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,value)))
                elif type.upper()=="PARTIAL_LINK_TEXT":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,value)))
                elif type.upper()=="LINK_TEXT":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,value)))
                elif type.upper()=="CSS_SELECTOR":
                    WebDriverWait(self.driver,seconds,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,value)))
                else:
                   return False,logger.error(f"元素'{info}'定位类型:'{read_yaml.split(info)[0]}'错误,请检查录入数据！")
                return True,logger.info(f"元素'{read_yaml.split(info)[1]}'等待出现成功。")
            except:
                return False,logger.error(f"元素'{read_yaml.split(info)[1]}'等待出现失败。")

    def get_element(self,info):
        """
        获取单个元素
        """
        if read_yaml.split(info)!=None:
            type,value=read_yaml.split(info)
            element=None
            try:
                if type.upper() == "ID":
                    self.element_wait(info)
                    element=self.driver.find_element(By.ID,value)
                elif type.upper() == "NAME":
                    self.element_wait(info)
                    element=self.driver.find_element(By.NAME,value)
                elif type.upper() == "XPATH":
                    self.element_wait(info)
                    element=self.driver.find_element(By.XPATH, value)
                elif type.upper() == "CLASS":
                    self.element_wait(info)
                    element=self.driver.find_element(By.CLASS_NAME, value)
                elif type.upper() == "TAG_NAME":
                    self.element_wait(info)
                    element=self.driver.find_element(By.TAG_NAME, value)
                elif type.upper() == "PARTIAL_LINK_TEXT":
                    self.element_wait(info)
                    element=self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
                elif type.upper() == "LINK_TEXT":
                    self.element_wait(info)
                    element=self.driver.find_element(By.LINK_TEXT, value)
                else:
                    self.element_wait(info)
                    element=self.driver.find_element(By.CSS_SELECTOR, value)
                logger.info(f"元素'{read_yaml.split(info)[1]}'获取成功。")
            except:
                logger.error(f"元素'{read_yaml.split(info)[1]}'获取失败。")
                self.get_screen_shot()
            return element

    def get_elements(self,info):
        """
        获取元素列表
        """
        if read_yaml.split(info)!=None:
            type,value=read_yaml.split(info)
            elements=None
            try:
                if type.upper() == "ID":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.ID,value)
                elif type.upper() == "NAME":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.NAME,value)
                elif type.upper() == "XPATH":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.XPATH, value)
                elif type.upper() == "CLASS":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.CLASS_NAME, value)
                elif type.upper() == "TAG_NAME":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.TAG_NAME, value)
                elif type.upper() == "PARTIAL_LINK_TEXT":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.PARTIAL_LINK_TEXT, value)
                elif type.upper() == "LINK_TEXT":
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.LINK_TEXT, value)
                else:
                    self.element_wait(info)
                    elements=self.driver.find_elements(By.CSS_SELECTOR, value)
                logger.info(f"元素'{read_yaml.split(info)[1]}'获取成功。")
            except:
                self.get_screen_shot()
                logger.error(f"元素'{read_yaml.split(info)[1]}'获取失败。")
            return elements

    def get_list_element(self,info,info_node,index=None):
        """
        层级定位获取到元素,先获取到元素info,再定位子元素info_node
        """
        if index == None:
            element = self.get_element(info[0])
        else:
            element = self.get_elements(info[0])[index]
        if element!=None:
            if read_yaml.split(info_node) != None:
                type, value = read_yaml.split(info_node)
                try:
                    if type.upper() == "ID":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.ID, value)
                    elif type.upper() == "NAME":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.NAME, value)
                    elif type.upper() == "XPATH":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.XPATH, value)
                    elif type.upper() == "CLASS":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.CLASS_NAME, value)
                    elif type.upper() == "TAG_NAME":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.TAG_NAME, value)
                    elif type.upper() == "PARTIAL_LINK_TEXT":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.PARTIAL_LINK_TEXT, value)
                    elif type.upper() == "LINK_TEXT":
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.LINK_TEXT, value)
                    else:
                        self.element_wait(info_node)
                        logger.info(f"子元素'{read_yaml.split(info_node)[1]}'获取成功。")
                        return element.find_element(By.CSS_SELECTOR, value)
                except:
                    logger.error(f"子元素'{read_yaml.split(info_node)[1]}'获取失败。")
                    self.get_screen_shot()

    def click_element(self,*args,**kwargs):
        """
        点击元素
        """
        if len(args)==1:
            if kwargs.get("index")==None:
                element=self.get_element(args[0])
            else:
                element=self.get_elements(args[0])[kwargs.get("index")]
            if element != None:
                try:
                    element.click()
                    logger.info(f"元素'{read_yaml.split(args[0])[1]}'点击成功。")
                except Exception as e:
                    logger.error(f"元素'{read_yaml.split(args[0])[1]}'点击失败，错误信息：'{e}'")
                    self.get_screen_shot()
            else:
                return False
        else:
            element=self.get_list_element(args[0],args[1])
            if element!=None:
                try:
                    element.click()
                    logger.info(f"元素'{read_yaml.split(args[1])[1]}'点击成功。")
                except Exception as e:
                    logger.error(f"元素'{read_yaml.split(args[1])[1]}'点击失败，错误信息：'{e}'")
                    self.get_screen_shot()
            else:
                return False

    def send_text(self,value,*args):
        """
        元素进行输入操作
        """
        if len(args) == 1:
            element = self.get_element(args[0])
            if element != None:
                try:
                    element.send_keys(value)
                    logger.info(f"元素'{read_yaml.split(args[0])[1]}'输入'{value}'成功。")
                except Exception as e:
                    logger.error(f"元素'{read_yaml.split(args[0])[1]}'输入'{value}'失败，错误信息：'{e}'")
                    self.get_screen_shot()
            else:
                return False
        else:
            element = self.get_list_element(args[0],args[1])
            if element != None:
                try:
                    element.send_keys(value)
                    logger.info(f"元素'{read_yaml.split(args[1])[1]}'输入'{value}'成功。")
                except Exception as e:
                    logger.error(f"元素'{read_yaml.split(args[1])[1]}'输入'{value}'失败，错误信息：'{e}'")
                    self.get_screen_shot()
            else:
                return False

    def get_screen_shot(self):
        """
        截图操作，并保存到screenshots文件下
        """
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(f"截图成功，图片保存路径：'{screen_name}'")
        except Exception as e:
            logger.error(f"截图失败，错误信息：'{e}'")

    def get_text(self,info,type=None):
        """
        获取元素对应的文本
        """
        element=self.get_element(info)
        if element!=None:
            try:
                if type==None:
                    text=element.text
                else:
                    text=element.get_attribute(type)
                logger.info(f"获取到元素'{read_yaml.split(info)[1]}'的text值为：'{text}'")
                return text
            except Exception as e:
                logger.error(f"获取元素'{read_yaml.split(info)[1]}'的text值失败，错误信息：'{e}'")
        else:
            return False

    def switch_to_alter(self,info=None,text=None):
        """
        系统弹窗的操作
        """
        try:
            if info==None and text==None:
                self.driver.switch_to_alert().accept()
                logger.info("已关闭系统弹窗")
            elif info==None and text!=None:
                self.driver.switch_to_alert().send_keys(text)
                self.driver.switch_to_alert().accept()
                logger.info(f"在输入框中输入内容：'{text}'后关闭系统弹窗")
            else:
                self.driver.switch_to_alert().dismiss()
                logger.info(f"系统弹窗已点击取消按钮。")
        except Exception as e:
            self.get_screen_shot()
            logger.error(f"系统弹窗操作异常，错误信息：'{e}'")

    def assert_title(self,title_name):
        """
        判断title是否正确
        """
        if title_name!=None:
            get_title=EC.title_contains(title_name)
            return get_title(self.driver) #返回的是bool值
        else:
            logger.error(f"未传递'{title_name}'，无法断言。")

    def switch_to_window(self,title_name):
        """
        切换窗口
        """
        current_window=self.driver.current_window_handle
        handles=self.driver.window_handles
        try:
            for i in handles:
                if i!=current_window:
                    self.driver.switch_to_window(i)
                    if self.assert_title(title_name):
                        break
                    logger.info(f"已切换到title为'{title_name}'的窗口。")
        except Exception as e:
            logger.error(f"切换到title为'{title_name}'的窗口失败，错误信息:'{e}'")

    def switch_to_iframe(self,info=None):
        """
        iframe的切换操作
        """
        try:
            if info!=None:
                self.driver.switch_to_frame(info)
                logger.info(f"已成功切换到元素为'{read_yaml.split(info)[1]}'iframe层。")
            else:
                self.driver.switch_to_default_content()
                logger.info(f"已成功切换出元素为'{read_yaml.split(info)[1]}'iframe层。")
        except Exception as e:
            logger.error(f"切换frame操作失败，错误信息：'{e}'")

    def clear_data(self,info):
        """
        清除数据
        """
        element=self.get_element(info)
        if element!=None:
            try:
                element.clear()
                logger.info(f"清除元素'{read_yaml.split(info)[1]}'原有的数据成功。")
            except Exception as e:
                logger.error(f"清除元素'{read_yaml.split(info)[1]}'原有的数据失败，错误信息：'{e}'。")
        else:
            return False

    def move_element(self,info,sloc):
        """
        鼠标悬停到某个元素后，再点击下一个元素
        """
        mouse=self.get_element(info)
        if mouse!=None:
            try:
                ActionChains(self.driver).move_to_element(mouse).perform()
                logger.info(f"鼠标悬停到元素'{read_yaml.split(info)[1]}'成功。")
                self.click_element(sloc)
            except Exception as e:
                logger.error(f"鼠标悬停到元素'{info}'失败，错误信息：'{e}'")
                self.get_screen_shot()

    def keybord_file_upload(self,file):
        """
        上传非input标签的文件
        """
        pykey=PyKeyboard()
        pykey.tap_key(pykey.shift_key)
        self.sleep(2)
        pykey.type_string(file)
        self.sleep(2)
        pykey.tap_key(pykey.enter_key)
        pykey.tap_key(pykey.enter_key)

    def js_excute(self,js):
        """
        执行js代码
        """
        try:
           return self.driver.execute_script(js),logger.info(f"执行js='{js}'成功。")
        except Exception as e:
            return False,logger.error(f"执行js='{js}'失败，错误提示：'{e}'")

    def scroll_window(self,height=None):
        """
        滑动滚动条操作
        """
        if height==None:
            self.js_excute("var q=document.documentElement.scrollTop=10000")
            logger.info("滑动滚动条到底部完成。")
        else:
            self.js_excute("var q=document.documentElement.scrollTop=0")
            logger.info("滑动滚动条到顶部完成。")

    def scroll_window_getElement(self,info):
        """
        滑动查找元素
        """
        element=self.get_element(info)
        if element!=None:
            return self.js_excute("arguments[0].scrollIntoView(false);",element)
        else:
            return False

    @staticmethod
    def sleep(seconds):
        """
        强制等待
        """
        time.sleep(seconds)
        logger.info(f"强制等待'{seconds}'秒。")




