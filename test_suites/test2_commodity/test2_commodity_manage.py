# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from framework.browser_info import Browser_Info
from page_objects.test_commodity.test_commodity_manage import Commodity_Commodity_Manage

from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
get_browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page_objects.test_commodity.test_commodity_manage import Commodity_Commodity_Manage


class Test_Commodity_Commodity_Manage(unittest.TestCase):
    """
    商品-商品管理模块
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        register_page = Commodity_Commodity_Manage(self.driver)
        register_page.into_commodity_manage_page()
    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    #拿到json里的数据进行数据驱动测试
    # @file_data(data_path)
    def test01_inquire_commodity(self):
        """
        查询存在商品
        """
        register_page = Commodity_Commodity_Manage(self.driver)
        result = register_page.inquire_commodity_name("日本进口pilot百乐贵客钢笔")
        if result:
            self.assertTrue(result, logger.info("查询商品用例用例执行成功."))

        else:
            self.assertTrue(result, logger.error("查询存在商品用例执行失败!"))

    def test02_inquire_commodity_classify(self):
        """
        通过存在的商品分类进行查询
        """
        register_page = Commodity_Commodity_Manage(self.driver)
        result = register_page.inquire_suppliers("文具","UAT新增供货商3")
        if result:
            self.assertTrue(result, logger.info("通过存在的商品分类进行查询用例执行成功."))

        else:
            self.assertTrue(result, logger.error("通过存在的商品分类进行查询用例执行失败!"))
