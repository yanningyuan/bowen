#/usr/bin/env python
# -*- coding:utf-8 -*-
#import random
# 基础语句 循环语句  异常处理语句  上下文管理语句

#判断语句
#格式  if  条件:
#    (缩进)执行语句
#      else
#    (缩进)执行语句
# 注意： ： 缩进
#a=54
#if a > 30:
#  print('你好')
#else:
#  print('你不好')

#a=int(input('输入成绩'))
#if a >= 90:
#    print('优秀')
#elif a >= 80:
#    print('良好')
#elif a >=70:
#    print('一般')
#elif  a >=60:
#    print('差')
#else:
# print('不及格')


# 嵌套判断
#a=input('字符串')
#if a.startswith('a'):
#    if a.endswith('c'):
#       print('helloword')
#    else:
#       print('hello')
# #elif  a.endswith('c'):
#    print('word')
#else:
#    print(123)




#判断三角形
#a=input('输入数字')
#b=a.split(',')
#b.sort()
#c=int(b[0])
#d=int(b[1])
#e=int(b[2])

#if c+d>e:
#    if c**2+d**2==e**2:
#        print('直角')
#    elif c**2+d**2<e**2:
#        print('钝角')
#    elif  c**2+d**2>e**2:
#        print('锐角')
#else:
#    print('不是三角形')


# for 语句   格式：for 变量名 in 范围
#                        执行语句
#                        执行语句
#                        执行语句
#                        。。。。
#       注意 ：  1.没有do和done
#                 2.冒号和缩进
#
#1.   range 函数 : 将数字变为一个范围   1.只有一个数字时，默认从零开始
#                                  2.有两个数字时，第一个数字是起始值
#                                  3.有三个数字时，第三个数字是递进
#
#a=12
#for i in range(2,a,3):
#    print(i)
#a=0  #b=0
#for i in range(1,100,2):
#    a+=i
#print(a)
#b=0
#for  j in range(2,100,2):
#    b+=j
#print(a-b)

# 2.   enumerate 函数:
 #          将下标位置和元素对应
# a=['asd','123','er']
# for i,j in enumerate(a):
#    print(i)
#    print(j[0])

#a=['电脑','计算机','mp3']
#for i,j in enumerate(a):
#   print(i+1,j)
#b=int(input('1'))
#print(a[b-1])


# 循环嵌套判断 for 语句中 if 语句
#b=0
#for a in range(1,100):
#    if a % 2 ==0:
#        b-=a
#    else:
#        b+=a
#print(b)



#a=random.randrange(1,10) #从1到10中间随机选取一个数

#b=int(input('输入数字'))
#if b==a:
#    print



#循环嵌套循环  for..for
#for i in range(3):
 #   for j in range(2):
  #      print(123)

#  end='不换行'  print()换行

#   九九乘法
#for i in range(1,10):
##    for j in range(1,i+1):
#        print('{}*{}={}'.format(i,j,i*j),end='\t')
#    print('')

# continue 结束本次循环  break 结束循环



#  for... else..语句  原理:只要循环没有被break掉，就执行else 语句

#  while 循环  格式;while 条件：

# while  条件：
#     执行语句
#     执行语句
#     。。。。


#for循环通常用于循环有序列的数据
#while循环通常用于根据条件循环
# a=3
# while a<3:
#     print('zz')
#     a+=1

# a=1
# b=0
# while a<101:
#     b=b+a
#     a+=1
#
# print(b)


#while 九九乘法表
# a=0
# while a<10:
#     a+= 1
#     b=1
#     while b<=a:
#         print('{}*{}={}'.format(b,a,a*b), end='\t')
#         b+=1
#     # a+=1
#     print('')

#while ...else...语句
#循环只要不被break掉，就执行else语句
# a=2
# while a<3:
#     print('zz')
#     break
# else:
#     print('bxy')


# a = input('输入一组数')
# b=a.split(',')
# # c=len(b)
# for i,j in enumerate(b):
#     b[i]=int(j)
# for q in range(0,len(b)-1):
#    for e in range(q+1,len(b)):
#        if b[q]>b[e]:
#            d=b[q]
#            b[q]=b[e]
#            b[e]=d
#
# print(b)


#  创建十个文件夹，文件夹里添加十个文件，文件里添加十行
# import os
# for i in range(1,11):
#     os.mkdir(r'C:\Users\admin\Desktop\新建文件夹{}'.format(i))
#     for j in range(1,11):
#         with open(r'C:\Users\admin\Desktop\新建文件夹{}\{}.txt'.format(i,j),'w',encoding='utf-8') as f:
#             f.write('123')
#         with open(r'C:\Users\admin\Desktop\新建文件夹{}\{}.txt'.format(i,j),'a',encoding='utf-8') as f:
#             for c in range(9):
#                 f.write('\n'+'123')
#                 f.close
#         os.remove(r'C:\Users\admin\Desktop\新建文件夹{}\{}.txt'.format(i,j))
#     os.rmdir(r'C:\Users\admin\Desktop\新建文件夹{}'.format(i))


# import xlwt
# with open ('a.txt','r',encoding='utf-8') as f:
#     a=f.readline()
#     b=a.split(',')
#     c=f.read()
#     d=c.split('\n')
# e=xlwt.Workbook(encoding='utf-8')
# sheet=e.add_sheet('>')
# for i,j in enumerate(b):
#     sheet.write(0,i,j)
# for m,n in enumerate(d):
#     g=n.split(',')
#     for i in range(len(g))
#         sheet.write(m+1,i,g[i])
# e.save('text.xls')


# import xlrd
# f=xlrd.open_workbook(encoding='utf-8')
# sheet=f.nsheets
# sheet=f.sheets()[0]
# a=sheet.nrows
# b=sheet.row_values(0)
# with open ('a.txt','w',encoding='utf-8') as e:
#
#     for i in range(len(b)):
#         if i==len(b)-1:
#             e.write(b[i])
#         else:
#             e.write(b[i]+',')
#     for j in range(1,a):
#         k=sheet.row_values(j)
#         for m in range(len(k)):
#             if m==len(k)-1:
#                 e.write(k[m]+'\n')
#             else:
#                 e.write(k[m]+',')


# import pymysql
# import xlwt
# abc=pymysql.(host,port,user,passward,charset)
# aaa=abc.cursor
# aaa.execute('use python')
# aaa.execute('dest biao1')
# biaotou=aaa.fetchall
# aaa.execute('select * from biao1')
# shuju=aaa.fetchall
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('>')
# for i in range(len(biaotou)):













