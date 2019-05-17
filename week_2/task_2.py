#coding utf-8
#Time : 2019-03-13 16:27

# 1、利用for循环， 完成1-10的整数数字相加和

# def add(a,b,c,d,e,f,g,h,i,j):
#     res=a+b+c+d+e+f+g+h+i+j
#     return res
# result=add(1,2,3,4,5,6,7,8,9,10)
# print(result)

#range函数表示有序数列
# sum=0
# for n in range(11):
#     sum+=n
# print(sum)


# 2、用嵌套for循环输出等边三角形（三个边均为5个*）
# for i in range(1,6):
#     for a in range(1,6-i):
#         print(" ",end="")   #end为print函数的默认参数，默认值为换行符，通过指定end参数的值，可以取消在末尾输出回车符，实现不换行
#     print("* "*i)
# 方法二：
for i in (1,2,3,4,5):
    print(' '*(5-i),end='')
    print('* '*i)



# 3、用嵌套for循环输出直角三角形（*）
# *
# **
# ***
# ****
# *****
#
# for i in range(1,6):
#     print(i*'*')



# 4、 有1、2、3、4这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？abc a!=b!=c
# nums=[]
# for n1 in range(1,5):
#     for n2 in range(1,5):
#         for n3 in range(1,5):
#             if n1 != n2 and n1 != n3 and n2 != n3:
#                 num=100*n1+10*n2+n3
#                 if num not in nums:
#                     nums.append(num)
# print(nums)





# 5、 输出99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,j*i),end='')    #\t：是Tab
#     print()

