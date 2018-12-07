#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
def duqu():
    shuju=[]
    f=xlrd.open_workbook(r'c:\Users\admin\Desktop\xiaogege\删除购物车\data\商品.xls')
    sheet=f.sheets()[0]
    num=sheet.nrows
    # print(num)
    for i in range(1,num):
        aa=sheet.row_values(i)
        shuju.append(aa)
    return shuju
# duqu()
# shuju=[]
# f = xlrd.open_workbook(r'c:\Users\admin\Desktop\xiaogege\删除购物车\data\商品.xls')
# sheet = f.sheets()[0]
# num = sheet.nrows
# for i in range(1,num):
#         aa=sheet.row_values(i)
#         shuju.append(aa)
#
#
# print(shuju)