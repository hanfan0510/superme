#coding utf-8
#Time : 2019-03-11 15:47

#元组 tuple()
#1 : 空元组  t=()
#2 : 元组里面只有一个数据时，要加一个逗号才会是元组类型 如：t=('hello',)，t即为元组类型
     #t=('hello')中，t为string类型
t=('hello',)
print(type(t))

#3 ： 元组里面的元素可以是任意类型，不同元素之间用逗号隔开
#4 ： 元组是有下标的，正序/反序限号都支持，取值方式同字符串
t=(1,0.03,'hello',True,(1,2,3,666,'python')) #0,1,2,3,4
# 单个取值
print(t[2])  #结果为hello
print(t[-1::-1])  #反序输出

#5 ：嵌套取值
#取出嵌套元组的666
print(t[4][3])
print(t[-1][3])
print(t[-1][-2])

#取出嵌套元组元组python的y
print(t[-1][-1][1])
print(t[-1][-1][-5])

#6 : 元组类型是不可变类型  不可改变元组的数据
# 如：t[0]='hello' 是不可以的，会报错 --> SyntaxError: invalid character in identifier


