# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/9 16:17
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from base.test_base import TestBase
from pageobjects.login import LoginPage

class TestLogin(TestBase,LoginPage):
    """
    登录测试类
    """
    def test_login_success(self):
        """
        正常用户登录成功测试用例
        """
        self.login("wj@qq.com","yx1234")
        self.assertTrue(self.get_index())

    def test_login_out(self):
        """
        注销成功测试用例
        """
        self.login("wj@qq.com","yx1234")
        self.login_out()
        self.assertEqual(self.get_text("text"),"欢迎登录研学服务平台")

    def test_forbidden_user(self):
        """
        停用的用户登录失败测试用例
        """
        self.login("12122334455@QQ.COM","yx1234")
        self.assertEqual(self.get_text("login_error_text"),"已停用，请联系管理员!")

    def test_error_password(self):
        """
        错误密码登录失败测试用例
        """
        self.login("wj@qq.com","yx123")
        self.assertEqual(self.get_text("login_error_text"),"用户名或密码错误！")

    def test_invalid_user(self):
        """
        无效用户名登录失败测试用例
        """
        self.login("wj@qq.com","yx12345")
        self.assertEqual(self.get_text("login_error_text"),"无效的用户！")
