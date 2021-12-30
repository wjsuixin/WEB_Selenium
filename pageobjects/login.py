# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/8 15:19
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from base.url_save import *
from base.base_page import BasePage


class LoginPage(BasePage):

    def login(self,user,password):
        """
        登录操作
        """
        #打开登录网页
        self.open_url(URLSAVE().LOGIN)
        #输入用户名
        self.send_text(user,"username")
        #输入密码
        self.send_text(password,"password")
        #点击登录按钮
        self.click_element("login_btn")

    def get_index(self):
        """
        获取首页，返回bool值
        """
        element=self.get_element("index_title")
        if element!=None:
            return True
        else:
            return False

    def login_out(self):
        """
        注销登录
        """
        self.move_element("user","login_out")




if __name__ == '__main__':
    l=LoginPage()
    l.login("wj@qq.com","yx1234")
    l.login_out()