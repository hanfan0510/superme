#coding utf-8
#Time : 2019-03-13 10:11

# 判断成绩if
# score=int(input("请输入成绩："))
# if score>=90:
#     print("Very Good!!")
# elif score>=80:
#     print("good!")
# elif score>=70:
#     print("well")
# elif score>=60:
#     print("pass")
# else:
#     print("not pass")

#while循环&for循环&嵌套循环

#=====while循环====================
#语法：while 条件表达式：  #条件表达式同if---->本质：布尔值：逻辑运算符、比较运算符、成员运算符
        #循环体

#风险：容易进入死循环
#为了避免进入死循环：
# 1）while后面不要是永真式，那么while后面的表达式的值是要变化的

# x=1  #设定一个变量x，初始值1
# while x<5:
#     x = x + 1
#     print(x)

# 2)如果while后面是永真式，那么可以永break或continue组合的方法来防止进入死循环
# break 终止循环  continue结束本轮循环，继续下一轮循环

# a=0
# while 1:  #1 此处1表示永真
#     a = a + 1
#     if a<3:
#         print("python")
#         continue
#     else:
#         break
#

#=====作业题============================
#有一个空列表 s[],我们利用while循环 循环5次，每次询问一个人的名字，并且把名字加到列表里面去
#提醒，用 列表名.append(值)
s=[]
a=0
#方法一：
# while 1:
#     if a<5:
#         name=input("name")
#         s.append(name)
#         a+=1
#         print(s)
#         continue
#     else:
#         break

#方法二：
# while a<5:
#     s.append(input('请输入第{}个人的名字：'.format(a+1)))
#     a+=1
# print(s)

#方法三：
# while a<5:
#     name=input("请输入姓名：")
#     s+=name
#     a+=1
# print(s)

#方法四：
while len(s)<5:
    name=input("姓名：")
    s.append(name)
print(s)

