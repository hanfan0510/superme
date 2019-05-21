# _*_ coding: utf-8  _*_ 
# @Time : 2019-04-30 02:28

# # 视频时间2019.4.19  视频编号49
# 延续 study_pymysql.py

import pymysql


class DoMysql:
    '''完成与Mysql数据库的交互'''

    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306  # mysql的默认连结端口是3306
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)  # 连结数据库
        self.cursor = self.mysql.cursor()  # 游标，主要用来记录

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()
