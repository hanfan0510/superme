# _*_ coding: utf-8  _*_ 
# @Time : 2019-05-13 03:05

# 视频时间 2019.4.16

import configparser
from Study_API.common import contants


class ReadConfig:
    '''
    完成配置文件的读取
    '''

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 如果开关打开，使用online的配置
            self.config.read(contants.online_file)
        else:  # 如果开关关闭，读取test的配置
            self.config.read(contants.test_file)

    def get(self, section, option):
        return self.config.get(section, option)

config=ReadConfig()


if __name__ == '__main__':
    config = ReadConfig()
    print(config.get('api', 'pre_url'))
