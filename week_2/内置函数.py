#coding utf-8
#Time : 2019-03-14 16:45
# print()  #print函数print(self, *args, sep=' ', end='\n', file=None)：*args动态参数，不定多个；sep=' '返回参数用空格隔开
                             #end='\n' 换行

#capitalize  首字母大写
# s='pythoyn'
# res=s.capitalize()     //首字母大写
# res=s.count('y',1,6)      #统计子字符串出现的次数   count(self, sub, start=None, end=None)  //sub:要搜索的子字符串
# res=s.find('y',2,6)   #查找最近的索引位置  如果没找到，返回-1
# res=s.index('y')   #与find函数一样，只不过没找到时会报错ValueError
# res=s.islower()  #判断所有字符串是否是小写，如果都是小写返回True，否则返回False
# res=s.isupper()  #判断所有字符串是否是大写，如果都是大写返回True，否则返回False
# res=s.upper()  #将字符串全部转换为大写
# res=s.lower()  #将字符串全部转换为小写
# s=input("请输入数字：")
# res=s.isdigit()  #返回bool，判断是否是纯数字
# res=s.isdecimal()  #判断是否是十进制的数
s='pythoyn'
res='@'.join(s)  #拼接，join参数必须是可迭代的数据类型（字符串，元组，列表，字典），返回结果为：p@y@t@h@o@y@n

print(res)
