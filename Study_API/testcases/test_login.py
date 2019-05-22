# _*_ coding: utf-8  _*_ 
# @Time : 2019-05-13 02:31

# 视频时间2019.4.16号

# 从配置文件读取数据登录

import unittest
from Study_API.common import contants
from Study_API.common import do_excel
from Study_API.common.http_request import HTTPRequest2
from ddt import ddt, data


@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUp(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_login(self, case):
        resp = self.http_request.request(case.method, case.data, case.url)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDown(cls):
        cls.http_request.close()
