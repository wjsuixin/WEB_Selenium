# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/8 17:29
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
from faker import Faker
from pageobjects.login import LoginPage
from base.logger import Logger

# 创建一个日志实例
logger = Logger(logger="JobMange").getlog()

class JobMange(LoginPage):
    """
    岗位管理页面类
    """
    def star_path(self):
        """
        进入岗位管理的入口
        """
        self.login("wj@qq.com", "yx1234")
        #点击基础档案菜单
        self.click_element("basic",index=9)
        #点击子菜单岗位管理
        self.sleep(1)
        self.click_element("basic_list",index=13)

    def new_job(self,name,desc):
        """
        新增岗位管理
        """
        #点击新增
        self.click_element("job_add")
        #输入岗位名称
        self.send_text(name,"job_name")
        #输入岗位描述
        self.send_text(desc,"job_desc")
        #点击确定按钮
        self.click_element("job_check",index=26)

    def edit_job(self,data,name,desc):
        """
        编辑岗位
        """
        #查询出需要编辑的数据
        self.list_data(data)
        #点击编辑按钮
        self.click_element("edit_btn")
        #校验此时的名称是不是输入的名称
        if self.get_text("job_name","value")==data:
            self.clear_data("job_name")
        else:
            return False,logger.error("该岗位名称新增时的数据，与编辑前的数据不一致，请核实。")
        # 输入岗位名称
        self.send_text(name, "job_name" + "001")
        # 输入岗位描述
        self.send_text(desc, "job_desc")
        # 点击确定按钮
        self.click_element("job_check", index=26)

    def list_data(self,data,status=None):
        """
        查询数据
        """
        if status==None: #只查询名称，状态为全部
            # 输入名称
            self.send_text(data,"name_list")
        else:
            #点击状态为全部按钮
            self.click_element("all_status")
            if status=="enable":
                #点击启用条件按钮
                self.click_element("enable_status")
            else:
                #点击停用条件按钮
                self.click_element("disable_status")
            # 输入名称
            self.send_text(data, "name_list")
        #点击查询
        self.click_element("job_query")

    def select_check_data(self,*index_list):
        """
        勾选数据
        """
        if index_list==None:
            #勾选全部数据
            #self.click_element("selct_data", index=0)
            self.driver.find_elements_by_class_name("ant-checkbox-input")[0].click()
        else:
            if 0 not in index_list:
                for index in index_list:
                    #遍历index_list并完成勾选数据
                    self.click_element("selct_data", index=index)
            else:
                logger.error("index_list中不能存在0，请重新选择1~10值。")

    def batch_change_status(self,status=None,index=None):
        """
        批量启用/停用数据
        """
        if status==None:
            #勾选全部数据
            self.select_check_data(index)
            #WebDriverWait(self.driver,2).until(EC.element_to_be_clickable((By.XPATH,"dis_enable_btn")))
            print(self.get_element("dis_enable_btn").value_of_css_property("button"))
            #return self.get_element("dis_enable_btn")#返回bool值
        else:
            if status=="disable":
                #批量停用
                self.click_element("disable_btn",index=9)
            else:
                #批量启用
                self.click_element("enable_btn", index=10)

if __name__ == '__main__':
    fake=Faker()
    DATA=fake.job()
    job= JobMange()
    job.star_path()
    #job.new_job(DATA,"1111111111111111")
    print(job.batch_change_status())