import string
import time
import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.test_login_logout.test_login import Login_And_Logout_Page
from config.element_commodity.element_supplier import Element_Supplier

logger = Logger(logger='测试流程').get_log()

class Commodity_Suppliers(BasePage,Element_Supplier):
    """
    商店-供应商相关用例
    """
    def into_suppliers_page(self):
        """
        进入供货商管理页面
        :return:
        """
        Login_And_Logout_Page(self.driver).get_login_result("admin","123456")
        self.click(*self.commodity_button_element)
        self.click(*self.supplise_button_elment)
        self.frame(*self.first_iframe)
    def add_suppliers(self,suppliers_name):
        """新增供货商"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.frame(*self.second_iframe)
            self.input(suppliers_name, *self.add_name_input)
            self.input("UAT测试", *self.add_contact_input)
            self.input("15913174653", *self.add_tel_input)
            self.input("珠海市香洲区", *self.add_address_input)
            self.input(f"测试{suppliers_name}", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            WebDriverWait(self.driver, 5, 0.1).until(EC.visibility_of_element_located(self.public_element_add_succeed))
            logger.info(self.get_element(*self.public_element_add_succeed))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供应商失败!")
            logger.error(self.get_element(*self.public_element_add_succeed))
            logger.error(e)
            self.get_windows_img()
            return False
    def add_exist_suppliers(self,suppliers_name):
        """新增已存在的供货商"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.frame(*self.second_iframe)
            self.input(suppliers_name, *self.add_name_input)
            self.input("UAT测试", *self.add_contact_input)
            self.input("15913174653", *self.add_tel_input)
            self.input("珠海市香洲区", *self.add_address_input)
            self.input(f"测试{suppliers_name}", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_name_exist))
            logger.info(self.get_element(*self.public_element_name_exist))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增已存在的供应商失败!")
            logger.error(self.get_element(*self.public_element_name_exist))
            logger.error(e)
            self.get_windows_img()
            return False

    def add_suppliers_no_name(self):
        """新增供货商不填充名称"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.frame(*self.second_iframe)
            self.input("UAT测试", *self.add_contact_input)
            self.input("15913174653", *self.add_tel_input)
            self.input("珠海市香洲区", *self.add_address_input)
            self.input(f"测试新增不填充名称", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            self.frame(*self.second_iframe)
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(self.get_element(*self.public_element_required_no_null))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供应商不填充名称失败!")
            logger.error(self.get_element(*self.public_element_required_no_null))
            # logger.error(e)
            self.get_windows_img()
            return False

    def add_suppliers_no_contact_name(self):
        """新增供货商不填充联系人名称"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.frame(*self.second_iframe)
            self.input("测试新增供货商不填充联系人名称", *self.add_name_input)
            # self.input("UAT测试", *self.add_contact_input)
            self.input("15913174653", *self.add_tel_input)
            self.input("珠海市香洲区", *self.add_address_input)
            self.input(f"测试新增供货商不填充联系人名称", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            self.frame(*self.second_iframe)
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(self.get_element(*self.public_element_required_no_null))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供货商不填充联系人名称失败!")
            logger.error(self.get_element(*self.public_element_required_no_null))
            logger.error(e)
            self.get_windows_img()
            return False

    def add_suppliers_no_contact_tel(self):
        """测试新增供货商不填充联系人号码"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.frame(*self.second_iframe)
            self.input("测试新增供货商不填充联系人名称", *self.add_name_input)
            self.input("UAT测试", *self.add_contact_input)
            # self.input("15913174653", *self.add_tel_input)
            self.input("珠海市香洲区", *self.add_address_input)
            self.input(f"测试新增供货商不填充联系人名称", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            self.frame(*self.second_iframe)
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            element = self.get_element(*self.public_element_required_no_null)
            logger.info(f"元素:{element}出现")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供货商不填充联系人名称失败!")
            logger.error(self.get_element(*self.public_element_required_no_null))
            # logger.error(e)
            self.get_windows_img()
            return False

    def add_suppliers_cancel(self):
        """新增供货商点击取消"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            self.click_Cancel()
            WebDriverWait(self.driver, 5, 1).until(EC.none_of(EC.presence_of_element_located(self.add_supliers_window)))
            logger.info("不存在新增供货商弹窗")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供货商点击取消失败!")
            # logger.error(self.get_element('xpath',"//div[@class='layui-layer-title']"))
            logger.error(e)
            self.get_windows_img()
            return False

    def add_suppliers_close(self):
        """新增供货商点击关闭"""
        try:
            self.actionchains_click(*self.add_supplise_button_elment)
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.add_supliers_window))
            self.click_window_close()
            WebDriverWait(self.driver, 5, 1).until(EC.invisibility_of_element_located(self.add_supliers_window))
            logger.info("不存在新增供货商弹窗")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("新增供货商点击关闭失败!")
            # logger.error(self.get_element('xpath',"//div[@class='layui-layer-title']"))
            logger.error(e)
            self.get_windows_img()
            return False

    def inquire_suppliers(self,suppliers_name):
        """查询供货商成功"""
        try:
            self.input(suppliers_name, *self.supplise_inquire_input)
            self.click_inquire()
            self.select_by_value("90")
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(('xpath', f"//div[text()='{suppliers_name}']")))
            element = self.get_element('xpath', f"//div[text()='{suppliers_name}']")
            logger.info(f"供货商:{(element)}出现")
            self.get_windows_img()
            return True
        except TimeoutException as e:
            logger.error(f"查询供供货商失败无{suppliers_name}!")
            logger.error(self.get_element('xpath', f"//div[text()='{suppliers_name}']"))
            # logger.error(e)
            self.get_windows_img()
            return False

    def inquire_not_exist_suppliers(self,suppliers_name):
        """查询不存在供货商"""
        try:
            self.input(suppliers_name, *self.supplise_inquire_input)
            self.click_inquire()
            WebDriverWait(self.driver,5, 1).until(EC.presence_of_element_located(self.public_element_no_data))
            # element = self.get_element(*self.public_element_no_data)
            # logger.info(f"元素:{element}出现")
            logger.info(f"元素:{self.get_element(*self.public_element_no_data)}出现")
            self.get_windows_img()
            return True
        except Exception as e:
            # logger.error(f"查询不存在供应商{suppliers_name}失败!")
            logger.error(self.get_element(*self.public_element_no_data))
            self.get_windows_img()
            return False

    def empty_inquire(self,suppliers_name):
        """清空查询"""
        try:
            total_quantity = (self.get_element(*self.public_element_total_quantity))
            number = ''.join(filter(str.isdigit,total_quantity))
            self.input(suppliers_name, *self.supplise_inquire_input)
            self.click_inquire()
            self.click_empty_inquire()
            WebDriverWait(self.driver,5, 1).until(EC.text_to_be_present_in_element(self.public_element_total_quantity,number))
            logger.info(f"总数{number}与查询后重置的数量:{self.get_element(*self.public_element_total_quantity)}一致")
            WebDriverWait(self.driver, 5, 1).until(EC.text_to_be_present_in_element(self.supplise_inquire_input,"" ))
            logger.info(f"供货商名称输入框已被清空")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error(f"总数与查询后重置的数量不一致或供货商名称输入框清空失败!")
            # logger.error(self.get_element(*self.public_element_no_data))
            self.get_windows_img()
            return False
    def revise_suppliers(self,old_suppliers_name,new_suppliers_name):
        """修改供应商"""
        try:
            self.click('xpath',f"//td[@data-field='name']/div[text()='{old_suppliers_name}']/parent::*/parent::*//a[text()='修改']")
            self.frame(*self.revise_iframe)
            self.input(f"{new_suppliers_name}", *self.add_name_input)
            self.input("测试人员", *self.add_contact_input)
            self.input("15913171317", *self.add_tel_input)
            self.input("珠海市香洲区上冲", *self.add_address_input)
            self.input("UAT测试修改供应商", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_revise_succeed))
            logger.info(self.get_element(*self.public_element_revise_succeed))
            self.get_windows_img()
            self.click_empty_inquire()
            return True
        except Exception as e:
            logger.error("修改供应商失败!")
            logger.error(self.get_element(('xpath',"//div[text()='修改供应商']")))
            self.get_windows_img()
            return False

    def revise_suppliers_no_name(self,old_suppliers_name):
        """修改供应商清空名称"""
        try:
            self.click('xpath',f"//td[@data-field='name']/div[text()='{old_suppliers_name}']/parent::*/parent::*//a[text()='修改']")
            self.frame(*self.revise_iframe)
            self.input("", *self.add_name_input)
            self.input("测试人员", *self.add_contact_input)
            self.input("15913171317", *self.add_tel_input)
            self.input("珠海市香洲区上冲", *self.add_address_input)
            self.input("UAT测试修改供应商", *self.add_remark_input)
            self.parent_frame()
            self.click_determine()
            self.frame(*self.revise_iframe)
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(f"出现元素{self.get_element(*self.public_element_required_no_null)}")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("修改供应商清空名称失败!")
            logger.error(f"未出现元素{self.get_element(*self.public_element_required_no_null)}")
            self.get_windows_img()
            return False

    def revise_suppliers_close(self,old_suppliers_name):
        """修改供应商取消"""
        try:
            self.click('xpath',f"//td[@data-field='name']/div[text()='{old_suppliers_name}']/parent::*/parent::*//a[text()='修改']")
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.revise_supliers_window))
            self.click_Cancel()
            WebDriverWait(self.driver, 5, 1).until(EC.invisibility_of_element_located (self.revise_supliers_window))
            logger.info(f"修改供货商弹窗关闭成功")
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("修改供货商弹窗关闭失败!")
            logger.error(f"失败原因{e}")
            self.get_windows_img()
            return False
    def delete_suppliers(self,suppliers_name):
        """删除供应商"""
        try:
            self.click('xpath', f"//td[@data-field='name']/div[text()='{suppliers_name}']/parent::*/parent::*//a[text()='删除']")
            self.click_determine()
            WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(self.public_element_delete_succeed))
            logger.info(self.get_element(*self.public_element_delete_succeed))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("删除供应商失败!")
            logger.error(self.get_element(*self.public_element_delete_succeed))
            logger.error(e)
            self.get_windows_img()
            return False
    def delete_suppliers_close(self,suppliers_name):
        """删除供应商取消"""
        try:
            self.click('xpath', f"//td[@data-field='name']/div[text()='{suppliers_name}']/parent::*/parent::*//a[text()='删除']")
            self.click_Cancel()
            WebDriverWait(self.driver, 5, 1).until(EC.invisibility_of_element_located(self.public_element_delete_quantity))
            # logger.info(self.get_element(*self.public_element_delete_succeed))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("删除供应商取消失败!")
            # logger.error(self.get_element(*self.public_element_delete_succeed))
            logger.error(e)
            self.get_windows_img()
            return False


    def suppliers_page(self):
        """供应商选择每页显示20条数据"""

        Login_And_Logout_Page(self.driver).get_login_result()
        self.click(*self.commodity_button_element)
        self.click(*self.supplise_button_elment)
        self.frame(*self.first_iframe)
        self.select_by_value("20")
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(('xpath',"//div[text()='11']")))
            #logger.info(self.get_element(('xpath',"//div[text()='11']")))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("供应商选择每页显示20条数据失败!")
            logger.error(self.get_element(('xpath',"//div[text()='11']")))
            logger.error(e)
            self.get_windows_img()
            return False









