import os
import json
import time
from _ast import Assert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.base_page import BasePage
from config.element_login_logout.elment_login import Elment_Login
logger = Logger(logger='测试流程').get_log()

class Login_And_Logout_Page(BasePage,Elment_Login):
    """
    登录相关用例
    """

    #def login(self):
        # 以下为调试使用
        # login = Login(self.driver)
        # login.login('')

       # if self.get_account():
         #   login = Login(self.driver)
            # 参数为'superadmin'就登录superadmin账号，其他则登录注册成功的账号
         #   login.login('')
       # else:
           # raise Exception('登录账号为空!')

    def get_login_result(self,name,passward):
        """
        admin账号登录成功
        :return:
        """
        self.input(name,*self.login_user_input)
        self.input(passward,*self.login_password_input)
        self.input("我我我我",*self.login_captcha_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(self.login_succeed_assertion))
            logger.info(self.get_element(*self.login_succeed_assertion))
            #self.get_windows_img()
            return True
        except Exception:
            logger.error("登录失败!")
            logger.error(self.get_element(*self.login_succeed_assertion))
            self.get_windows_img()
            return False

    def get_null_user_login(self):
        """
        空账户登录
        :return:
        """
        self.input("我我我我", *self.login_captcha_input)
        self.input("1234.abcd",*self.login_password_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(self.get_element(*self.public_element_required_no_null))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("空账户登录用例执行失败")
            logger.error(self.get_element(*self.login_button_element))
            self.get_windows_img()
            return False

    def get_null_password_login(self):
        """
        空密码登录
        :return:
        """
        self.input("1234.abcd",*self.login_user_input)
        self.input("我我我我", *self.login_captcha_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(self.get_element(*self.public_element_required_no_null))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("空密码登录用例执行失败")
            logger.error(self.get_element(*self.login_button_element))
            self.get_windows_img()
            return False

    def get_error_password_login(self):
        """
        错误密码登录
        :return:
        """
        self.input("admin",*self.login_user_input)
        self.input("1234", *self.login_password_input)
        self.input("我我我我", *self.login_captcha_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.account_password_error_assertion))
            logger.info(self.get_element(*self.account_password_error_assertion))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("错误密码登录用例执行失败")
            logger.error(self.get_element(*self.account_password_error_assertion))
            self.get_windows_img()
            return False

    def get_error_captcha_login(self):
        """
        错误验证码登录
        :return:
        """
        self.input("admin",*self.login_user_input)
        self.input("1234.abcd", *self.login_password_input)
        self.input("123456", *self.login_captcha_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.login_captcha_error_assertion))
            logger.info(self.get_element(*self.login_captcha_error_assertion))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("错误验证码登录用例执行失败")
            logger.error(self.get_element(*self.login_captcha_error_assertion))
            self.get_windows_img()
            return False

    def get_null_captcha_login(self):
        """
        空验证码登录
        :return:
        """
        self.input("admin",*self.login_user_input)
        self.input("1234.abcd", *self.login_password_input)
        self.input("123456", *self.login_captcha_input)
        self.click(*self.login_button_element)
        try:
            WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(self.public_element_required_no_null))
            logger.info(self.get_element(*self.public_element_required_no_null))
            self.get_windows_img()
            return True
        except Exception:
            logger.error("空验证码登录用例执行失败")
            logger.error(self.get_element(*self.login_button_element))
            self.get_windows_img()
            return False

