#coding utf-8
#Time : 2019-03-15 16:35


#
# s='pyhtonppp'
# res=s.replace('p','@',1)  #替换  有返回值
                # 第一个参数：目标字符串；第二个参数是替换的新字符串；第三个是替换次数，不写默认全部替换

# res=s.split('p',2)  #切割 有返回值
                      #第一个参数：根据指定的字符进行切割；第二个参数：切割次数，不写默认全部切割
# s='   pyhtonppp   '
# res=s.strip()     #去除空白
                    # 默认去除头和尾的空格
                    #也能去掉指定的字符
# s='@@@pyht@@@onppp@@@@'
# res=s.strip('@')    #只能去掉头和尾
# print(s)

s='pyhTonPpp'
res=s.swapcase()   #大小写互换


print(res)





