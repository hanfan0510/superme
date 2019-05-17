#coding utf-8
#Time : 2019-03-13 11:37

# for循环 ：遍历循环

#  for循环语法：
#  for 变量名 in 数据：
#       #循环体
#
# L=['angelbaby','cindy',1.23]
# for item in L:                 #1）依次按顺序访问L里面的元素，有几个元素就会循环几次
#                                #2）在访问L里面的每一个元素的同时，把值赋值给item
#     print("Python大法好！")
#     print("item的值为：{}".format(item))

#======================================

#到底应该用哪个循环？
#如果你确定循环次数的话，就用for
#如果你不确定循环次数，而是要达到某个限制条件后才停止，用while

#=====题目==============================

#有一个空列表 s[],我们利用for循环 循环5次，每次询问一个人的名字，并且把名字加到列表里面去
#提醒，列表增加元素 用 列表名.append(值)
# s=[]
# for item in '12345':
#     name=input("name")
#     s.append(name)
# print(s)

# s={"name":"hanfan","age":22}
# for a in s.items():    #返回所有数据
#     print(a)
#
# s = {"name": "hanfan", "age": 22}
# for a in s.keys():  #返回key主键
#     print(a)
#
# s={"name":"hanfan","age":22}
# for a in s.values():   #返回values值
#     print(a)


#===========嵌套for循环======================

s=['sadless','toppy','sofary','summer']
#把s里面的每一个元素都打印出来
for a in s:
    print(a)
    for b in a:   #把a这个变量存的字符串里面的每一个元素都打印出来
        print(b)





