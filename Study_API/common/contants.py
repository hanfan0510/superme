# _*_ coding: utf-8  _*_ 
# @Time : 2019-04-28 23:52

import os

case_dir = os.path.abspath(__file__)
print(case_dir)  # /Users/hanfan/PycharmProjects/class_base/Study_API/common/contants.py

base_dir = os.path.dirname(os.path.dirname(case_dir))
print(base_dir)  # /Users/hanfan/PycharmProjects/class_base/Study_API

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')  # 路径合并
print(case_file)  # /Users/hanfan/PycharmProjects/class_base/data/cases.xlsx

global_file = os.path.join(base_dir, 'config', 'global.conf')  # 路径合并
print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')  # 路径合并
print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')  # 路径合并
print(test_file)
