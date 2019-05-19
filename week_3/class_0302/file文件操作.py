# coding : utf-8
# @Time : 2019/3/18 0:42

# 文件的新建/读取/写入数据
#open() 新建文件的操作，主要讲新建.txt文件
    #open函数语法：open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
    #mode=r：只读

# file=open('test.txt','r+',encoding='utf-8')  #encoding为默认函数，文中含有汉字时需要加encoding='utf-8'
# # file=open('../class_0218/python15','r+',encoding='utf-8')  #不在同一路径下时，添加上一级路径
# res=file.read()  #获取全文
# # res=file.read(5)  #获取的字符的长度
# print(res)
# file.write('你好，测试')  #在文件末尾写入
# file.close()  #最后一定记得关闭文件


#r   只读  如果文件里含有中文，需要加encoding='utf-8'
#r+  读写  可以进行读写操作  写入的内容在文件的末尾
          #1：先读在写，直接写在文件内容末尾
          #2：直接写，从头开始逐字覆盖写
          #3：写在指定位置，用tell()和seek（）函数 -----此处了解

#w   只写 清空写：如果文件存在，则清空写；如果文件不存在，则会新建一个文件再去写
# file=open('test.txt','w',encoding='utf-8')   #清空test.txt文件，，如果test.txt文件不存在则新建
# file.write('丢丢的班级逃课太严重啦！')   #执行后，test.txt文件的内容被写为"丢丢的班级逃课太严重啦！"
# file.close()

#w+  读写  也是清空写：如果文件存在，则清空写；如果文件不存在，则新建一个再写
# file=open('test.txt','w+',encoding='utf-8')
# file.write('我在学习python')
# print(file.read())  #读的时候，是根据光标位置来读，写完之后光标在最末尾，所以读不到内容
# file.close()

#a   追加  只能追加，不能读，不会清空
     #如果文件存在，直接追加，如果文件不存在，直接新建一个文件再写
# file=open('test.txt','a',encoding='utf-8')
# # file.read()   #a只追加，所以此句会报错：io.UnsupportedOperation: not readable
# file.write('丢丢的班级逃课太严重了！')
# file.close()

#a+  读追加
file=open('test.txt','a+',encoding='utf-8')
file.seek(0,0)  #seek函数，将光标定位在开头位置，所以下面语句可以读取到数据
print(file.read())
file.write('99999')
file.close()

