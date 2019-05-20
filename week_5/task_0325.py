#coding utf-8
#Time : 2019-03-27 10:58


# 1.定义两个字典用于表述你的个人信息===================================

# dict_1 = {'姓名':'hanfan','性别':'女','年龄':18,'身高':161.1}
# dict_2 = {'性格':'开朗','爱好':'singing','座右铭':'学而不思则罔'}

# a 字典合并
## 方法一
# res=dict(list(dict_1.items())+list(dict_2.items()))
# print(res)

## 方法二
# d=dict_1.copy()
# d.update(dict_2)
# print(d)

# b 修改年龄
# dict_1['年龄']=20
# print(dict_1)

# c 座右铭
# print(dict_2['座右铭'])

# d 字典支持序列类型查询，修改操作



# #请写出if判断语句的格式============================================
# if 判断条件:
# 	条件成立时要做的事情
# else:
# 	不满足条件时要做的事情




# # 3.求三个整数中的最大值=====================================
# number1 = int(input('请输入第一个数：'))
# number2 = int(input('请输入第二个数：'))
# number3 = int(input('请输入第三个数：'))
# if number1 <= number2:
#     if number2 <= number3:
#         print(number3)
#     else:
#         print(number2)
# else:
#     if number1 >= number2:
#         if number1 >= number3:
#             print(number1)
#         else:
#             print(number3)
#     else:
#         print(number1)
#



## 4.判断是否为闰年===============================================
# year = int(input('请输入年：'))
# if year%4==0 and year%100 !=0 :
#     print('{}年是闰年'.format(year))
# elif year%400 ==0:
#     print('{}年是世纪闰年'.format(year))
# else:
#     print('{}年不是闰年'.format(year))



## 5.分别使用for和while打印九九乘法表===============================

## for循环
# for i in range(1,10):
#     for j in range(1,i+1):
#         sum=j*i
#         print('{}*{}={}'.format(j,i,sum),end='\t')
#     print()


## while循环
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         sum=j*i
#         print('{}*{}={}'.format(j,i,sum),end='\t')
#         j+=1
#     i+=1
#     print()


## 7.使用if语句完成剪刀石头布游戏======================================
# a=0
# b=0
# c=0
# import random
# while True:
#     while True:
#         human_fist = int(input('请出拳：石头（1）／剪刀（2）／布（3）：'))
#         if human_fist in [1,2,3]:
#             break
#         else:
#             continue
#
#     pc_fist = random.randint(1,3)
#     ## 人赢
#     if (human_fist==1 and pc_fist ==2) or (human_fist==2 and pc_fist == 3) or (human_fist ==3 and pc_fist==1):
#         print('电脑出拳：{}'.format(pc_fist))
#         print('用户赢！')
#         a+=1
#     ## 电脑赢
#     elif (pc_fist==1 and human_fist ==2) or (pc_fist==2 and human_fist == 3) or (pc_fist ==3 and human_fist==1):
#         print('电脑出拳：{}'.format(pc_fist))
#         print('电脑赢！')
#         b+=1
#     ## 平局
#     else:
#         print('电脑出拳：{}'.format(pc_fist))
#         print('平局')
#         c+=1
#     d=input('退出请按n，继续请按任意键')
#     if d=='n':
#         break
#     else:
#         continue
# print('用户赢{}次，电脑赢{}次，平局{}次'.format(a,b,c))


## 8、 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（小的数字排前面，大的排后面）===================

a = [1,7,4,89,34,2]
for i in range (0,len(a)):
    for j in range (0,len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)


