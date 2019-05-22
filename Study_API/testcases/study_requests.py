# _*_ coding: utf-8  _*_ 
# @Time : 2019-04-13 21:52

# 听课视频在41号2019.4.9号的视频requests模块讲解和应用

import requests

'''
http请求的过程：
1、构造请求：请求方式（get、post），请求地址，请求参数
2、发起请求
3、返回响应
4、判断响应码，响应体
'''

# 测试地址：http://test.lemonban.com/futureloan/mvc/api/member/register

# # 注册接口
# param = {'mobilephone':'15011096051','pwd':'123456'}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register',params=param)    # 构造请求
# # 有返回值，所以要用变量resp接收  返回response的对象
#
# print('响应码：',resp.status_code)
# print('响应文本：',resp.text)
# print('响应头：',resp.headers)
# print('响应cookies：',resp.cookies)    # 响应cookies： <RequestsCookieJar[]>
# print('请求cookies：',resp.request._cookies)    # 请求cookies： <RequestsCookieJar[]>

# # 登录接口
param = {'mobilephone':'15011096051','pwd':'123456'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=param)    # 构造请求
                                                                # 如果是post请求，就用data传参
print('响应码：',resp.status_code)
print('响应文本：',resp.text)
print('响应头：',resp.headers)
print('响应cookies：',resp.cookies)  # 响应cookies： <RequestsCookieJar[<Cookie JSESSIONID=81A78D7D3E5BA6440249628D5526270F for test.lemonban.com/futureloan>]>
print('请求cookies：',resp.request._cookies)  # 请求cookies： <RequestsCookieJar[]>

#
# 充值接口
param = {'mobilephone':'15011096051','amount':'10'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=param,cookies = resp.cookies)    # 构造请求
                                                                                # cookies 从登录接口获取响应cookies；可以是字典，也可以是cookiejar

print('响应码：',resp.status_code)
print('响应文本：',resp.text)
print('响应头：',resp.headers)
print('响应cookies：',resp.cookies)
print('请求cookies：',resp.request._cookies)



