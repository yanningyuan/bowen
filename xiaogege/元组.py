#/usr/bin/env python
# -*- coding:utf-8 -*-
import random
#a='a,b,c'
#b='-'.join(a)
#b=a.split('b')
#print(b)
#a=[123,321,412,535,1,123,1,412]
#a.append(2)
#a.insert(2,'bn')
#a.remove(1)
#a.pop(1)
#b=a.index(4)
#b=set(a)
#c=list(b)
#c.sort()
#c.reverse()

#print(c)

# a=[2,34,2,5]
# b=['qw','rt','nhj']
# a.append(3)
# a.insert(4,'3')
# print(a)
# b=a.index(2)
# print(b)
#b=a.count(2)
#b=len(a)
#a.reverse()
#a.sort()
#a.extend(b)
#print(a)



#a=('qwew',123,46)
#b=a.count(12)
#b=a.index(43)
#print(a)



#a={'name':'yan','age':18,'xingge':'稳得一批'}
#b={'wo':'啧啧'}
#a['lala']='ha'
#a.pop('name')
#a.popitem()
#b=a.keys()
#b=a.values()
#b=a.items()
#a.pop('name')
#a.popitem()
#b=a.keys()
#b=a.values()
#b=a.items()
#a.update(b)
#print(a)


#a={12,34,56,76}
#b={'qwe','vcfd'}
#a.add(('qwew',123,46))
#a.pop()
#a.remove(12)
#a.update(b)
#print(a)



#a=input('输入')
#b=a.split(',')
#b.sort()
#c=int(b[0])
#d=int(b[1])
#e=int(b[2])
#if c+d>e:
#    if c**2+d**2==e**2:
#       print('直角')
#    elif c**2+d**2<e**2:
#        print('钝角')
#    else:
#        print('锐角')
#else:

#  print('不是')


# for 语句   格式：for 变量名 in 范围
#                        执行语句
#                        执行语句
#                        执行语句
#                        。。。。
#       注意 ：  1.没有do和done
#                 2.冒号和缩进
#
#range 函数 : 将数字变为一个范围   1.只有一个数字时，默认从零开始
#                                  2.有两个数字时，第一个数字是起始值
#                                  3.有三个数字时，第三个数字是递进
#
#a=12
#for i in range(2,a,3):
#    print(i)
#a={'name':'yan','age':18,'xingge':'稳得一批'}
#for i,j in a.items():
#    print(i,j)
# a=random.randrange(1,10) #从1到10中间随机选取一个数

#  三次猜数字
# for i in range(1,4):
#   b = int(input('输入数字'))
#   if b==a:
#      print('你真棒')
#      break
#   elif b>a:
#        if i==1:
#          print('大了，还有两次机会')
#        elif i==2:
#          print('大了，还有1次机会')
#   elif b<a:
#        if i == 1:
#          print('小了，还有两次机会')
#        elif i == 2:
#          print('小了，还有1次机会')
# else:
#     print('笨蛋')

#质数之和
# def zhishu(x=2,y=101):
#     b = 0
#     for i in range(2, 101):
#         for j in range(2, i + 1):
#             a = i % j
#             if a == 0:
#                 break
#         if i == j:
#             b += j
#     return b
# #if __name__=='__main__':
# print('zz')


# 阶乘求和
# a=0
# c=1
# b=int(input('输入阶乘数'))
#
# for i in range(1,b+1):
#    c=c*i
#    a+=c
# print(a)


#去重
#a=[1,1,1,3,3,4,5,5,6]
#for i in a:
#    if  a.count(i)>1:
#        for j in  range(a.count(i)-1):
#            a.remove(i)
#print(a)






 #三次猜数字
# c=1
# while c>0:
#   b = int(input('输入数字'))
#   if b==a:
#      print('你真棒')
#      break
#   elif b>a:
#        # if i==1:
#      print('大了')
#        # elif i==2:
#        #   print('大了，还有1次机会')
#   elif b<a:
#        # if i == 1:
#      print('小了')
#        # elif i == 2:
#        #   print('小了，还有1次机会')
# else:
#      print('笨蛋')

#第三个python的内置函数    sum()  求和
# a=[2,4,3,6,8,1,0]
#
# print(sum(a))



# while a=='exit':
#     a = input('输入一组数')
#     break
# else:
# b=a.split(',')
# c=int(b)
# d=len(c)
# print(c)


# a=input('>>>>')
# b=a.split(',')
# for i in (b):
#     for j in (b):
#
# print(b)

# a = input('输入一组数')
# b=a.split(',')
# c=len(b)
# for i,j in enumerate(b):
#     b[i]=int(j)
# print(b)
# print(c)


#字符串不用int变整数
# a='123456'
# b=a[::-1]
# c=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             c+=h*10**i
# print(c)


#十进制换十六进制  不太会
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('>>'))
# f=''
# while True:
#    c=b%16
#    b=b//16
#    f+=a[c]
#    if b==0:
#        break
# print(f[::-1])








#  判断字符串是否回文
# a='qwerwq'
# b=len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')



# a='1234'
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
#
# a='qwerttrewq'
# b=len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')


# 任意4个数，组成不同的三位数
# c=input('>')
# d=c.split(',')
# a=[]
# for i in d:
#     for j in d:
#         for k in d:
#            if (i!=j) and (j!=k) and (i!=k):
#        #           print(i,j,k)
#                a.append(int(i)*100+int(j)*10+int(k))
# print(a)


#将列表中最大的放在最后一位，最小的放在第一位
# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
# c=b.index(max(b))
# d=b.index(min(b))
# b[c],b[-1]=b[-1],b[c]
# b[d],b[0]=b[0],b[d]
# print(b)

# a=[55,988,7,7,77,9]
# b=a.index(max(a))
# c=a.index(min(a))
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)



#向左移一位
# a=input('请输入一组数')
# b=a.split(',')
# c=len(b)
# for i in  range(c-1):

#     t=b[i]
#     b[i]=b[i+1]   # b[i],b[i+1]=b[i+1],b[i]
#     b[i+1]=t

# print(b)


# def quchong():
#     a = input('>')
#     b = a.split(',')
#     for i in b:
#         if b.count(i) > 1:
#             for j in range(b.count(i) - 1):
#                 b.remove(i)
#     print(b)
# quchong()

# c=input('>')
# d=c.split(',')
# a=[]
# for i in d:
#     for j in d:
#         for k in d:
#            if (i!=j) and (j!=k) and (i!=k):
#        #           print(i,j,k)
#                a.append(int(i)*100+int(j)*10+int(k))
# print(a)




#a=int(input(''))

# a=input('>')
# d=a.split(',')
# b=[]
# for i in d:
#     c=int(i)
#
# print(c)


#打印列表中第一大和第二大的数

# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
# c=set(b)               #不太正确
# d=c.copy()
# f=max(d)
# print(f)
# d.remove(f)
# g=max(d)
# print(g)

# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
#
# f=b.copy()
# c=max(b)
# for d in f:
#     if d==c:
#         print(d)
# for i in f:
#     if i==c:
#         f.remove(c)
# f.remove(c)
# c=max(f)
# for e in f:
#     if e==c:
#         print(e)



# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
# c=[]
# for d in b:
#     if d not in c:
#         c.append(d)
# print(c)


# 一个数的因数之和等于它本身
# for i in range(1,1000):
#     s=0
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:
#         print(i)




# 一个有顺序的列表，随机加入一个数，加入的数在正确的位置

# a=[1,3,5,7,9]
#
# b=int(input('<'))
# c=len(a)
# d=max(a)
# e=min(a)
# for b in a:
#     if b==d:
#         a.insert(-1,b)
#         print(a)
#     break
# for e in a:
#     if b==e:
#         a.insert(0,b)
#         print(a)
#
#     break
# for i in range(c):
#     if b>a[i] and b<a[i+1]:
#         a.insert(i+1,b)
#     print(a)
# #




# a=4
# for i in range(4):
# 	print(' '*i,'* '*a)
# 	a-=1
# b=4
# for k in range(4):
# 	print(' * '*b)
# 	b-=1

# a=[1,2]
# b=a[0]
# b=' b'* 2
# print(b)

# def 加入购物车(x=1,y=10):
# 	for d in range(x, y):
# 		e = int(input('大兄弟买啥就点啥，买完按5'))
# 		if e < 5:
# 			c.append(e)
# 		if e == 5:
# 			print('小哥哥，结账')
# 			break
# 加入购物车()


# def zuoyi(*a):
#     b = a.split(',')
#     c = len(b)
#     for i in range(c - 1):
#         t = b[i]
#         b[i] = b[i + 1]  # b[i],b[i+1]=b[i+1],b[i]
#         b[i + 1] = t
#     return b




# def
# a=int(input('输入总资产'))
# b=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
# for i,j in enumerate(b):
#     print(i+1,j)
# c=[]
# for d in range(1,10):
#     e=int(input('大兄弟买啥就点啥，买完按5'))
#     if e<5:
#         c.append(e)
#     if e==5:
#         print('小哥哥，结账')
#         break
# print(c)
# s=0
# for f in c:
#     g=b[f-1]['price']
#     s+=g
# print(s)
# if s>a:
#     print('小哥哥，钱不够，可以卖身吗？')
#     h=int(input('1卖身换钱2忍着心痛减少商品'))
#     if h==1:
#         for k in range(66):
#             l=int(input('卖身换的钱'))
#             a+=l
#             m=int(input('1继续卖身2虚了不卖了'))
#             if m==1:
#                 print('扁扁的钱包')
#                 print(a)
#                 continue
#             if m==2:
#                 print('哼，卖身后有钱了')
#                 print(a)
#                 if s>a:
#                     print('呸，赔钱货，钱不够，继续卖身')
#                     print('商品总价')
#                     print(s)
#                     print('钱包')
#                     print(a)
#                     continue
#                 if s<=a:
#                     print('商品价格')
#                     print(s)
#                     print('余额')
#                     print(a - s)
#                     print('好开心哟，又把购物车清了')
#                     break
#     if h==2:
#         for n in range(6):
#             o=int(input('忍痛减少购物车'))
#             q=b[o-1]['price']
#             s=s-q
#             c.remove(o)
#             print('商品总价')
#             print(s)
#             print('钱包余额')
#             print(a)
#             if c==[]:
#                 print('没有商品')
#             n=int(input('1继续减少购物车2不减购买'))
#             if n == 1:
#                 print('购物车价格')
#                 print(s)
#                 continue
#             if n == 2:
#                 if s>a:
#                     print('钱还是不够，呜呜呜，继续减少商品')
#                     print('购物车价格')
#                     print(s)
#                 if s<=a:
#                     print('商品价格')
#                     print(s)
#                     print('余额')
#                     print(a-s)
#                     print('购买成功')
#                     break




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





# import pymysql
# abc=pymysql.connect(host='192.168.0.196',port=3306,user='root',password='977521',charset='utf8')
#
# # 创建游标
# aaa=abc.cursor()
#
# aaa.execute('create database shujuku1;')
# aaa.execute('use shujuku1;')
# aaa.execute('create table biao1(姓名 char(60),年龄 int,班级 char(60));')
# list1=['xiaobaitu',1,'banji']
# for i in range(30):
#     aaa.execute('insert into biao1 values("{}",{},"{}")'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()
# aaa.execute('select * from biao1;')
# for i in aaa.fetchall():
#     print(i)

# import pymysql
# abc=pymysql.connect(host='192.168.0.168',port=3306,user='root',passward=977521,charset='utf8' )
# a=abc.cursor()
# # a.execute('create database shuju')
# with open('a.txt', 'r', encoding='utf-8') as f:
#     print(f.readlines())
#     a=f.readlines()
# # print(a[0].split(',')[0])
# c=[]
# for i in range(30):
#     b=a[i].split(',')
#     c.append(b)
#     aaa.execute('insert into biao1 values("{}",{},"{}")'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()













