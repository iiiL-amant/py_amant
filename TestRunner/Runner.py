# _*_ coding:utf-8 _*_
import sys
import os
import requests
import unittest
import time
import json

# 找到根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加进根目录
sys.path.append(root_path)

from framework.logger import Logger
from framework.browser_info import Browser_Info

logger = Logger(logger="用例失败成功情况").get_log()
get_browser_info = Browser_Info()
from Python_HTMLTestReportCN import HTMLTestReportCN

chrome_driver_path = os.path.join(os.path.join(root_path, 'tools'), 'chromedriver.exe')
report_path = os.path.join(root_path, 'test_report')
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

#RobotKeys_file = os.path.join(os.path.join(root_path, 'config'), 'robot_keys.json')  # 企业微信机器人的keys的json文件
HtmlFile = os.path.join(report_path, now_time + "-test.html")

#with open(RobotKeys_file, encoding='utf-8') as file1:
    #robot_keys_json = json.load(file1)

#keys_list = [robot_keys_json["git_update"], robot_keys_json["test_group"]]  # 保存为企业微信机器人的keys的列表
"""class MyTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testcase_class):
        # 调用父类的获取“测试方法”函数
        test_names = super().getTestCaseNames(testcase_class)
        # 拿到测试方法list
        testcase_methods = list(testcase_class.__dict__.keys())
        # 根据list的索引对testcase_methods进行排序
        test_names.sort(key=testcase_methods.index)
        # 返回测试方法名称
        return test_names
"""
if __name__ == '__main__':
    with open(HtmlFile, 'wb') as file1:
        print(os.path.abspath(__file__))
        suites = unittest.TestLoader().discover(
            os.path.join(root_path, 'test_suites'))
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=file1,
            title='Ui_Auto_测试报告',
            description=u'执行情况',
            tester='QA',
        )
        runner.run(suites)

    #test_count = HTMLTestReportCN._TestResult()
    # for keys in keys_list:
    #     requests.post(
    #         url=f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={keys}',
    #         headers={'Content-Type': 'application/json;charset=UTF-8'},
    #         json={
    #             "msgtype": "markdown",
    #             "markdown": {
    #                 "content": f"UI自动化测试结果:\n"
    #                            f"成功的用例数: {test_count.get_count()[0]}\n"
    #                            f"失败的用例数: {test_count.get_count()[1]}\n"
    #                            f"错误的用例数：{test_count.get_count()[2]}\n"
    #                            f"ui测试的用例总数：{test_count.get_count()[0] + test_count.get_count()[1] + test_count.get_count()[2]}\n"
    #                            f"ui测试地址：[{get_browser_info.get_url()}]({get_browser_info.get_url()})\n"
    #                            f"ui测试报告地址: [10.1.1.156/ui-auto-test/{now_time}-test.html](10.1.1.156/ui-auto-test/{now_time}-test.html)"
    #             }
    #         }
    #     )
