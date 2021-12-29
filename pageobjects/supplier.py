# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/14 14:56
from faker import Faker
from pageobjects.login import LoginPage
from base.logger import Logger
# 创建一个日志实例
logger = Logger(logger="JobMange").getlog()
faker=Faker()
class Supplier(LoginPage):
    """
    供应商管理页面类
    """
    def start_path(self):
        """
        进入供应商界面
        """
        self.login("wj@qq.com", "yx1234")
        # 点击供应商菜单
        self.click_element("basic", index=5)
        # 点击子菜单供应商管理
        self.sleep(1)
        self.click_element("basic_list", index=12)

    def new_supplier_basicinfo(self,name,supplier_phoneNo,address=None,email=None,category_type=None,remark=None):
        """
        新增供应商数据-基础信息部分
        """
        #点击新增按钮
        self.click_element("su_new_btn")
        #输入名称
        self.send_text(name,"supplier_name")
        #选择国家-中国
        #self.click_element("supplier_country")
        self.driver.find_element_by_id("countryId").click()
        self.click_element("supplier_country_list")
        #选择省市
        button = self.driver.find_element_by_id('provinceCityId')
        self.driver.execute_script("(arguments[0]).click()", button)
        self.click_element("su_sheng")
        self.click_element("su_city")
        #输入地址非必填
        if address!=None:
            self.send_text(address,"supplier_address")
        #输入电话
        self.send_text(supplier_phoneNo, "supplier_phoneNo")
        #输入邮箱非必填
        if email!=None:
            self.send_text(email, "supplier_email")
        #选择类别

        self.click_element("category")
        #self.driver.find_element_by_id("category").click()
        if category_type==None:
            #选择类别为内部
            self.click_element("inner_category")
        else:
            # 选择类别为外部
            self.click_element("out_category")
        #输入备注
        if remark!=None:
            self.send_text(remark,"supplier_remark")

    def add_supplier(self):
        """
        添加上级供应商按钮，进入添加界面
        """
        return self.click_element("supplier_comm",index=0)

    def add_upper_supplier(self,su_name):
        """
        输入供应商名,完成添加
        """
        element_value='//div[@title="#su_name#"]'
        new_value=element_value.replace("#su_name#",su_name)
        #点击搜索框
        print(len(self.get_elements("supplier_add_btn")))
        self.click_element("supplier_add_btn",index=11)
        #清除输入框内容
        self.get_elements("supplier_clear")[1].clear()
        logger.info("执行清除输入框！")
        #输入需要搜索的供应商
        self.get_elements("supplier_comm")[11].send_keys(su_name)
        self.driver.find_element_by_xpath(new_value).click()
        #点击确定按钮保存
        self.click_element("supplier_submit",index=33)

    def add_resouce(self):
        """
        点击资源添加按钮
        """
        return self.click_element("supplier_comm",index=1)

    def add_resouce_list(self,resouce_type,resouce_name,copy=None):
        """
        添加资源
        """
        if resouce_type=="酒店":
            self.click_element("supplier_type",index=0)
        elif resouce_type=="交通方式":
            self.click_element("supplier_type",index=1)
        elif resouce_type=="基地营地":
            self.click_element("supplier_type",index=2)
        elif resouce_type=="工作人员":
            self.click_element("supplier_type",index=3)
        elif resouce_type=="餐":
            self.click_element("supplier_type",index=4)
        elif resouce_type=="物料":
            self.click_element("supplier_type",index=5)
        elif resouce_type=="保险":
            button=self.driver.find_elements_by_class_name("ant-radio-button")[6]
            self.driver.execute_script("(arguments[0]).click()",button)
            #self.click_element("supplier_type",index=6)
        elif resouce_type=="美化":
            self.click_element("supplier_type",index=1)
        else:
            logger.error(f"无该{resouce_type}的资源可以选择，请检查！")
        if copy==None:
            #取消勾选复制
            button = self.driver.find_elements_by_class_name("ant-checkbox-input")[11]
            self.driver.execute_script("(arguments[0]).click()", button)
         #输入资源名称并完成选择
        self.driver.find_elements_by_class_name("ant-select-selection-search-input")[10].click()
        self.driver.find_elements_by_class_name("ant-select-selection-search-input")[10].clear()
        logger.info("清除成功")
        #self.driver.find_elements_by_class_name("ant-select-selection-search-input")[10].send_keys(resouce_name)
        self.get_elements("su_resouce_name")[10].send_keys(resouce_name)
        self.sleep(1)
        element=self.driver.find_elements_by_class_name("ant-select-item-option")[3]
        self.driver.execute_script("(arguments[0]).click()", element)
        # 点击确定按钮保存
        self.click_element("supplier_submit", index=33)

    def new_contact(self,num=None):
        """
        添加联系人信息数据填写
        """
        if num==None:
            #点击添加按钮一次
            self.click_element("supplierContactsAdd")
        else:
            for i in range(num):
                #循环遍历num,点击添加按钮num次
                self.click_element("supplierContactsAdd")

    def supplier_contact_info(self,num,name,phone,wechatNo,position):
        """
        供应商联系人信息内容填写
        """
        contact_name=f"supplierContacts_{num}_name"
        contact_phoneNo=f"supplierContacts_{num}_phoneNo"
        contact_wechatNo=f"supplierContacts_{num}_wechatNo"
        contact_position=f"supplierContacts_{num}_position"
        self.driver.find_element_by_id(contact_name).send_keys(name)
        logger.info(f"元素'{contact_name}'输入'{name}'成功。")
        self.driver.find_element_by_id(contact_phoneNo).send_keys(phone)
        logger.info(f"元素'{contact_phoneNo}'输入'{phone}'成功。")
        self.driver.find_element_by_id(contact_wechatNo).send_keys(wechatNo)
        logger.info(f"元素'{contact_wechatNo}'输入'{wechatNo}'成功。")
        self.driver.find_element_by_id(contact_position).send_keys(position)
        logger.info(f"元素'{contact_position}'输入'{position}'成功。")

    def delete_contact(self,index=None):
        """
        删除联系人信息
        """
        if index==None:
            #默认删除第一个已添加的联系人信息
            self.click_element("delete_contact",index=0)
        else:
            if index>len(self.get_elements("delete_contact")):
                logger.error(f"index:{index}不能超过{len(self.get_elements('delete_contact'))},请检查需要删除的联系人!")
            else:
                #删除指定的联系人信息
                self.click_element("delete_contact",index=index)

    def payment_cycle(self,cycle_type=None):
        """
        付款周期选择
        """
        if cycle_type==None:
            self.driver.find_elements_by_class_name("ant-radio-input")[0].click()
        elif cycle_type=="周结":
            self.driver.find_elements_by_class_name("ant-radio-input")[1].click()
        elif cycle_type=="半月结":
            self.driver.find_elements_by_class_name("ant-radio-input")[2].click()
        elif cycle_type=="月结":
            self.driver.find_elements_by_class_name("ant-radio-input")[3].click()
        elif cycle_type=="季结":
            self.driver.find_elements_by_class_name("ant-radio-input")[4].click()
        elif cycle_type=="实时转账":
            self.driver.find_elements_by_class_name("ant-radio-input")[5].click()
        elif cycle_type == "团结":
            self.driver.find_elements_by_class_name("ant-radio-input")[6].click()
        else:
            logger.error(f"没有{cycle_type}类型的付款周期选择！")

    def payment_type(self,key):
        """
        付款方式选择
        """
        if key=="银行转账":
            self.click_element("BANK_TRANSFER")
        elif key=="信用卡":
            self.click_element("CREDIT_CARD")
        elif key=="现金":
            self.click_element("CASH")
        elif key=="支票":
            self.click_element("CHEQUE")
        elif key=="支付宝":
            self.click_element("ALIPAY")
        else:
            logger.error(f"没有'{key}'付款方式可以选择！")

    def su_payment_info(self,key,type=None,payPeriod=None):
        """
        付款信息的填写
        """
        if type==None:
            #选择预付比例50
            self.driver.find_element_by_id("prepayPercent").click()
            self.click_element("Percent_50")
        else:
            self.payment_cycle(type)
        if payPeriod!=None:
            #输入账期
            self.send_text(payPeriod,"supplier_payPeriod")
        # 选择付款方式
        self.driver.find_element_by_id("payType").click()
        self.payment_type(key)
        # 选择币种
        self.driver.find_element_by_id("currencyId").click()
        self.click_element("CNY")

    def bank_account_type(self,key):
        """
        银行账户信息-账户类型
        """
        if key=="储蓄卡":
            self.click_element("account_CASH")
            logger.info(f"点击{key}成功。")
        elif key=="支付宝":
            self.click_element("account_ALIPAY")
            logger.info(f"点击{key}成功。")
        elif key=="信用卡":
            self.click_element("account_CREDIT")
            logger.info(f"点击{key}成功。")
        else:
            logger.error(f"没有{key}账户类型可以选择！")

    def new_bankinfo(self,num=None):
        """
        添加银行账户信息数据填写
        """
        if num==None:
            #点击添加按钮一次
            self.click_element("add_bank")
        else:
            for i in range(num):
                #循环遍历num,点击添加按钮num次
                self.click_element("add_bank")

    def bank_info(self,num,account_Name,key,account_No,bank_Name,swiftBic_No=None,country=None,City=None,bank_Address=None,payee_Address=None):
        """
        银行账户信息的填写
        """
        accountName = f"supplierBankAccounts_{num}_accountName"
        accountNo=f"supplierBankAccounts_{num}_accountNo"
        payType=f"supplierBankAccounts_{num}_payType"
        swiftBic=f"supplierBankAccounts_{num}_swiftBic"
        bankName=f"supplierBankAccounts_{num}_bankName"
        countryId=f"supplierBankAccounts_{num}_countryId"
        BankCity=f"supplierBankAccounts_{num}_accountBankCity"
        bankAddress=f"supplierBankAccounts_{num}_bankAddress"
        payeeAddress=f"supplierBankAccounts_{num}_payeeAddress"
        #输入账户名
        self.driver.find_element_by_id(accountName).send_keys(account_Name)
        logger.info(f"元素{accountName}输入{account_Name}成功。")
        #选择账户类型
        self.driver.find_element_by_id(payType).click()
        self.bank_account_type(key)
        #输入账号/IBAN
        self.driver.find_element_by_id(accountNo).send_keys(account_No)
        logger.info(f"元素{accountNo}输入{account_No}成功。")
        #输入开户行
        self.driver.find_element_by_id(bankName).send_keys(bank_Name)
        logger.info(f"元素{bankName}输入{bank_Name}成功。")
        #输入Swift/BIC
        if swiftBic_No!=None:
            self.driver.find_element_by_id(swiftBic).send_keys(swiftBic_No)
            logger.info(f"元素{swiftBic}输入{swiftBic_No}成功。")
        #输入开户行国家
        if country!=None:
            self.driver.find_element_by_id(countryId).click()
            button=self.driver.find_element_by_xpath("//div[@title='中国']")
            self.driver.execute_script("(arguments[0]).click()", button)
            #self.click_element("su_country")
        #输入开户行省市
        if City!=None:
            self.driver.find_element_by_id(BankCity).click()
            self.click_element("su_sheng")
            self.click_element("su_city")
        #输入开户行地址
        if bank_Address!=None:
            self.driver.find_element_by_id(bankAddress).send_keys(bank_Address)
            logger.info(f"元素{bankAddress}输入{bank_Address}成功。")
        #输入收款人地址
        if payeeAddress!=None:
            self.driver.find_element_by_id(payeeAddress).send_keys(payee_Address)
            logger.info(f"元素{payeeAddress}输入{payee_Address}成功。")

    def delete_bankinfo(self,index=None):
        """
        删除银行账户信息
        """
        if index == None:
            # 默认删除第一个已添加的银行账户信息
            self.click_element("delete_bankinfo", index=0)
        else:
            if index > len(self.get_elements("delete_bankinfo")):
                logger.error(f"index:{index}不能超过{len(self.get_elements('delete_bankinfo'))},请检查需要删除的银行账户信息!")
            else:
                # 删除指定的银行账户信息
                self.click_element("delete_bankinfo", index=index)

    def file_upload_type(self,type):
        """
        附件上传类型
        """
        if type=="合同":
            self.click_element("supplier_updload",index=1)
        elif type=="资质证明":
            self.click_element("supplier_updload",index=4)
        elif type=="账户证明（代收）":
            self.click_element("supplier_updload", index=2)
        elif type=="代收协议":
            self.click_element("supplier_updload", index=7)
        else:
            logger.error(f"供应商附件信息没有'{type}'的附件内容！")

    def upload_count(self,type,args):
        """
        文件上传个数
        """
        count=len(args)
        print(count)
        print(args)
        for i in range(count):
            self.file_upload_type(type)
            self.keybord_file_upload(args[i])

    def submit_data(self,btn_type=None):
        """
        提交数据返回列表页面
        """
        if btn_type==None:
            #默认点击确定按钮，保存数据
            button=self.get_element("su_submit")
            button.click()
            #self.driver.execute_script("arguments[0]).click()", button)
        else:
            #非默认则为取消
            self.click_element("su_cancel")


if __name__ == '__main__':
    su=Supplier()
    faker=Faker(locale="zh_CN")
    name=faker.company()
    supplier_phoneNo=faker.phone_number()
    wechat_no=faker.phone_number()
    address=faker.address()
    email=faker.company_email()
    su.start_path()
    su.new_supplier_basicinfo(name,supplier_phoneNo,address,email)
    #su.bank_info(2,faker.name(),"支付宝",faker.credit_card_number(),faker.credit_card_number(),faker.street_address(),faker.address(),faker.address())
    #su.add_supplier()
    #su.sleep(2)
    #su.add_upper_supplier("测试银行账户问题")
    su.add_resouce()
    su.add_resouce_list("保险","保险资源1")
    su.su_payment_info("现金")
    su.submit_data()

