# _*_ coding: utf-8  _*_ 
# @Time : 2019-05-12 23:33

# 课程视频在2019.4.20号，课程编号51后半部分开始

#  正则表达式的学习

'''
正则表达式使用单个字符串来描述、匹配一系列符合某个句法规则的字符串
正则表达式一般包含原本字符和元字符两种
（）表示一个组，通俗的理解就是可以用它来标记一个表达式组的开始和结束
. 可以匹配任意单个字符，汉字、字母、符号、数字（注意：是单个）
\d 匹配任意单个数字
+ 至少匹配一次
？ 最多匹配一次
* 匹配0次或多次
'''

import re
from Study_API.common.config import config

# data = '{"mobilephone":"normal_user","pwd":"normal_pwd"}'

# # 原本字符
# p = 'normal_user'  # 正则表达式
# m = re.search(p, data)
# print(m)


# 元字符
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'  # 井号表示查找字符的起始位置
# p='#.*#'  # .表示任意单个字符，*表示匹配多次
# 返回 <re.Match object; span=(16, 50), match='#normal_user#","pwd":"#normal_pwd#'>

p = '#(.*?)#'  # ? 表示找到一个就截止   （）表示一个组的开始和结束
# 返回 <re.Match object; span=(16, 29), match='#normal_user#'>

# ms = re.findall(p, data)  # findall 查找全部 ，返回列表
# 返回 ['normal_user', 'normal_pwd']
# print(ms)

# m = re.search(p, data)  # 如果没有查找到，返回None
# # print(m)
# print(m.group(0))  # 返回表达式和组里面的内容，返回：#normal_user#
# g = m.group(1)  # 只返回指定组的内容，返回：normal_user
# print(g)
#
# v = config.get('data', g)
# print(v)
# data_new = re.sub(p,v,data,count=1)
# print(data_new)


# 如果匹配多次，替换多次，用循环解决
while re.search(p, data):
    m = re.search(p, data)  # 如果没有查找到，返回None
    g = m.group(1)  # 只返回指定组的内容，返回：normal_user
    print(g)

    v = config.get('data', g)
    print(v)
    data = re.sub(p, v, data, count=1)
print("最后替换后的data：",data)


