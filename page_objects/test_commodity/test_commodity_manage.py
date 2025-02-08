import time
import webbrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from page_objects.test_login_logout.test_login import Login_And_Logout_Page
from config.element_commodity.element_commodity_manage import Element_Commodity_Manage

logger = Logger(logger='测试流程').get_log()

class Commodity_Commodity_Manage(BasePage,Element_Commodity_Manage):
    """
    商店-商品管理相关用例
    """

    def into_commodity_manage_page(self):
        """
        进入商品管理页面
        :return:
        """
        Login_And_Logout_Page(self.driver).get_login_result("admin","123456")
        self.click(*self.commodity_button_element)
        self.click(*self.commodity_manage_element)
        self.frame(*self.first_iframe)

    def inquire_commodity_name(self,commodity_name):
        """通过存在的商品名称查询"""
        try:

            self.input(commodity_name, *self.inquire_commodity_name_element)
            self.click_inquire()
            WebDriverWait(self.driver, 50, 1).until(EC.presence_of_element_located(('xpath', f"//td[@data-field='name']/div[contains(string(),'{commodity_name}')]")))
            # logger.info(self.get_element(('xpath', f"//div[text()[contains(., '%s')]]")))
            self.get_windows_img()
            return True
        except Exception as e:
            logger.error("通过存在的商品名称查询失败!")
            #logger.error(self.get_element(*self.login_button_element))  2023-10-18 16:19:18
            logger.error(e)
            self.get_windows_img()
            return False

    def inquire_suppliers(self,text,text1):
        self.select_item_classification(text)
        self.select_suppliers(text1)
        time.sleep(10)

    def add_commodity(self,commodity_name):
        try:
            self.click(*self.publish_commodity)


        except Exception as e:
            return False


