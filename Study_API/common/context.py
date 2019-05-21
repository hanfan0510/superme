# _*_ coding: utf-8  _*_ 
# @Time : 2019-05-13 05:25

import re
from Study_API.common.config import config


def replace(data):
    data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'  # 井号表示查找字符的起始位置
    p = '#(.*?)#'  # ? 表示找到一个就截止   （）表示一个组的开始和结束

    while re.search(p, data):
        m = re.search(p, data)  # 如果没有查找到，返回None
        g = m.group(1)  # 只返回指定组的内容，返回：normal_user
        print(g)

        v = config.get('data', g)
        print(v)
        data = re.sub(p, v, data, count=1)

    return data
