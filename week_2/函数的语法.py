#coding utf-8
#Time : 2019-03-13 15:42

# 函数语法：
# def 函数名(参数1，参数2，参数3)    #小写字母  不同的字母和数字之间用下划线隔开
    #函数体
    #return

#参数类型：位置参数 默认参数 动态参数*args 关键字参数**kwargs
#参数个数：0到无数个

#一：
#return 是否有返回值   #不写return时，默认返回None

def say_hello():
    print("good morning!")
    return 888
# say_hello()

res=say_hello()
print(res)

#二：
# return后面只有一个值的时候，是什么类型的数据就会返回什么类型的数据
# 比如说return后面是整数，那么返回整数类型，如果是字符串 那么返回字符串类型

#三：
#如果return后面有多个值的时候，以元组的类型返回
# def say_hello():
#     print("good morning!")
#     return (1,2,3),{"name":"hanfan"}
# # say_hello()
#
# res=say_hello()
# print(res)
# #对say_hello()函数的结果 进行遍历
# for item in res:
#     print(item)

#四：
# return表示函数结束，return后面的代码都不会再执行了

# def add(a,b,c):
#     res=a+b+c
#     # print(res)
#     return res
# result=add(2,3,4)
# print(result)