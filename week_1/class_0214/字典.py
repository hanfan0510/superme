#coding utf-8
#Time : 2019-03-12 11:24

#  字典 dict--dictionary {}

# 1:可以有空字典dict{}
# d={}
# print(type(d))

# 2:字典的组成{key:value} 键值对  不同的键值对之间用逗号隔开
# key：int,float,boolean,str,tuple---key不可变
# value：int,float,boolean,str,tuple,list,dict----value可变，可以是任意类型
# 一般用字符串 ''  ""   一般用""较多

# d={1:'我',
#    0.02:'爱',
#    True:'罗',
#    (1,2,3):"hello"}
# print(d)

d={
    "name":"柠檬班",
    "class_name":"python_15",
    "score":[99,67,87],
    "height":{'张三':180,'李四':178}
}
print(d)

# 3：字典取值  字典名[key]
print(d["score"])

# 4 ：嵌套取值

print(d["height"]["李四"])   #取值height字典里的李四的身高
print(d["score"][0])    #取值score元组的第一个元素

# 5：字典也是可变无序数据类型
d["height"]["李四"]=187
print(d)
