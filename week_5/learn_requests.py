#coding utf-8
#Time : 2019-03-26 09:42
# 视频时间2019.3.12

'''
模拟客户端发送一个get和post请求
'''

import requests

class HttpRequest:
    def http_requests(self,url,param,method):
        if type(param)==str:
            param=eval(param)

        if method.lower() == "get":
            resp = requests.get(url,params=param)
            print(resp.text)
            return requests.get(url,params=param)

        else:
            return requests.post(url,data=param)

# 测试代码
if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    param = {'mobilephone':'18688773467','pwd':'123456'}
    resp = HttpRequest().http_requests(url,param,method='geT')
    # print(resp)



