# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/13 16:54
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from faker import Faker
from base.url_save import *
from pageobjects.login import LoginPage
from base.logger import Logger
# 创建一个日志实例
logger = Logger(logger="JobMange").getlog()

class RoleMange(LoginPage):
    """
    角色管理页面类
    """
    def star_path(self):
        """
        进入角色管理的入口
        """
        self.login("wj@qq.com", "yx1234")
        #点击基础档案菜单
        self.click_element("basic",index=9)
        #点击子菜单角色管理
        self.click_element("basic_jobmange",index=3)

    def new_role(self,name,other_name,select_list):
        """
        新增角色
        """
        #点击新增角色按钮
        self.click_element("role_new")
        #输入名称
        self.send_text(name,"role_name")
        #输入别名
        self.send_text(other_name,"role_other_name")
        #选择授权系统
        self.click_element("select_system")
        self.click_element("system_list")
        #遍历勾选数据
        for index in select_list:
            self.click_element("select",index=index)
        #点击确定按钮
        self.click_element("role_ok")