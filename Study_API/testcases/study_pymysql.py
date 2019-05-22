# _*_ coding: utf-8  _*_ 
# @Time : 2019-04-29 23:56

# 视频时间2019.4.19  视频编号49

## 学习pymysql

import pymysql

# 1,建立连结：数据库的连结信息
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306  # mysql的默认连结端口是3306
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)  # 连结数据库

# 2，新建一个查询页面
cursor = mysql.cursor()  # 游标，主要用来记录
# 3，编写sql
sql = 'select max(mobilephone) from future.member'
# sql='select * from future.loan limit 10'
# 4，执行sql
cursor.execute(sql)
# 5，查看结果
result = cursor.fetchone()  # 获取查询结果集里面最近的一条数据返回
# results=cursor.fetchall()  # 获取全部结果集
print(type(result), result)   # <class 'tuple'> ('18999999999',)
# 6，关闭查询窗口（游标）
cursor.close()
# 7，关闭数据库连结
mysql.close()


# 以上，可以封装成一个类，用来做数据库的交互  见do_mysql.py
