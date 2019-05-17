#coding utf-8
#Time : 2019-03-12 14:37

# 利用input函数，获取一个日期，格式如20190214
# 对日期输出：2019年2月14日  这个字符串到控制台

date=input("请输入日期：")
print("{}年{}月{}日".format(date[:4],date[4:6],date[6:]))
print(date[:4]+"年"+date[4:6]+"月"+date[6:]+"日")



