# from curses.ascii import isdigit
# import imp
# import math
# import sys
'''
# TODO: set的元素类型可以有哪些？？
sites1 = [{'name': '小明', 'age': 26}, {'name': '老王', 'age': 40},
          {'name': 'Jane', 'phoneNum': '16637649278'}]
print(sites1)
sites2 = [{'name': '小明', 'age': 26}, {'name': 'Tom', 'phoneNum': '13395631505'}, {
    'name': 'Jane', 'phoneNum': '16637649278'}]
# print(sites1-sites2) # 报错

# int(x [,base])   //将x转换为一个整数

print(int(3.14))

# float(x)      //将x转换到一个浮点数
x = 12
print(float(x))

# complex(real [,imag])    //创建一个复数

# str(x)      //将对象 x 转换为字符串
obj = {'name':'tt'}
str = str(obj)
print(str)
print(obj)

# repr(x)     //将对象 x 转换为表达式字符串
print(repr(obj))

# eval(str)   //用来计算在字符串中的有效Python表达式,并返回一个对象

# tuple(s)    //将序列 s 转换为一个元组

# list(s)     //将序列 s 转换为一个列表

# set(s)       //转换为可变集合

# dict(d)   //创建一个字典。d 必须是一个 (key, value)元组序列。

# frozenset(s)    //转换为不可变集合

# chr(x)    //将一个整数转换为一个字符

# ord(x)   //将一个字符转换为它的整数值

# hex(x)   //将一个整数转换为一个十六进制字符串

# oct(x)   //将一个整数转换为一个八进制字符串

num = 5
str = '6'
print(type(num))
print(type(str))
str = int(str)
print(ord("A"))
print(hex())

# List = [i for i in range(30) if i % 5 == 0]
# print(List)

l = ['A', 'B', 'C']
dic = {key:ord(key) for key in l}
print(dic)
ss = [1,1,1,1]
s = {i for i in ss}
print(s)

a = {'i':'1'}
b = {'i':'1'}
print(a!=b)


print(a)

x = 1.347
b = 6.56
a = math.modf(x)
# print("line1 \
# ... line2 \
# ... line3")
# print("\a")
# print("Hello \b    World!")


name= '强哥' #string类型
age=18 #int 整数类型
str1 = '我是%s,今年%d'%(name,age)
print(str1)

str2 = f'我是{name},今年{age}'
print(str2)1

# str1 = 'adsdwwwwTTT'
# print(str1.capitalize())
# print(str1.center(20,'-'))

str = "runoob\t12345\tabc"  
print('原始字符串:', str)
 
# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号:', str.expandtabs())

str1 = "Runoob example....wow!!!"
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 5))
# print (str1.index(str2, 10))

txt = "Google#Runoob#Taobao#Facebook"
 
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 2)
 
print(x)
str = "123abcrunoob321"
print (str.strip( '123' ))  # 字符序列为 12
tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Value : %s" %  tinydict.items())

tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Age': 'female' }
 
tinydict.update(tinydict2)
print ("更新字典 tinydict : ", tinydict)

tinydict.popitem()
print ( tinydict)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({'a':456})
print(thisset)
thisset.update([9,4],[5,6])  
print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
z = x.difference(y) 
print(x)
print(z)

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素
# print (next(it))
# print (next(it))
# print (next(it))
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ,")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(a)
print(id(a))
change(a)
print(a)

def printinfo( arg1, aarg2 ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
x=[row[0] for row in matrix]
print(x)

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))

list = [['name','age','phone'],['小红',25,'13395631505']]
# # dic1 = [[row[i] for row in list] for i in 2]

# b = ['小红',25,'13395631505']
# c=['小红1',25,'13395631505']
# print(b in list)
# print(c in list)

 
# print('命令行参数如下:')
# for i in sys.argv:
#    print(i)
 
# print('\n\nPython 路径为：', sys.path, '\n')
# import test
# test.print_func('nnnn')
# s = 'Hello, Runoob'
# str(s)
# for x in range(1,11):
#    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))
# table = {'Google': '56p', 'Runoob': 2, 'Taobao': 3}
# print('Google: {Google};{Taobao}'.format(**table))
f = open("./test.txt", 'rb+')


f.write(b'012345woza8')
str = f.seek(-3,2)
print(str)
# 关闭打开的文件
f.close()
import pprint, pickle
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

import os, sys
ret = os.access("./test.txt", os.X_OK)
print ("F_OK - 返回值 %s"% ret)

path = "/text"
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)
os.chdir( path )

import os, sys
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()
print(p.age)
print(dir(os))
'''
# from urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)
# import datetime
# now = datetime
# print(datetime)
# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}\t'.format(i,j,i*j),end=' ')
#     print()
# 斐波那契数列 1 2=1+1 3=2+1 5=3+2
# a=[]
# for i in range(0,10):
#     if i < 2:
#         a.append(i+1)
#     else:
#         a.append(a[i-1]+a[i-2])
# print(a)
# n1=0
# n2=1
# count=100
# print('{},{}'.format(n1,n2,),end=',')
# nt = n1+n2
# while nt<count:
#     nt = n2 + n1
#     n1 = n2
#     n2 = nt
#     print(nt,end=',')
# 阿姆斯特朗数 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
# print('请输入一个正整数：')
# num = int(input("请输入一个数字: "))
# n = len(str(num))
# print(n)
# def add(x, y):

#    return x + y

# def subtract(x, y):
#    """相减"""

#    return x - y

# def multiply(x, y):
#    """相乘"""

#    return x * y

# def divide(x, y):
#    """相除"""

#    return x / y

# # 用户输入
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")

# choice = input("输入你的选择(1/2/3/4):")

# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))

# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))

# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))

# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))

# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
# else:
#    print("非法输入")

# import datetime
# def getYesterday():
#     today=datetime.date.today()
#     oneday=datetime.timedelta(days=1)
#     yesterday=today-oneday
#     return yesterday

# # 输出
# print(datetime)
# params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# print(params.keys())
# # dict_keys(['server', 'database', 'uid', 'pwd'])
# print(params.values())
# # dict_values(['mpilgrim', 'master', 'sa', 'secret'])
# print(params.items())
# # dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
# [k for k, v in params.items()]
# # ['server', 'database', 'uid', 'pwd']
# [v for k, v in params.items()]
# # ['mpilgrim', 'master', 'sa', 'secret']
# ["%s=%s" % (k, v) for k, v in params.items()]
# # ['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']

# li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# for item in li:
#     print(item,li.count(item))
# 30 个人在一条船上，超载，需要 15 人下船。
# 于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
# people={}
# for x in range(1,31):
#     people[x]=1
# print(people)
# check=0
# i=1
# j=0
# while i<=31:
#     if i == 31:
#         i=1
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             print(i,'3333')
#             i+=1
#             continue
#         else:
#             check+=1
#             if check == 9:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue
# li = [i for i in range(1, 31)]
# i = 0
# p = []
# check = 0
# while i <= 30:
#     if i == 30:
#         i = 0
#     elif len(p) == 15:
#         p.sort()
#         print('下船人的编号列表为：', p)
#         break
#     else:
#         if li[i] in p:
#             i += 1
#             continue
#         else:
#             check += 1
#             if check == 9:
#                 p.append(li[i])
#                 check = 0
#             else:
#                 i += 1
#                 continue

# def main():
#     fish = 1
#     while True:
#         total, enough = fish, True
#         for _ in range(5):
#             if (total - 1) % 5 == 0:
#                 total = (total - 1)  //  5 * 4
#             else:
#                 enough = False
#                 break
#         if enough:
#             print(f'总共有{fish}条鱼')
#             break
#         fish += 1

# print(__name__)
# if __name__ == '__main__':
#     main()
# 初始化列表
# test_list_set = [ 1, 6, 3, 5, 3, 4 ]
# test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]
 
# print("查看 4 是否在列表中 ( 使用 set() + in) : ")
 
# test_list_set = set(test_list_set)
# if 9 in test_list_set :
#     print ("存在")
 
# print("查看 4 是否在列表中 ( 使用 count()) : ")
 
# if test_list_bisect.count(9) > 0 :
#     print ("存在")
# li = [ 1, 6, 3, 5, 3, 4 ]
# def sumli(li):
#     sum = 0
#     for i in li:
#         sum +=i
#     return sum
# print(sumli(li))
# print(sum(li))
# print(min(li))
# print(max(li))
# str = 'abcdefg'
# str = str[:1]+str[2:]
# print(str)
# def ff(str,num):
#     return str[:num] + str[num+1:];
# print(ff(str,2));
# print(ff(str,4));
# str = str.replace(str[1],'',1)
# print(str)

# string = "www.runoob.com"
# sub_str ="runoob"
# if sub_str in string:
#     print('存在')
# else:
#     print('不存在')
# test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4} 
# print(test_dict)
# # 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息
# removed_value = test_dict.pop('Taobao','') 
# print (removed_value)
# del test_dict['Zhihu']
# print(test_dict)
# import time
 
# a1 = "2019-5-10 23:40:00"
# # 先转换为时间数组
# timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
# print(timeArray)
# # 转换为时间戳
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)
 
 
# # 格式转换 - 转为 /
# a2 = "2019/5/10 23:40:00"
# print(a2)
# # 先转换为时间数组,然后转换为其他格式
# timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
# otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
# print(otherStyleTime)

import time
import datetime
 
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 6))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

name = input("输入你的名字: \n\n") 
  
lngth = len(name) 
l = "" 
  
for x in range(0, lngth): 
    c = name[x] 
    c = c.upper() 
      
    if (c == "A"): 
        print("..######..\n..#....#..\n..######..", end = " ") 
        print("\n..#....#..\n..#....#..\n\n") 
          
    elif (c == "B"): 
        print("..######..\n..#....#..\n..#####...", end = " ") 
        print("\n..#....#..\n..######..\n\n") 
          
    elif (c == "C"): 
        print("..######..\n..#.......\n..#.......", end = " ") 
        print("\n..#.......\n..######..\n\n") 
          
    elif (c == "D"): 
        print("..#####...\n..#....#..\n..#....#..", end = " ") 
        print("\n..#....#..\n..#####...\n\n") 
          
    elif (c == "E"): 
        print("..######..\n..#.......\n..#####...", end = " ") 
        print("\n..#.......\n..######..\n\n") 
          
    elif (c == "F"): 
        print("..######..\n..#.......\n..#####...", end = " ") 
        print("\n..#.......\n..#.......\n\n") 
          
    elif (c == "G"): 
        print("..######..\n..#.......\n..#.####..", end = " ") 
        print("\n..#....#..\n..#####...\n\n") 
          
    elif (c == "H"): 
        print("..#....#..\n..#....#..\n..######..", end = " ") 
        print("\n..#....#..\n..#....#..\n\n") 
          
    elif (c == "I"): 
        print("..######..\n....##....\n....##....", end = " ") 
        print("\n....##....\n..######..\n\n") 
          
    elif (c == "J"): 
        print("..######..\n....##....\n....##....", end = " ") 
        print("\n..#.##....\n..####....\n\n") 
          
    elif (c == "K"): 
        print("..#...#...\n..#..#....\n..##......", end = " ") 
        print("\n..#..#....\n..#...#...\n\n") 
          
    elif (c == "L"): 
        print("..#.......\n..#.......\n..#.......", end = " ") 
        print("\n..#.......\n..######..\n\n") 
          
    elif (c == "M"): 
        print("..#....#..\n..##..##..\n..#.##.#..", end = " ") 
        print("\n..#....#..\n..#....#..\n\n") 
          
    elif (c == "N"): 
        print("..#....#..\n..##...#..\n..#.#..#..", end = " ") 
        print("\n..#..#.#..\n..#...##..\n\n") 
          
    elif (c == "O"): 
        print("..######..\n..#....#..\n..#....#..", end = " ") 
        print("\n..#....#..\n..######..\n\n") 
          
    elif (c == "P"): 
        print("..######..\n..#....#..\n..######..", end = " ") 
        print("\n..#.......\n..#.......\n\n") 
          
    elif (c == "Q"): 
        print("..######..\n..#....#..\n..#.#..#..", end = " ") 
        print("\n..#..#.#..\n..######..\n\n") 
          
    elif (c == "R"): 
        print("..######..\n..#....#..\n..#.##...", end = " ") 
        print("\n..#...#...\n..#....#..\n\n") 
          
    elif (c == "S"): 
        print("..######..\n..#.......\n..######..", end = " ") 
        print("\n.......#..\n..######..\n\n") 
          
    elif (c == "T"): 
        print("..######..\n....##....\n....##....", end = " ") 
        print("\n....##....\n....##....\n\n") 
          
    elif (c == "U"): 
        print("..#....#..\n..#....#..\n..#....#..", end = " ") 
        print("\n..#....#..\n..######..\n\n") 
          
    elif (c == "V"): 
        print("..#....#..\n..#....#..\n..#....#..", end = " ") 
        print("\n...#..#...\n....##....\n\n") 
          
    elif (c == "W"): 
        print("..#....#..\n..#....#..\n..#.##.#..", end = " ") 
        print("\n..##..##..\n..#....#..\n\n") 
          
    elif (c == "X"): 
        print("..#....#..\n...#..#...\n....##....", end = " ") 
        print("\n...#..#...\n..#....#..\n\n") 
          
    elif (c == "Y"): 
        print("..#....#..\n...#..#...\n....##....", end = " ") 
        print("\n....##....\n....##....\n\n") 
          
    elif (c == "Z"): 
        print("..######..\n......#...\n.....#....", end = " ") 
        print("\n....#.....\n..######..\n\n") 
          
    elif (c == " "): 
        print("..........\n..........\n..........", end = " ") 
        print("\n..........\n\n") 
          
    elif (c == "."): 
        print("----..----\n\n")