# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from framework.browser_info import Browser_Info
from page_objects.test_login_logout.test_login import Login_And_Logout_Page

from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
get_browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test_Register(unittest.TestCase):
    """
    测试注册模块
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    #拿到json里的数据进行数据驱动测试
    # @file_data(data_path)
    def test1_login(self):
        """
        admin账号登录
        """
        name = "admin"
        passward = "123456"
        register_page = Login_And_Logout_Page(self.driver)
        result = register_page.get_login_result(name,passward)
        if result:
            self.assertTrue(result, logger.info("登录用例执行成功."))

        else:
            self.assertTrue(result, logger.error("登录用例执行失败!"))
    def test2_null_user_login(self):
        '''
        空用户名登录
        '''
        register_page = Login_And_Logout_Page(self.driver)
        result = register_page.get_null_user_login()
        if result:
            self.assertTrue(result, logger.info("空用户名登录用例执行成功."))

        else:
            self.assertTrue(result, logger.error("空用户名登录用例执行失败!"))

    def test3_null_password_login(self):
        '''
        密码登录
        '''
        register_page = Login_And_Logout_Page(self.driver)
        result = register_page.get_null_password_login()
        if result:
            self.assertTrue(result, logger.info("密码登录用例执行成功."))

        else:
            self.assertTrue(result, logger.error("密码登录用例执行失败!"))

    def test4_error_password_login(self):
        '''
        错误密码登录
        '''
        register_page = Login_And_Logout_Page(self.driver)
        result = register_page.get_error_password_login()
        if result:
            self.assertTrue(result, logger.info("错误密码登录用例执行成功."))

        else:
            self.assertTrue(result, logger.error("错误密码登录用例执行失败!"))

    def test5_error_captcha_login(self):
        '''
        错误验证码登录
        '''
        register_page = Login_And_Logout_Page(self.driver)
        result = register_page.get_error_captcha_login()
        if result:
            self.assertTrue(result, logger.info("错误验证码登录用例执行成功."))

        else:
            self.assertTrue(result, logger.error("错误验证码登录用例执行失败!"))
if __name__ == '__main__':
    unittest.main()
