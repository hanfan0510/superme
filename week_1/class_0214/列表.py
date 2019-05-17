#coding utf-8
#Time : 2019-03-11 16:30

#列表 list[]
l=[1,'hello',True,(1,2,3,666),['python','java']]   # list类型
t=(1,'hello',True,(1,2,3,666),['python','java'])   # 元组tuple类型
print(l)

# 列表是有序可变类型
# l[3][1]='hf'   #执行会报错，l[3]是元组类型，不可变
# print(l)

l[4][1]='hf'   #可以执行，l[4]是list类型，可变
print(l)

# 列表和元组的可变性不是绝对的
t[-1][0]='hello python'    # t[-1]是list类型 所以是可变的
print(t)