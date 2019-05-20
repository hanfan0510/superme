# _*_ coding: utf-8  _*_ 
# @Time : 2019-03-30 23:09

## 1.break和continue的区别
# break是结束整个循环体，continue是结束单次循环


## 2.while和for循环的异同点
# for循环主要用在遍历中
# while循环主要用在条件表达式成立时，容易进入死循环


## 3.函数有哪些特性
# 函数名符合标识符的命名规则
# 具有独立功能的代码块
# 在需要的时候可以调用



## 4.Pycharm中Debug调试的Step Over(F8)、Step Into(F7)区别
## Step Over 在单步执行时，在函数内遇到子函数时不会进入子函数内单步执行，而是将子函数整个执行完再停止
## Step Into 单步执行，遇到子函数就进入并且继续单步执行


## 5.将列表[13, 20, 42, 85, 9, 45]翻转之后为[45, 9, 85, 42, 20, 13]的所有方法
# a = [13, 20, 42, 85, 9, 45]
# a.reverse()    # 方法一
# print(a)
# b = a[-1::-1]  # 方法二
# print(b)
# c = a[::-1]    # 方法三
# print(c)



## 6。将列表[13, 20, 42, 85, 9, 45]中的最大值为85取出
# a = [13, 20, 42, 85, 9, 45]
# max_num = 0
# for i in range(len(a)-1):
#     if max_num < a[i]:
#         max_num = a[i]
#     else:
#         continue
# print(max_num)



## 7.如果输入1~5，打印对应的“周一”~“周日”，如果输入的数字是6或7，打印输出“周末”
# 方法一：
# week_dic = {'1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周末','7':'周末'}
# while True:
#     week_input = input('请输入1-7的数字：')
#     if '0' < week_input <= '5':
#         print(week_dic[week_input])
#         continue
#     elif '0'< week_input <= '7':
#         print(week_dic[week_input])
#         continue
#     elif week_input == '0':
#         break
#     else:
#         print('输入有误，请重新输入！')
#     continue


# 方法二：
def which_day():

    """

    What day is today depending on your input number

    :return:

    """

    day_list = ['周一', '周二', '周三', '周四', '周五', '周末']

    day_num = 1

    while day_num:

        try:

            day_num = int(input('Please enter your number: '))

        except ValueError:  # 捕获输入非int类型时的异常

            print('类型输入有误，请重新输入数字！')

        else:

            if 0 < day_num < 8:

                if day_num < 6:

                    print('今天是{}'.format(day_list[day_num-1]))

                else:

                    print('今天是{}'.format(day_list[-1]))

            elif day_num == 0:

                break

            else :

                print('输入有误，请重新输入！')

which_day()


## 8.计算BMI指数
# height = float(input('请输入身高（m）：'))
# weight = float(input('请输入体重（KG）：'))
# BMI = weight / height**2
# print('BMI值为：%.2f'%(BMI),end=' ')
#
# if BMI <= 18.5:
#     print('过轻')
# elif BMI <= 25:
#     print('正常')
# elif BMI <= 28:
#     print('过重')
# elif BMI <= 32:
#     print('肥胖')
# elif BMI > 32:
#     print('严重肥胖')



## 9.登录程序
# username = input('请输入用户名：')
# password = input('请输入密码：')
# def login(a,b):
#     if a == username and b == password:
#         print('登录成功')
#     else:
#         print('用户名或密码错误')
# login('lemon','best')



