# print('hello python')

# print(type(3))
#
# a=300
# b='我爱北京天安门'
# print(len(b))
# print(type(b))
# print(b[-1])
# print(b[1:7:2])
# print(b[::-1])
# print(b[-1::-1])
#
##————————————————第二节课——————————————##

#格式化输出
#索引 index

name='丫头'
age=22
salary='9000'
height='168'
print('有一个学生名叫'+name+',她今年'+str(age)+'岁'+'，薪资是'+salary)

print('有一个学生名叫%s,她今年%d岁,薪资是%s'%(name,age,salary))

#{}format的使用
print('有一个学生名叫{},她今年{}岁,薪资是{}'.format(name,age,salary))

#三引号的使用
print('''
有一个学生名叫%s,
她今年%s岁,
薪资是%s'''%(name,age,salary))
