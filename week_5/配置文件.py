# _*_ coding: utf-8  _*_ 
# @Time : 2019-03-31 00:42


## 创建配置文件   .conf或者.cfg

from configparser import  ConfigParser

# 实例化类
cf = ConfigParser()

## 1。读取conf文件：文件路径，编码方式
cf.read("demo.conf",encoding="utf-8")

## 2。读取所有section  返回列表形式       ////sections区域
secs = cf.sections()
print(secs)     ##返回结果： ['db', 'excel']

## 3。获取某一个section下面的所有options
print(cf.options(secs[0]))   ## 返回结果：['db_name', 'db_user', 'db_password', 'db_port']

## 获取某一个section下面，某一个option具体值 用get
  # 得到的所有结果都是字符串
print(cf.get("db","db_user"))     ##//// 返回值：python15

## 如果想获取int类型的，cf.getint
old = cf.get('db','db_port')
print(type(old))   ## 返回： <class 'str'>
port = cf.getint('db','db_port')
print(type(port))  ## 返回：<class 'int'>








