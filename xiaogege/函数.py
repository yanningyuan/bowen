#/usr/bin/env python
# -*- coding:utf-8 -*-
# 函数  具有某种功能可重复使用的代码块
#函数名规则和变量名规则一样
#格式   def  函数名():
#              执行语句
# def jiujiu():
#      for i in range(1,10):
#          for j in range(1,i+1):
#              print('{}*{}={}'.format(i,j,i*j),end='\t')
#          print()
# jiujiu()

#函数的传参
# #1.必须参数
# def jiujiu(x):
#      for i in range(1,x):
#          for j in range(1,i+1):
#              print('{}*{}={}'.format(i,j,i*j),end='\t')
#          print()
# jiujiu(4)
#2.默认参数
# def jiujiu(x=7):
#      for i in range(1,x):
#          for j in range(1,i+1):
#              print('{}*{}={}'.format(i,j,i*j),end='\t')
#          print()
# jiujiu()

#3.可变长参数  参数前加星号
# def aaa(*a):    # 将所有元素变成一个元组传入
#     print(a)
# aaa()
# def aaa(**kwargs)   # 接收的只能是键值对
#     print()

#
# def jiujiu(*a):
#     for j in a:
#      for i in range(1,j):
#          for j in range(1,i+1):
#              print('{}*{}={}'.format(i,j,i*j),end='\t')
#          print()
# jiujiu(3,4,5)

#函数的作用域
# a=123
# def aaa():   #在函数外面的变量属于全局变量
# #    global a  #将局部变量变为全局变量
#     a=999
#     print(a)  #函数中的变量属于局部变量
# aaa()
# print(a)

# return   1.函数的结束语
#          2.讲结果返回给调用者





# def aaa():
#     b = 0
#     for i in range(2, 101):
#         for j in range(2, i + 1):
#             a = i % j
#             if a == 0:
#                 break
#         if i == j:
#             b += j
#     print(b)
#     return b
# aaa()
# print(aaa())
# #print(aaa()+1)


#lambda   匿名函数  用来定义函数的

#格式：函数名  = lambda : 表达式

# aa=lambda : 3+4
# bb=lambda x,y : x-y
# print(bb(5,3))


#计算器，两个数之间的加减乘除
# aa=lambda x,y:x+y
# b=lambda x,y:x-y
# c=lambda x,y:x*y
# d=lambda x,y:x//y
# a=input('>')
# a=a.split(',')
# if '+' in a:
#     print(aa(int(a[0],int(a[2]))))
# if '-' in a:
#     print(b(int(a[0],int(a[2]))))

#列表推导式  将语句放在列表中，产生的结果变成列0表的元素
# a=[]
# for i in range(10):
#     if i>5:
#         a.append(i)
# b=[x for x in range(10) if x>5]
# print(a)
# print(b)

#  python中的内置函数
#  max(a)  # 列表中最大的
#print(min(a))  #列表中最小的

# a=100
# print(hex(a))    #  将十进制转化为十六进制
# print(oct(a))    #  将十进制转化成八进制
# print(bin(a))    # 将十进制转换成二进制
# print(int(0o144))  #将其他进制数转换成十进制
#

# a,b=divmod(16,16)  #  整除求余
# print(a,b)

# 对文件的操作  open() 函数
# 格式  open('文件名','权限'，'编码方式')
# 文件名：如果不加路径，表示的是当前目录下的文件   如果此目录下有这个文件，
# 就操作这个文件，如果没有就创建
# 如果有路径的话要在路径上加上双斜杠，表示不转义或者在路径前边加上小写r
# 权限：代码对文件的操作权限  w--写的权限 r--读的权限  a--追加的权限
#a='''三个引号可添加
#很多行
#'''
# a='''qwe
# qwrewq
# qwe
#
# qwrwq
# qwre
# wqr
# '''
# #wqrq
# qwrwq
# qwr

#afrf
#ewafr
# #'''
# f=open(r'C:\Users\小哥哥\Desktop\a.txt','r',encoding='utf-8')  #打开一个空的文件
# f.write('同桌大笨蛋'+'\n')
#write写入的内容只能是字符串
# f.write(a)
# f.read() #读取文件中所有内容，结果是字符串类型
# print(f.read())
# f.readlines()
# print(f.readlines()) #读取文件中所有内容结果是列表
#f.readline()   每次只读取文件中的一行，第一次读第一行，第二次读第二行，自己有累加的功能
#追加  a  write具备不换行的功能



# for i in range(1,10):
#    for j in range(1,i+1):
#        f.write(' {}*{}={} '.format(i,j,i*j))
#    f.write('\n')

# f.write('\n'+a)
# f.write('\n'+'小哥哥最好')


#wb,rb,ab  权限，可以保存图片音频
# f=open(r'C:\Users\小哥哥\Desktop\a.jpg','wb')
# print(f.read())
#
#f.close() #关闭文件

#上下文管理器  with 语句  原理：_enter_、_exit_
# 对上下文的打开和关闭强制执行的操作
# 格式 ：with 打开的文件  as 变量名：

# with open(r'C:\Users\小哥哥\Desktop\a.txt','r',encoding='utf-8') as f
#             b=f.readlines()
# c=len(b)
# print(c)
# for i in b:
#     if i=='\n' or i.startswith('#'):
#         b.remove(i)
# c=len(b)
# print(c)


# for i in range(1,11):
#     f=open(r'C:\Users\小哥哥\Desktop\{}.txt'.format(i), 'a', encoding='utf-8')
#     for j in range(1,11):
#         f.write('\n'+'123')
#         f.close



#异常处理语句
#异常：因代码的逻辑关系，导致的程序中断
#异常处理：对将要发生的异常进行预防   try...except...
# 针对某一种异常或者多种异常去处理
# try:
#     a='123'
#     print(a+1)
# # except:   #默认处理所有的异常
# except TypeError as x:
# # except TypeError and NameError as x:  #处理多种异常
#      print('hello')

#当你只想处理一种异常时，在except语句后边加上异常的类型   except TypeError as x:
#报错的格式

#try ...except...else...原理：只要try语句中的代码没有异常，就执行else
# try:
#     a='123'
#     print(a+1)
# except:
#     print('hello')
# else:
#     print('123')

#try ...except...finally..原理：finally语句一定会被执行
# try:
#     a=123
#     print(a+1)
# except:
#     print('hello')
# else:
#     print('zz')
# finally:
#     print('123')

 #    raise    触发异常    自定义异常
# a=123
# raise  Exception('白晓媛zz')
# print(123+1)

# 或者
# a=666
# if a==123:
#     raise Exception('zz')
# print(123+1)

# 导入语句 把要使用的库导入到本文件中  import
# import 元组  库  模板
# import 元组
# print(元组.zhishu())
#if __name__=='__main__':

# 或者 from 文件名 import 函数名    只能导入这一个函数
# 如果函数名用*来代替，代表导入所有函数
# from 元组 import zhishu
# print(zhishu())


#  下载库
# 1.pip下载  pip是python自带的一个组件
# 作用：用来下载网络上的上面的python库
# 用法 ：在cmd中，输入pip install 库名

#步骤 ：File  setting  project interpreter
#  +代表下载  -代表卸载


#  面向对象 ：将函数进行分类和封装，使开发更高效
#只关注   输入和输出
# 在python 上通过 类 来实现某个对象的功能

#  类：属性、方法
# 属性 ：每种方法必须具备的条件
#定义类 ：class 类名():           类名一般为大写
#              def  函数（）：
#                    执行语句
#              def  函数名 ():
#  self 实例化  1.自定义：方便在类的外部调用  2.内置（self）方便在类的内部调用
# class Shuzi():
#     def jiujiu(self):   #  self  类的实例化
#         print(1)
#     def zhishu(self):
#         print(2)
# a=Shuzi()
# a.jiujiu()
# Shuzi().jiujiu()

# class Shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#         #return d
#         print(d)
#     def zhishu(self):
#         b=self.jiecheng()
#         s=0
#         for  i in range(2,b+1):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         print(s)
# a=Shuzi()
# a.zhishu()

 # 继承 ：一个新的类拥有旧的类的所有方法
# class  asd(Shuzi):
#     pass
# asd=asd()
# print(asd.jiecheng())


#多继承 ：一个新的类拥有多个旧的类的继承方法
#如果继承的多个类中有相同的方法，那么使用的是最左边的类里面的
# class Shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#         print(d)
# class asd():
#     def aaa(self):
#         print(123)
# #
# class bbb(asd,Shuzi):
#     pass
# bb=bbb()
# bb.aaa()
# bb.jiecheng()


# 多态 又叫方法重写
# class asd():
#     def aaa(self):
#         print(123)
# class Shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#         print(d)
# class bbb(asd,Shuzi):
#     def aaa(self):
#         a=0
#         for i in range(101):
#             a+=i
#         print(a)
# bb=bbb()
# bb.aaa()

#  私有方法：只属于本类的方法
# 定义私有方法：方法名前加两个下划线
# class asd():
#     def aaa(self):
#         print(123)
# class Shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#         print(d)
# class bbb(asd,Shuzi):
#     pass
# bb=bbb()
# bb.aaa()
# bb.jiecheng()

# class Shuzi():
#     def __init__(self,a,b):
#         self.name=a
#         self.nianji=b
#     def jiecheng(self):
#         print('hello %s,今年%d年级'%(self.name,self.nianji))
#     def bbb(self):
#         print('hello %s'%(self.name))
# aa=Shuzi('小明',7)
# aa.jiecheng()
# aa.bbb()

# class aa():
#     def zhishu(self,x,y):
#         s = 0
#         for i in range(x,y):
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 s += i
#         print(s)
# a=aa()
# a.zhishu(6,100)
#
#
#
# class aaa():
#     def huiwen(self,a):
#         b = len(a) // 2
#         for i in range(b):
#             if a[i] != a[-i - 1]:
#                 print('no')
#                 break
#         else:
#             print('yes')
# b=aaa()
# b.huiwen('qwerwqf')
#
# import pymysql
# #连接数据库
# abc=pymysql.connect(host='192.168.0.196',port=3306,user='root',password='977521',charset='utf8')
# # 创建游标
# aaa=abc.cursor()
# aaa.execute('show databases;') #  执行sql语句  只能输入一个
# print(aaa.fetchall())
# aaa.fetchall()  #读取上一句sql语句的结果
# aaa.execute('use arlicle;')
# print(aaa.fetchmany(3))
# aaa.execute('show databases;')
# aaa.execute('use arlicle;')
# aaa.execute('show tables;')
# print(aaa.fetchall())
# print(aaa.fetchone())
# print(aaa.fetchone())
# print(aaa.fetchone())

# aaa.execute('cleate datebase bbb;')
# aaa.execute('use bbb;')
# aaa.execute('create table biao1(姓名 char(200),年龄 int,班级 char(200);')
# list=['we',1,'qwe']
# for i in range(10):
#     aaa.execute('insert into biao1 values("{}",{},"{}")'.format(list[0],list[1]+i,list[2]))
#     abc.commiit()
# aaa.execute('select * from biao2;')
# for i in aaa.fetchall():
#     print(i)

#
# import pymysql
# abc=pymysql.connect(host='192.168.0.168',port=3306,user='root',password='977521',charset='utf8')
#
# # 创建游标
# aaa=abc.cursor()

# aaa.execute('create database shujuku;')
# aaa.execute('use shujuku;')
# aaa.execute('create table biao1(姓名 char(60),年龄 int,班级 char(60));')
# list1=['xiaobaitu',1,'banji']
# for i in range(30):
#     aaa.execute('insert into biao1 values("{}",{},"{}")'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()
# aaa.execute('select * from biao1;')
# for i in aaa.fetchall():
#     print(i)

# aaa=abc.cursor()
# aaa.execute('create database shujuku;')
# aaa.execute('use shujuku;')
# aaa.execute('create table biao1(姓名 char(60),年龄 int,班级 char(60));')
# list1=['xiaobaitu',1,'banji']
# for i in range(30):
#     aaa.execute('insert into biao1 values("{}",{},"{}")'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()
# aaa.execute('select * from biao1;')
# for i in aaa.fetchall():
#     print(i)

#
# b=abc.cursor()   #指挥者
# b.execute('use test_1;')
# b.execute('desc biao;')          #表头读取到txt中
# bb=b.fetchall()
# with open('a.txt', 'w', encoding='utf-8') as f:
#     f.write('{},{},{}'.format(bb[0][0],bb[1][0],bb[2][0]))
# b=abc.cursor()
# b.execute('select * from biao')  #内容读取到txt文件中
# a=b.fetchall()
# for i in a:
#     with open('a.txt','a+',encoding='utf-8') as f:
#         f.write('\n'+'{},{},{}'.format(i[0],i[1],i[2]))
# print('over')




#
# aaa=abc.cursor()
# aaa.execute('use shujuku;')
# aaa.execute('select * from biao1;')
# shuju=aaa.fetchall()
# aaa.execute('desc biao1;')
# biaotou=aaa.fetchall()
#
# with open ('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             f.write(biaotou[i][0])
#         else:
#             f.write(biaotou[i][0]+',')
#     for j in shuju:
#         f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))
#
#
# import  pymysql
#
# aaa=abc.cursor()
# aaa.execute('use shujuku;')
# aaa.execute('select * fr
#

#  os模块  python自带的模块
# 作用：python与操作系统之间的交互
# import os
# #a=os.popen('ping 192.168.0.6')  #执行命令
# a=os.popen('nslookup www.baidu.com')
# print(a.read())
# 获取当前所在的位置
# print(os.getcwd())

#切换目录
#os.chdir(r'C:\Users\小哥哥\Desktop\xiaogege')  #
#print(os.chdir())
#两个斜杠或者前面加r:为了让转义字符不转义

#创建目录
# os.mkdir('aaaa') #如果不加路径就在当前目录下创建

#创建递归目录
# os.makedirs(r'aaa\bbb\ccc')

#删除递归目录
#os.removedirs(r'aaa/bbb/ccc')

#删除空目录
# os.rmdir('aaaa')

#删除文件
# os.remove('a.txt')

#获取当前目录下的所有文件
# print(os.listdir(r"D:\Program Files (x86)"))

#更改文件名
# os.rename('gouwuche.py','购物车.py')

#将文件名与路径分割开
#注意分割的是字符串与有无此文件或路径无关
# print(os.path.split(r'C:\Users\小哥哥\Desktop\xiaogege\元组.py'))

#将文件后缀名与路径分割开
# print(os.path.splitext(r'C:\Users\小哥哥\Desktop\xiaogege\元组.py'))

#判断是否为普通文件
# print(os.path.isfile('aaaa.py'))

#判断是否为目录文件
# print(os.path.isdir('.idea'))

#判断是否为链接文件
# print(os.path.islink('aaaa.py'))

#判断目录下的普通文件与目录文件
# s=0
# x=0
# os.chdir(r"D:\Program Files\Foxmail 7.2")
# for i in os.listdir():
#     if os.path.isfile(i):
#         print(i)
#         s+=1
#     elif os.path.isdir(i):
#         print(i)
#         x+=1
# print(s)
# print(x)
#

# a=[i for i in os.listdir() if os.path.isfile(i)]
# b=[y for y in os.listdir() if os.path.isdir(y)]
# print(len(a),len(b))

#xlwt 作用：给excel表格写入数据
#xlrd  作用：读取excel表格中的数据
#xlutiles 作用：给excel表格中追加数据

# import xlwt

# 打开一个文件
# f=xlwt.Workbook(encoding='utf-8')
# 添加一个标签页，括号中写标签页中的名称
# sheet=f.add_sheet('python操作excel表格')
#写入数据
#  sheet.write(0,0,'姓名')
# sheet.write(0,1,'年龄')
# sheet.write(0,2,'班级')
#
# #保存文件
# # f.save('text.xls')
# for i in range(1,31):
#         sheet.write(i,0,'小明')
#         sheet.write(i,1,i + 1)
#         sheet.write(i,2,i)
# f.save('text.xls')
#   第一个数字代表多少行。第一列从0开始
#   第二个数字代表多少列。第一行从0开始
#   第三个字符串代表写入的内容

#
# import pymysql
# abc=pymysql.connect(host='192.168.0.183',port=3306,user='root',password='977521',charset='utf8')
# aaa=abc.cursor()


# aaa.execute('create database daoru;')
# aaa.execute('use shujuku1;')
# aaa.execute('create table biao1(姓名 char(60),年龄 int,班级 char(60));')
# b=a[1].split(',')[0]
# print(b)
#     print(a)

# import pymysql
# abc=pymysql.connect(host='192.168.0.21',port=3306,user='root',password='977521',charset='utf8')
# aaa=abc.cursor()
# with open('a.txt', 'r', encoding='utf-8') as f:
#     a=f.readlines()
#     print(a)
# c=[]
# for i in range(30):
#     b=a[i].split(',')
#     c.append(b)
# aaa.execute('create database abc;')
# aaa.execute('use d;')
# aaa.execute('create table biao1(姓名 char(60),年龄 int,班级 char(60));')
# for j in range(1,31):
#     aaa.execute('insert into biao1 values("{}","{}","{}")'.format(c[j][0],int(c[j][1]),c[j][2]))



#password='123456',
# charset='utf8')
# tag = abc.cursor()                                #创建游标
# tag.execute('use yiku;')                          #使用库
# # tag.execute('create table biao4(姓名 char(30),年龄 int,班级 char(30));')      #创建表
# with open('a.txt','r+',encoding='utf-8')as f:                                  #打开txt文件
#     shujv = f.readlines()                                                      #读取txt文件中内容
# shu = len(shujv)                                                               #统计txt文件中有多少行
# for i in range(1,shu):                                                         #循环将txt文件中内容写入到数据库中
#     tag.execute('insert into biao2 values("{}","{}","{}");'.format(shujv[i].split(',')[0],shujv[i].split(',')[1],shujv[i].split(',')[2]))
#     abc.commit()
# tag.execute('select * from biao2;')                                            #查看数据库中表数据
# for i in tag.fetchall():
#     print(i)
# abc.close()
#
# import requests
# import re
#
# class Meizi():
#     head = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5733.400 QQBrowser/10.2.2050.400Name'}
#     def qingqiu(self,page):     #a:个数
#         url = 'http://www.mzitu.com/zipai/comment-page-{}/#comments'.format(page)
#         res = requests.get(url,headers = self.head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         tupian = []
#         a = re.compile(r'<img src="(http://ww\d.sinaimg.cn/mw690/\w+.jpg)"')
#         b = a.findall(html)
#
#         tupian.extend(b)
#
#         return tupian
#     def baocun(self,tupian):
#         for j,i in enumerate(tupian):
#             res = requests.get(i,headers=self.head)
#             html3 = res.content
#
#             with open('{}{}.jpg'.format(w,j), 'wb') as f:
#                 f.write(html3)
# meizi = Meizi()
# for w in range(2):
#     html = meizi.qingqiu(w)
#     tupian = meizi.guolv(html)
#     meizi.baocun(tupian)






# import  requests
# import  re
# tupian=[]
# # 输入网址
# url='https://www.qiushibaike.com/imgrank/'
# # 伪装成浏览器（反爬）
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'}
# response=requests.get(url=url,headers=head)   #发送请求
# html=response.content.decode('utf-8')  #读取的内容
# patt=re.compile(r'<div class="thumb">(.*?)</div>',re.S)   #过滤的条件
# itmes=patt.findall(html) #过滤出想要的内容
# print(itmes)
#
# tupian=[]
# for i in itmes:
#     response=requests.get(url=i,headers=head)  #发送请求
#     html1=response.content.decode('utf-8')#读取的内容
#     patt1=re.compile(r'<img src="//(.*?) alt') #过滤图片的条件
#     itmes2=patt1.findall(i)  #过滤的内容
#     for j in itmes2:
#         tupian.append(j)   #图片过滤
# print(tupian)

# for e,k  in enumerate(tupian): #
#     k = k.replace('"', '')
#     ur = 'https://{}'.format(k)
    # print(ur)
    # tupian=requests.get(url=ur) #发送请求
    # jap=tupian.content # 获取图片的二进制文件
    # with open(r'E:\爬虫文件\{}.jpg'.format(e),'wb') as f:
    #     f.write(jap)
#
# import requests
# import re
#
# url='https://www.qqtn.com/tp/sgtp_1.html'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# url = 'https://www.qqtn.com/tx/qinglvtx_{}.html'.format(8)
# res = requests.get(url=url, headers=head)
# html = res.content.decode('gbk')
# # print(html)
# patt = re.compile(r'<li><a href="(.*?)" target="_blank" title="',re.S)
# # (r'<li><a href="(.*?)" target="_blank" title="',re.S)
# itmes = patt.findall(html)
# # print(itmes)
# tupian=[]
# for i in itmes:
#     i = i.replace("'", '')
#     i='https://www.qqtn.com'+i
#     res1 = requests.get(url=i, headers=head)
#     html5 = res1.content.decode('gbk')
#     patt2 = re.compile(r'<p align="center"><img src="(.*?)"/></p>',re.S)
#     itme2 = patt2.findall(html5)
#     for i in itme2:
#         tupian.append(i)
# for i,j in enumerate(tupian):
#         res=requests.get(url=j, headers=head)  #发送请求
#         html2=res.content  #获取照片的二进制
#         with open(r'E:\头像1\{}.jpg'.format(i),'wb') as f:
#             f.write(html2)
























