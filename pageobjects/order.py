# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/21 14:10
from faker import Faker
from pageobjects.login import LoginPage
from base.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
# 创建一个日志实例
logger = Logger(logger="Order").getlog()
faker=Faker()
class Order(LoginPage):
    """
    订单管理页面类
    """
    def start_path(self):
        """
        进入订单列表界面
        """
        self.login("wj@qq.com", "yx1234")
        # 点击订单菜单
        self.click_element("basic", index=1)
        # 点击子菜单订单/团组查询
        self.sleep(1)
        self.click_element("basic_list", index=12)

    def new_order(self):
        """
        新建订单
        """
        self.click_element("new_order")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.click_element("sale")
        self.click_element("sale_name")
        self.click_element("Organization")
        self.click_element("Organization_name")
        self.click_element("customer")
        self.click_element("customer_name")
        self.click_element("start_date")
        self.click_element("start_time")
        self.click_element("start_time")
        self.sleep(1)
        code = self.get_element("code").get_attribute("value")
        logger.info("此处打印订单号:{0}".format(code))
        self.click_element("contract")
        self.click_element("contract_Y")
        self.click_element("destination")
        self.click_element("destination_name")
        self.click_element("groupType")
        self.click_element("groupType_name")
        self.driver.find_element_by_id("groupTypeCustom_Ids").click()
        self.driver.find_element_by_xpath("//div[text()='党建活动']").click()
        self.send_text(100,"unitPrice")
        self.send_text(20,"gpr")
        self.click_element("goSchool")
        self.click_element("shool_name")
        self.send_text( 1000,"studentNum")
        self.click_element("orderChannelType")
        self.click_element("orderChannelType_name")
        self.send_text(10,"monthBillPeriod")
        self.send_text("1111111","order_text")
        self.click_element("next")

        # 第二页数据
        # 1、勾选资源
        self.sleep(1)
        self.get_element("base_camp").click()
        self.get_element("Traffic").click()
        self.get_element("Meal").click()
        self.get_element("Worker").click()
        self.get_element("Material").click()
        self.get_element("Insurance").click()
        self.get_element("Hotel").click()
        self.get_element("Design").click()

        # 2、勾选城市
        self.click_element("start_city")
        self.click_element("city_name")
        self.click_element("arrive_city")
        self.click_element("a_city_name")

        # 3、添加餐资源
        self.get_elements("add_resource")[1].click()
        self.get_elements("resource_name")[0].click()

        # 3-1 添加餐要求
        self.click_element("time")
        self.click_element("meal_H",index=0)
        self.click_element("meal_H",index=1)
        self.click_element("quedin")
        self.click_element("yoncanrenyuan")
        self.click_element("yoncanrenyuan_name")
        self.click_element("mealType")
        self.click_element("mealType_name")
        self.click_element("save_resource",index=1)

        # 3-2 添加酒店资源
        self.click_element("add_resource",index=1)
        self.click_element("add_hotel",index=1)
        self.click_element("student_zili")
        self.click_element("time")
        self.click_element("meal_H", index=0)
        self.click_element("meal_H", index=1)
        self.click_element("quedin")
        self.driver.find_element_by_xpath('//*[@id="starCustomId"]').click()
        self.click_element("start_name")
        # base_view.click_element("breakfast")
        self.driver.find_element_by_xpath('//*[@id="breakfastCustomId"]').click()
        self.click_element("breakfast_name")
        # base_view.click_element("room")
        self.driver.find_element_by_xpath('//*[@id="roomAmountPairs_0_roomCustomId"]').click()
        self.click_element("room_name")
        self.send_text(20,"roomAmount")
        self.click_element("save_resource",index=1)

        # 4、点击下一步，填写第三页数据
        self.click_element("next_2",index=1)

        # 5、添加工作人员要求
        self.click_element("worker_type")
        self.click_element("work")
        ActionChains(driver=self.driver).move_by_offset(200, 100).click().perform()

        # 6、添加保险要求
        self.click_element("insur")

        # 7、添加交通要求
        js = "window.scrollTo(200,document.body.scrollHeight);"
        self.driver.execute_script(js)
        self.sleep(1)
        self.click_element("trafficModes")
        self.click_element("trafficMode")
        self.click_element("departureTime")
        self.click_element("next_Mouth")
        self.click_element("choice_day")
        self.click_element("time_save")
        self.click_element("Vehicle_start")
        self.click_element("Vehicle_start_city")
        self.click_element("returnTime")
        self.click_element("returnTime_nextM")
        self.click_element("returnday")
        self.click_element("return_time_save")
        self.click_element("return_city")
        self.click_element("return_city_name")
        self.send_text(30,"vehicleAmount")
        self.click_element("VehicleCls")
        self.click_element("VehicleCls_num")

        # 美化要求的添加
        self.click_element("designRequire")
        # element = base_view.finds_element("designRequire")
        # element.click()
        self.click_element("Require")

        # 订单提交
        self.click_element("order_submit")


if __name__ == '__main__':
    order=Order()
    order.start_path()
    order.new_order()
    order.driver.quit()