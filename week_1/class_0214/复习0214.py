#coding utf-8
#Time : 2019-03-12 09:17

# 格式化输出
name='张三'
age=22
height=170
# print('python15期班有一个学生名叫'+name+'，她今年'+str(age)+'岁'+',身高'+str(height))
# print('python15期班有一个学生名叫%s，她今年%d岁,身高%s'%(name,age,height))
# {}format
# print('python15期班有一个学生名叫{}，她今年{}岁,身高{}'.format(name,age,height))

# 元组 tuple()  元组不可变，元组里面内容可以是任意类型
# t=('hello',12,{'hello',12},(1,'python'))
# print(t)
# 单个取值
# print(t[-1])
# 切片取值
# print(t[3][1][::-1])
# 元组是不可变类型

#列表 list []
l=[1,2,'hello',(3,4),{'python,java'},[1,2,3]]

print(l[5][2])

# 字典 dic{key:value}---字典是无序的，所以没有索引
d={'name':'hf',
'age':22,
'height':'169'}
print(d)
print(d['name'][::-1])


