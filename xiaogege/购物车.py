#/usr/bin/env python
#-*- coding: utf-8 -*-
# goods=[
#     {'name':'电脑','price','1999'}
#     {'name':'鼠标','price','10'}
#     {'name':'游艇','price','20'}
#     {'name':'美女','price','998'}
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
# def cz():
#     global a
#     aa = int(input('金额'))
#     a += aa
#     return a
#
# def sc():
#     global s
#     bb = int(input('商品号'))
#     q = b[bb - 1]['price']
#     s-=q
#     c.remove(bb)
#     return a
# s=0
# def goumai():
#     global s
#     for f in c:
#         g = b[f - 1]['price']
#         s += g
#     print(s)
#     if a<s:
#         print('选择')
#         aaa=input('充值或减商品')
#         while True:
#             if aaa == '充值':
#                 cz()
#                 if a > s:
#                     print('购买成功')
#                     break
#             else:
#                 sc()
#                 print(s)
#                 if a > s:
#                     print('购买成功')
#                     break
#     else:
#         print('购买成功')
a=int(input('输入总资产'))
b=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
for i,j in enumerate(b):
    print(i+1,j)
c=[]
while True:
		e = int(input('大兄弟买啥就点啥，买完按5'))
		if e < 5:
			c.append(e)
		elif e == 5:
			print('小哥哥，结账')
			break
goumai()
