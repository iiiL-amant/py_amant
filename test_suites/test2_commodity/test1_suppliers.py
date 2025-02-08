# coding=utf-8
import os
import unittest
from framework.browser_engine import BrowserEngine
from framework.browser_info import Browser_Info
from page_objects.test_commodity.test_suppliers import Commodity_Suppliers

from framework.logger import Logger

logger = Logger(logger='测试结果').get_log()
get_browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class Test_Commodity_Suppliers(unittest.TestCase):
    """
    商品-供货商模块
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        register_page = Commodity_Suppliers(self.driver)
        register_page.into_suppliers_page()
    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    #拿到json里的数据进行数据驱动测试
    # @file_data(data_path)
    def test01_add_suppliers_succeed(self):
        """
        新增供货商
        """
        suppliers_name = "UAT新增供货商"
        register_page = Commodity_Suppliers(self.driver)
        if register_page.inquire_suppliers(suppliers_name):# 前置操作：检查是否存在供货商，如存在则删除
            register_page.delete_suppliers(suppliers_name)
        # 新增供货商并得到结果
        result = register_page.add_suppliers(suppliers_name)
        if result:
            register_page.inquire_suppliers(suppliers_name)
            register_page.delete_suppliers(suppliers_name)# 如果新增成功，清除数据
            logger.info(f"新增供货商：({suppliers_name})用例执行成功.")
        else:
            logger.error(f"新增供货商：({suppliers_name})用例执行失败!")
        self.assertTrue(result)
    # def test02_add_suppliers_not_name(self):
    #     """
    #     新增供货商不填充供货商名称
    #     """
    #     register_page = Commodity_Suppliers(self.driver)
    #     result = register_page.add_suppliers_not_name()
    #     if result:
    #         self.assertTrue(result, logger.info("新增供货商不填充供货商名称用例执行成功."))
    #
    #     else:
    #         self.assertTrue(result, logger.error("新增供货商不填充供货商名称用例执行失败!"))
    def test02_add_exist_suppliers(self):
        """
        新增已存在的供货商
        :return:
        """
        exist_suppliers_name = "新增已存在的供货商"
        register_page = Commodity_Suppliers(self.driver)
        if not register_page.inquire_suppliers(exist_suppliers_name):
            register_page.add_suppliers(exist_suppliers_name)
        result = register_page.add_exist_suppliers(exist_suppliers_name)
        if result:
            logger.info(f"新增已存在的供货商：({exist_suppliers_name})用例执行成功.")
        else:
            logger.error(f"新增已存在的供货商：({exist_suppliers_name})用例执行失败!")
        self.assertTrue(result)
    def test03_add_suppliers_no_name(self):
        """
        新增供货商不填写供货商名称
        :return:
        """
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.add_suppliers_no_name()
        if result:
            logger.info("新增供货商不填写供货商名称用例执行成功")
        else:
            logger.error("新增供货商不填写供货商名称用例执行失败")
        self.assertTrue(result)

    def test04_add_suppliers_no_contact_name(self):
        """
        新增供货商不填写联系人名称
        :return:
        """
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.add_suppliers_no_contact_name()
        if result:
            logger.info("新增供货商不填写联系人名称用例执行成功")
        else:
            logger.error("新增供货商不填写联系人名称用例执行失败")
        self.assertTrue(result)

    def test05_add_suppliers_no_contact_tel(self):
        """
        新增供货商不填写供货商号码
        :return:
        """
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.add_suppliers_no_contact_tel()
        if result:
            logger.info("新增供货商不填写联系人号码用例执行成功")
        else:
            logger.error("新增供货商不填写联系人号码用例执行失败")
        self.assertTrue(result)

    def test06_add_suppliers_cancel(self):
        """
        新增供货商点击取消
        :return:
        """
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.add_suppliers_cancel()
        if result:
            logger.info("新增供货商点击取消用例执行成功")
        else:
            logger.error("新增供货商点击取消用例执行失败")
        self.assertTrue(result)

    def test07_add_suppliers_close(self):
        """
        新增供货商点击取消
        :return:
        """
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.add_suppliers_close()
        if result:
            logger.info("新增供货商点击关闭用例执行成功")
        else:
            logger.error("新增供货商点击关闭用例执行失败")
        self.assertTrue(result)
    def test08_inquire_suppliers(self):
        """
        查询供货商
        """
        suppliers_name = "123666"
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.inquire_suppliers(suppliers_name)
        # if not result:
        #     register_page.add_suppliers(suppliers_name)
        #     result = register_page.inquire_suppliers(suppliers_name)
        #     register_page.delete_suppliers(suppliers_name)
        if result:
            self.assertTrue(result, logger.info(f"查询供货商:{suppliers_name}用例执行成功."))
        else:
            self.assertTrue(result, logger.error(f"查询供货商:{suppliers_name}用例执行失败!"))
    def test09_inquire_not_exist_suppliers(self):
        """
        查询不存在供货商成功
        """
        suppliers_name = "UAT新增供货商110"
        register_page = Commodity_Suppliers(self.driver)
        if register_page.inquire_suppliers(suppliers_name):
            register_page.delete_suppliers(suppliers_name)
        result = register_page.inquire_not_exist_suppliers(suppliers_name)
        if result:
            self.assertTrue(result, logger.info(f"查询不存在供货商：{suppliers_name}用例执行成功."))

        else:
            self.assertTrue(result, logger.error(f"查询不存在供货商：{suppliers_name}用例执行失败!"))

    #
    def test10_inquire_empty_inquire(self):
        """
        查询后点击清空查询
        """
        suppliers_name = "AAAAAA"    #需要进行查询的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        result = register_page.empty_inquire(suppliers_name)
        if result:
            self.assertTrue(result, logger.info("查询不存在供货商后点击清空查询执行成功."))

        else:
            self.assertTrue(result, logger.error("查询不存在供货商后点击清空查询执行失败!"))

    def test09_revise_suppliers(self):
        """
        修改供货商
        """
        new_suppliers_name = "修改新供货商"   #经修改后的供货商名称
        old_suppliers_name = "修改旧供货商"   #修改前的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        if register_page.inquire_suppliers(new_suppliers_name):   # 检查并移除现有的'修改新供货商',确保修改后的供货商不存在
            register_page.delete_suppliers(new_suppliers_name)
        if not register_page.inquire_suppliers(old_suppliers_name):   # 检查'修改旧供货商'的存在，如果不存在则添加，确保有旧的供货商可以进行修改
            register_page.add_suppliers(old_suppliers_name)
        result = register_page.revise_suppliers(old_suppliers_name, new_suppliers_name) # 修改供货商并根据结果记录日志
        register_page.delete_suppliers(new_suppliers_name) # 清除数据
        if result:  # 根据结果生成日志并断言
            logger.info(f"修改供货商：{old_suppliers_name}用例执行成功.")
        else:
            logger.error(f"修改供货商：{old_suppliers_name}用例执行失败!")
        self.assertTrue(result)

    def test09_revise_suppliers_no_name(self):
        """
        修改供货商清空供货商名称
        """
        old_suppliers_name = "修改旧供货商"   #修改前的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        if not register_page.inquire_suppliers(old_suppliers_name):   # 检查'修改旧供货商'的存在，如果不存在则添加，确保有旧的供货商可以进行修改
            register_page.add_suppliers(old_suppliers_name)
        result = register_page.revise_suppliers_no_name(old_suppliers_name) # 修改供货商并根据结果记录日志
        if result:  # 根据结果生成日志并断言
            logger.info(f"修改供货商：{old_suppliers_name}清空名称用例执行成功.")
        else:
            logger.error(f"修改供货商：{old_suppliers_name}清空名称用例执行失败!")
        self.assertTrue(result)

    def test09_revise_suppliers_close(self):
        """
        修改供货商取消
        """
        old_suppliers_name = "修改旧供货商"   #修改前的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        if not register_page.inquire_suppliers(old_suppliers_name):   # 检查'修改旧供货商'的存在，如果不存在则添加，确保有旧的供货商可以进行修改
            register_page.add_suppliers(old_suppliers_name)
        result = register_page.revise_suppliers_close(old_suppliers_name) # 修改供货商并根据结果记录日志
        if result:  # 根据结果生成日志并断言
            logger.info(f"修改供货商：{old_suppliers_name}取消用例执行成功.")
        else:
            logger.error(f"修改供货商：{old_suppliers_name}取消用例执行失败!")
        self.assertTrue(result)
    def test10_delete_suppliers(self):
        """
        删除供货商
        """
        suppliers_name = "新增失败3"    #需要进行删除的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        if not register_page.inquire_suppliers(suppliers_name): #检查需要删除的供货商是否存在，如不存在就先新增供货商
            register_page.add_suppliers(suppliers_name)
        result = register_page.delete_suppliers(suppliers_name)
        if result:
            self.assertTrue(result, logger.info(f"删除供货商:{suppliers_name}用例执行成功."))

        else:
            self.assertTrue(result, logger.error(f"删除供货商:{suppliers_name}用例执行失败!"))
    def test10_delete_suppliers_close(self):
        """
        删除供货商取消
        """
        suppliers_name = "新增失败3"    #需要进行删除的供货商名称
        register_page = Commodity_Suppliers(self.driver)
        if not register_page.inquire_suppliers(suppliers_name): #检查需要删除的供货商是否存在，如不存在就先新增供货商
            register_page.add_suppliers(suppliers_name)
        result = register_page.delete_suppliers_close(suppliers_name)
        if result:
            self.assertTrue(result, logger.info(f"删除供货商:{suppliers_name}取消用例执行成功."))

        else:
            self.assertTrue(result, logger.error(f"删除供货商:{suppliers_name}取消用例执行失败!"))




if __name__ == '__main__':
    unittest.main()
