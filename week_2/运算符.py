#coding utf-8
#Time : 2019-03-12 15:13

# 五种运算符：算数运算符 赋值运算符 比较运算符 逻辑运算符 成员运算符

# 算数运算符 + - * / % //
# %:表示取余
# //：表示地板除，取整数
# a=10
# b=3
# print(a%b)

a=0.1
b=0.3
c=0.2
print(a+b-c+a)   # 输出结果0.30000000000000004   # python是动态语言，精确度不定
# print('%.1f'%(a+b-c+a))   #浮点数取小数点后多少位：%.2f
print(round(a+b-c+a,1))   # 输出结果 0.3    #round取小数点精确度
# 判断奇偶数，可以用到模运算%  比如： x%2==0 表示是偶数


# 赋值运算符   = += -=
x=3
x+=2 #等同于x=x+2
x-=4 #等同于x=x-4
print(x)

# 比较运算符  == != > >= < <=
    # 运算结果是布尔值 True False
x=5
y=3
print(x>=y)  # 返回True

# 逻辑运算符  and or not
   # 运算结果是布尔值 True False
a=5
b=0
print(a and b)  #b代表假0，所以返回结果0
print(a>0 and b>0) #返回false
# and两边为真才为真
# or 只要有一边为真 就为真


# 成员运算符 in/not in
    # 运算结果是布尔值 True False