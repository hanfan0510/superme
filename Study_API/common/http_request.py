# _*_ coding: utf-8  _*_ 
# @Time : 2019-04-16 00:25

# 2019.4.12号课程

# 学习request方法
# 一键规范代码的快捷键command+option+L/ctrl+alt+L

import requests
from Study_API.common.config import config

'''
两种传递cookies的方式
1，单独的session，把上一个请求的返回的cookies指定传递到下一个请求的入参cookie当中
2，使用同一个session，就会自动传递cookie。
'''


# class HTTPRequest():
#     '''
#     使用这个类的request方法去完成不同的HTTP请求，并且返回响应结果
#     '''
#     # ======== 下面方法是第一种，传cookies的方法 ==============================================
#     def request(self, method, data, url, json=None, cookies=None):
#         method = method.upper()
#         if method == 'GET':
#             resp = requests.get(params=data, url=url, cookies=cookies)
#         elif method == 'POST':
#             if json is not None:
#                 resp = requests.post(url=url, json=json, cookies=cookies)
#             else:
#                 resp = requests.post(data=data, url=url, cookies=cookies)
#         else:
#             print('UN-supposed method')
#         return resp
#
# if __name__ == '__main__':
#     param = {'mobilephone': '15011096051', 'pwd': '123456'}
#     url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
#     httprequest = HTTPRequest()
#     # 调用登录
#     resp = httprequest.request('gET', data=param, url=url)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#
#     # 调用充值
#     params = {'mobilephone': '15011096051', 'amount': '10'}
#     url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
#     resp = httprequest.request('post', data=params, url=url, cookies=resp.cookies)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)

# ======== 上面方法是第一种，传cookies的方法 ==============================================


# # ===== session的简单介绍 =======
# session = requests.sessions.session()
#
# # 登录
# param = {'mobilephone': '15011096051', 'pwd': '123456'}
# url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# resp = session.request('GET', url=url, params=param)
# print(resp.status_code)
# print(resp.text)
# print(resp.cookies)
#
# # 充值
# params = {'mobilephone': '15011096051', 'amount': '10'}
# url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# resp2 = session.request('POST', url=url, params=params)  # 不用传cookies
# print(resp2.status_code)
# print(resp2.text)
# print(resp2.cookies)
# session.close()  # session会话关闭


# ====== session的简单介绍结束 =======


# ======== 下面的方法是第二种，调用session方法，不用传cookies ==============================

class HTTPRequest2():
    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, data, url, json=None):
        method = method.upper()  # 全部转为大写

        '''将从Excel读取的字符串类型的data强制转换为字典类型'''
        if type(data) == str:
            data = eval(data)

        # 拼接URL
        url = config.get('api', 'pre_url') + url

        if method == 'GET':
            resp2 = self.session.request(method=method, params=data, url=url)  # ///data
        elif method == 'POST':
            if json is not None:
                resp2 = self.session.request(method=method, url=url, json=json)
            else:
                resp2 = self.session.request(method=method, url=url, data=data)
        else:
            print('UN-supposed method')
        return resp2

    def close(self):
        self.session.close()


if __name__ == '__main__':
    params = {'mobilephone': '15011096051', 'pwd': '123456'}
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    httprequest2 = HTTPRequest2()
    resp2 = httprequest2.request('get', data=params, url=url)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)

    # # 充值
    # params = {'mobilephone': '15011096051', 'amount': '10'}
    # url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    # resp2 = httprequest2.request('POST', data=params, url=url)  # 不用传cookies
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)
