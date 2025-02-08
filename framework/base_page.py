# coding=utf-8
import math
import time
import os.path
import win32gui
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from framework.logger import Logger
from framework.browser_info import Browser_Info
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

# create a logger instance
logger = Logger(logger="测试流程").get_log()
get_browser_info = Browser_Info()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

account = None


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        """
        打开浏览器
        """
        # noinspection PyBroadException
        try:
            self.driver.get()
            logger.info("打开浏览器成功.")
        except Exception:
            logger.error("打开浏览器失败.")

    def get_windows_img(self):
        """
        浏览器截图操作
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹./screenshots下
        """
        try:

            file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshots')
            datatime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            screen_name = os.path.join(file_path, datatime + '.png')
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(f"已经成功截图并保存在 : {screen_name}")
        except Exception as e:
            logger.warning(f"截图失败： {e}.")

    def quit_browser(self):
        """
        浏览器退出操作
        """
        # noinspection PyBroadException
        try:
            self.driver.quit()
            logger.info("Click quit on current page.")
        except Exception:
            logger.warning("网页无法退出.")
            self.get_windows_img()

    def forward(self):
        """
        浏览器前进操作
        """
        # noinspection PyBroadException
        try:
            self.driver.forward()
            logger.info("Click forward on current page.")
        except Exception:
            logger.error("网页无法向前翻页.")
            self.get_windows_img()

    def back(self):
        """
        浏览器后退操作
        """
        # noinspection PyBroadException
        try:
            self.driver.back()
            logger.info("成功向后翻页浏览器.")
        except Exception:
            logger.error("网页无法向后翻页.")
            self.get_windows_img()

    def close(self):
        """
        点击关闭当前窗口
        """
        try:
            self.driver.close()
            logger.info("成功关闭当前窗口.")
        except Exception as e:
            logger.error(f"退出浏览器失败 {e}.")

    def implicit_wait(self, seconds):
        """
        隐式等待
        """
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(seconds)
            logger.info(f"隐式等待 {seconds} 秒.")
        except Exception:
            logger.warning("隐式等待失败.")
            self.get_windows_img()

    def forced_wait(self, *selector):
        """
        显式等待,进行操作之前都需要显式等待一下
        """
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 7, 1).until(EC.presence_of_element_located(selector))
            # logger.info('显式等待元素成功.')
        except Exception:
            logger.warning('显式等待元素失败.')

    # 暂时用不到这个自定义方法
    # def find_element(self, *selector):
    #     """
    #     定位元素方法
    #     传入元组
    #     传入的时候定义好定位的方式和元素
    #     """
    #     # noinspection PyBroadException
    #     try:
    #         # self.forced_wait(*selector)
    #         element = self.driver.find_element(*selector)
    #         logger.info(f"成功找到元素：{selector}")
    #         return element
    #     except Exception:
    #         logger.error(f"找不到元素: {self.get_element(*selector)}")
    #         self.get_windows_img()

    def find_element_attribute(self, attribute, *selector):
        """
        得到某个节点标签的属性值
        """
        self.forced_wait(*selector)
        try:
            value = self.driver.find_element(*selector).get_attribute(attribute)
            return value
        except Exception as e:
            logger.error("找不到该节点标签的属性值")
            logger.error(e)
            self.get_windows_img()
            return ''

    def get_element(self, *selector):
        """
        得到元素文本信息
        """
        # self.forced_wait()
        try:
            time.sleep(1)
            element = self.driver.find_element(*selector)
            return element.text
        except Exception as e:
            logger.error(f"找不到元素: {e}")
            self.get_windows_img()

    def input(self, text, *selector):
        """
        输入框输入信息
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element.clear()
            element.send_keys(text)
            logger.info(f"输入 '{text}' 成功")
        except Exception as e:
            logger.error(f"输入框输入失败")
            logger.error({e})
            self.get_windows_img()

    # def select_by_value(self, value):
    #     """
    #     列表选择展示多少条数据，10条/页、20条/页、30条/页、40条/页、50/页、60/页、70/页、80/页、90/页
    #     select标签下拉框通过value值选择,如10、20、30、40、50、60、70、80、90等
    #     """
    #     #self.forced_wait(*selector)
    #     try:
    #         time.sleep(0.5)
    #         element = self.driver.find_element('xpath',"//div[@id='layui-table-page1']//span[@class='layui-laypage-limits']//select")
    #         Select(element).select_by_value(value)
    #         element_name = element.text
    #         logger.info(f"下拉框'{element_name}'选择 '{value}' 成功")
    #     except Exception as e:
    #         element = self.driver.find_element('xpath',"//div[@id='layui-table-page1']//span[@class='layui-laypage-limits']//select")
    #         element_name = element.text
    #         logger.error(f"获取下拉框' {element_name} '失败")
    #         logger.error(f"下拉框选择失败")
    #         # logger.error({e})
    #         self.get_windows_img()
    #         time.sleep(1)
    #         return True
    def select_by_value(self, value):
        """
        列表选择展示多少条数据，10条/页、20条/页、30条/页、40条/页、50/页、60/页、70/页、80/页、90/页
        select标签下拉框通过value值选择,如10、20、30、40、50、60、70、80、90等
        """
        # self.forced_wait(*selector)
        try:
            time.sleep(0.5)
            element = self.driver.find_element('xpath',"//div[@id='layui-table-page1']//span[@class='layui-laypage-limits']//select")
            if element is not None:
                Select(element).select_by_value(value)
                # element_name = element.text
                logger.info(f"下拉框选择 '{value}'页成功")
        except Exception as e:
            logger.error(f"页面上无下拉框元素")
            self.get_windows_img()
            time.sleep(1)
            return True
    def select_by_visible_text(self, text, *selector):
        """
        select下拉框通过文本进行选择
        """
        try:
            element =self.driver.find_element(*selector)
            Select(element).select_by_visible_text(text)
            logger.info(f"下拉框选择 '{text}' 成功")
        except Exception as e:
            logger.error(f"下拉框选择失败")
            logger.error({e})
            self.get_windows_img()

    def upload_input_file(self, file_path, *selector):
        """
        input标签上传文件,往输入框输入绝对地址
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element.send_keys(file_path) #往输入框输入绝对地址
            logger.info(f"上传文件 '{file_path}' 成功")
        except Exception as e:
            logger.error(f"上传文件失败")
            logger.error({e})
            self.get_windows_img()

    def win32gui_upload_file(self, file_path):  #win32gui 是Windows系统下的一个自动化工具
        """
        win32gui上传文件,往输入框输入绝对地址
        """
        time.sleep(0.5)
        try:

            dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, str(file_path))  # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
            logger.info(f"上传文件 '{file_path}' 成功")
        except Exception as e:
            logger.error(f"上传文件失败")
            logger.error({e})
            self.get_windows_img()


    def clear(self, *selector):
        """
        清除输入框
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element.clear()
            logger.info("清除了输入框.")
        except Exception as e:
            logger.warning(f"清除输入框 '{e}' 失败")
            self.get_windows_img()

    def click(self, *selector):
        """
        点击元素
        """
        self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            element = self.driver.find_element(*selector)
            element_name = element.text
            element.click()
            logger.info(f"按钮 '{element_name}' 已被点击.")
        except Exception as e:
            element = self.driver.find_element(*selector)
            element_name = element.text
            logger.error(f"点击按钮' {element_name} '失败")
            logger.error(e)
            self.get_windows_img()

    def frame(self, *selector):
        """
        进入frame
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            element = self.driver.find_element(*selector)
            #element.switch_to.frame()
            self.driver.switch_to.frame(element)
            logger.info(f"进入iframe成功")
        except Exception as e:
            logger.error(f"进入iframe失败")
            logger.error(e)
            self.get_windows_img()


    def parent_frame(self, *selector):
        """
        返回上一层iframe,
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            #element = self.driver.find_element(*selector)
            self.driver.switch_to.parent_frame()
            logger.info(f"返回上一层iframe成功")
        except Exception as e:
            logger.error(f"返回上一层iframe失败")
            logger.error(e)
            self.get_windows_img()

    def default_content_frame(self, *selector):
        """
        从frame中切回主文档
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            #element = self.driver.find_element(*selector)
            self.driver.switch_to.default_content()
            logger.info(f"从frame中切回主文档成功")
        except Exception as e:
            logger.error(f"从frame中切回主文档失败，原因{e}")
            self.get_windows_img()

    def accept(self,*selector):
        """
        alert弹窗确认
        """
        try:
            result = EC.alert_is_present()(self.driver)
            if result:
                result.accept()
                logger.info(f"确认弹窗成功")
        except Exception as e:
            logger.error(f"确认弹窗失败,原因：{e}")
            self.get_windows_img()

    def accept_text(self,*selector):
        """
        alert弹窗获取文本
        """
        try:
            result = EC.alert_is_present()(self.driver)
            if result:

                return str(result.text)
            logger.info(f"获取弹窗文本成功")
        except Exception as e:
            logger.error(f"获取弹窗文本失败,原因：{e}")
            self.get_windows_img()

    def traverse_click(self, attribute, value, *selector):
        """
        遍历点击相同节点下的所有按钮
        """
        times = 0
        # 避免值属性位置不确定,取每一个值传入无序集合中
        self.forced_wait(*selector)
        try:
            elements = self.driver.find_elements(*selector)
            for element in elements:
                times = times + 1
                element.click()
                values = element.get_attribute(attribute)
                if value in values:
                    logger.info(f"循环点击第{times}个按钮:'{element.text}'成功.")
                else:
                    logger.error(f"循环点击第{times}个按钮:'{element.text}'失败!")
                    self.get_windows_img()
                time.sleep(0.5)
            logger.info("循环点击成功.")
        except Exception as e:
            logger.error(f"循环点击失败,原因:{e}")
            self.get_windows_img()

    def actionchains_click(self, *selector):
        """
        移动鼠标点击
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            element_name = self.get_element(*selector)
            ActionChains(self.driver).move_to_element(element).click(element).perform()
            logger.info(f"按钮 '{element_name}' 已被点击.")
            #self.sleep(1.5)
        except Exception as e:
            logger.error(f"移动鼠标点击按失败,原因:{e}")
            self.get_windows_img()

    def execute_script_click(self, *selector):
        """
        调用js点击
        """
        self.forced_wait(*selector)
        try:
            element = WebDriverWait(self.driver, 5, 1).until(EC.visibility_of_element_located(selector))
            element_name = self.get_element(*selector)
            self.driver.execute_script('arguments[0].click()', element)
            logger.info(f"调用JS,按钮 '{element_name}' 已被点击.")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"调用js点击按钮失败,原因:{e}")
            self.get_windows_img()

    def execute_script_get_text(self, *selector):
        """
        调用js获取文本
        """
        self.forced_wait(*selector)
        try:
            element = self.driver.find_element(*selector)
            self.driver.execute_script('arguments[0].value()', element)
            logger.info(f"文本内容已被获取.")
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"文本内容获取失败,原因:{e}")
            self.get_windows_img()

    def get_page_title(self):
        """
        获取网页标题
        """
        # noinspection PyBroadException
        try:
            logger.info(f"Current page title is {self.driver.title}")
            return self.driver.title
        except Exception as e:
            logger.warning(f"获取页面title失败,原因:{e}")
            self.get_windows_img()

    def get_wait_element(self, *selector):
        """
        找到显示等待的元素
        """
        self.forced_wait(*selector)
        # noinspection PyBroadException
        try:
            logger.info(f"找到 '{self.get_element(*selector)}' 按钮")
        except Exception:
            logger.error('找不到显式等待的元素')
            self.get_windows_img()

    def refresh_browser(self):
        # noinspection PyBroadException
        try:
            self.driver.refresh()
            logger.info("刷新网页成功")
            time.sleep(0.5)
        except Exception as e:
            logger.error("刷新网页失败")
            self.get_windows_img()

    def click_add(self):
        """
        点击新增按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            element = self.driver.find_element(By.XPATH,"//button[@data-type='add']")
            element.click()
            logger.info(f"新增按钮已被点击.")
        except Exception as e:
            logger.error(f"点击新增按钮失败,原因:{e}")
            self.get_windows_img()

    def click_inquire(self):
        """
        点击查询按钮
        """

        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//button[text()='查询']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[text()='查询']")
            # element.click()
            # logger.info(f"查询按钮已被点击.")
        except Exception as e:
            logger.error(f"点击查询按钮失败,原因:{e}")
            self.get_windows_img()

    def click_empty_inquire(self):
        """
        点击清空查询按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//button[text()='清空查询']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[text()='清空查询']")
            # element.click()
            # logger.info(f"清空查询按钮已被点击.")
        except Exception as e:
            logger.error(f"点击清空查询按钮失败,原因:{e}")
            self.get_windows_img()

    def click_determine(self):
        """
        点击确定按钮
        """
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//a[text()='确定']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//a[text()='确定']")
            # element.click()
            # logger.info(f"确定按钮已被点击.")
        except Exception as e:
            logger.error(f"点击确定按钮失败,原因:{e}")
            self.get_windows_img()

    def click_save(self):
        """
        点击保存按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//a[text()='保存']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//a[text()='保存']") #layui-layer-btn0
            # element.click()
            # logger.info(f"保存按钮已被点击.")
        except Exception as e:
            logger.error(f"点击保存按钮失败,原因:{e}")
            self.get_windows_img()

    def click_Cancel(self):
        """
        点击取消按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//a[text()='取消']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//a[text()='取消']")
            # element.click()
            # logger.info(f"取消按钮已被点击.")  //a[@class='layui-layer-ico layui-layer-close layui-layer-close1']
        except Exception as e:
            logger.error(f"点击取消按钮失败,原因:{e}")
            self.get_windows_img()
    def click_window_close(self):
        """
        点击弹窗的X按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',"//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//a[text()='取消']")
            # element.click()
            logger.info(f"点击弹窗的X按钮已被点击")
        except Exception as e:
            logger.error(f"点击弹窗的X按钮失败,原因:{e}")
            self.get_windows_img()
    def click_export(self):
        """
        点击导出按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//button[text()='导出']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[text()='导出']")
            # element.click()
            # logger.info(f"按钮导出已被点击.")
        except Exception as e:
            logger.error(f"点击导出按钮失败,原因:{e}")
            self.get_windows_img()

    def click_add_classify(self):
        """
        点击添加分类按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//button[@id='add-cate']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[@id='add-cate']")
            # element.click()
            # logger.info(f"按钮添加分类已被点击.")
        except Exception as e:
            logger.error(f"点击添加分类按钮失败,原因:{e}")
            self.get_windows_img()

    def click_upload_image(self):
        """
        点击上传图片按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//button[@id='upload']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[@id='upload']")
            # element.click()
            # logger.info(f"按钮上传图片已被点击.")
        except Exception as e:
            logger.error(f"点击上传图片按钮失败,原因:{e}")
            self.get_windows_img()

    def click_delete_image(self):
        """
        点击删除图片按钮
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//button[@id='del']")
            # time.sleep(0.5)  # 每次点击前都需要等待一下
            # element = self.driver.find_element(By.XPATH,"//button[@id='del']")
            # element.click()
            # logger.info(f"按钮删除图片已被点击.")
        except Exception as e:
            logger.error(f"点击删除图片按钮失败,原因:{e}")
            self.get_windows_img()

    def select_item_classification(self,text):
        """
        选择商品分类，形参填写例如：文具
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//label[text()='商品分类:']/..//input[@type='text']")
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',f"//dd[contains(text(),'-----{text}')]")
            logger.info(f"选择商品分类{text}成功")
        except Exception as e:
            logger.error(f"选择商品分类{text}失败,原因:{e}")
            self.get_windows_img()

    def select_suppliers(self,text):
        """
        选择商品供货商分类，
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            self.click('xpath',"//label[text()='商品供货商:']/..//input[@type='text']")
            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.click('xpath',f"//dd[text()='{text}']")
            logger.info(f"选择商品供货商分类{text}成功")
        except Exception as e:
            logger.error(f"选择商品供货商分类{text}失败,原因:{e}")
            self.get_windows_img()

    def input_start_time(self,text_time):
        """
        选择前时间，形参填写例如：2023-10-18 16:19:18
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:

            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.input(text_time, ('xpath',"//input[@id='start_time']"))
            logger.info(f"选择时间{text_time}成功")
        except Exception as e:
            logger.error(f"选择时间{text_time}失败,原因:{e}")
            self.get_windows_img()

    def input_end_time(self,text_time):
        """
        选择后时间，形参填写例如：2023-10-18 16:19:18
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:

            time.sleep(0.5)  # 每次点击前都需要等待一下
            self.input(text_time, ('xpath',"//input[@id='end_time']"))
            logger.info(f"选择时间{text_time}成功")
        except Exception as e:
            logger.error(f"选择时间{text_time}失败,原因:{e}")
            self.get_windows_img()
    def flip_page(self,input_nubmer):
        """
        通过输入页面进行翻页功能
        """
        #self.forced_wait(*selector)  # 每次点击前都需要显式等待一下
        try:
            total_quantity = (self.get_element(*self.public_element_total_quantity))
            number = int(''.join(filter(str.isdigit, total_quantity)))
            page_number = math.ceil(number/int(input_nubmer))
            if input_nubmer < page_number:
                logger.error(f"输入的页数{input_nubmer}大于总页数{page_number}")
                return False
            self.input(input_nubmer,('xpath',"// input[ @ value = '1']"))
            if WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(('xpath',f"//em[text()='{input_nubmer}']"))):
                return True
            return False


        except Exception as e:
            logger.error(f"翻页失败,原因:{e}")
            self.get_windows_img()

    """ 公共元素位置"""
    public_element_name_exist = ('xpath', "//div[contains(text(),'该名称已存在')]")
    public_element_required_no_null = ('xpath',"//div[contains(text(),'必填项不能为空')]")
    public_element_tel_mistake = ('xpath', "//div[contains(text(),'请输入正确的手机格式')]")
    public_element_no_data = ('xpath',"//div[text()='暂无数据！']")
    public_element_delete_succeed = ('xpath', "//div[contains(text(),'删除成功')]")
    public_element_add_succeed = ('xpath', "//div[contains(text(),'添加成功')]")
    public_element_revise_succeed = ('xpath', "//div[contains(text(),'修改成功')]")
    public_element_total_quantity = ('xpath',"//span[@class='layui-laypage-count']")
    """新增供货商弹窗定位"""
    public_element_delete_quantity= ('xpath',"//div[@class='layui-layer-title']")
    """删除确认弹窗定位"""
