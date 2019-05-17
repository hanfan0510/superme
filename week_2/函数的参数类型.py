#coding utf-8
#Time : 2019-03-14 11:50


#参数类型：位置参数 默认参数 动态参数*args 关键字参数**kwargs

# def add(x,y):     # 调用函数的时候传参 ----形参/位置参数
#     print('x的值是',x)
#     print('y的值是',y)
#     return x+y
#
# res=add(2,4) #调用函数的时候传的参数--实参
#              #默认按顺序赋值
# #res2=add(y=9,x=6) #指定赋值
# print("函数结果为：{}".format(res))


# 默认参数：在定义函数的时候，给某个参数设置默认值
# def add(x,y=9):    #位置参数必须在默认参数之前
#     print('x的值是', x)
#     print('y的值是', y)
#     return x + y
# res=add(6)   #默认值y可传可不传
# print(res)


# 动态参数 *args arguments复数  指定多个----不定长参数
# def add(*args):  #参数传递到函数内部  会把所有对参数存储到一个元组
#                  #args是变量名，也可以命名a，b
#     print('数据类型：',type(args))
#     print(args)
#     #遍历args函数，对每个参数求和
#     sum=0
#     for item in args:   # item是变量名，可以是其他名字，如a，b
#         sum+=item
#     print('求和结果为：',sum)
# add(3,4,6,7,8,90,34)


# 关键字参数 **kwargs-----key word arguments
# 参数传进去后变成了一个字典 kwargs  指定key value
# def student_info(**kwargs):
#     print(kwargs)
#
# student_info(name='hanfan',age=28)



#  * 解包
#======调用参数时加*，表示解包，脱一层括号===================
# def add(*args):
#     print('args的值',args)
# t=[[1,2],[3,4]]
# add(t)  #返回([[1, 2], [3, 4]],)是一个含有一个元组的元组
# add(*t) #返回([1, 2], [3, 4])是一个含有两个元素的元组，脱掉了最外面一层的[]

# **kwargs
def student_info(**kwargs):
    print(kwargs)
k={'name':'han','age':18}

student_info(age=18,name='hf')  #返回字典类型{'age': 18, 'name': 'hf'}
# student_info(k)     #这样写会报错
student_info(**k)     #这样可以，返回{'name': 'han', 'age': 18}
student_info(info=k)  #这样也可以，返回{'info': {'name': 'han', 'age': 18}}