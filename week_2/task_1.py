#coding utf-8
#Time : 2019-03-13 09:13

# 简单登录
#
# a=input("请输入用户名：")
#
# if a=="hanfan":
#     b=input("请输入密码：")
#     if b=="123456":
#         print("登录成功！")
#     else:
#         print("用户名密码错误！")
# else:
#     print("用户名密码错误！")
#
# a=input("请输入用户名：")
# b=input("请输入密码：")
# if a=="hanfan" and b=="123456":
#     print("登录成功！")
# else:
#     print("用户名或密码错误！")



#字典
# a={"name":"hanfan",
#    "age":22,
#    "height":160}
# print(a["name"])
#
# #列表
# l=[1,2,3,"han",[3,4,5],{"name":"hanfan"}]
# print(l[-2][0])
#
# #元组tuple
# t=(1,23.4,(4,5))
# print(t[2][1])
#
# #运算符
# # 逻辑运算符 and or not
# # 赋值运算符 = += -=
# # 算术运算符 + - * / % //
# # 比较运算符 == > >= < <=
# # 成员运算符 in/not in
# a=(1,3,5,(2,5))
# print(2 in a)  # 返回False

# 判断成绩
score=int(input("请输入成绩："))
if score>=90:
    print("Very Good!!")
elif score>=80:
    print("good!")
elif score>=70:
    print("well")
elif score>=60:
    print("pass")
else:
    print("not pass")


