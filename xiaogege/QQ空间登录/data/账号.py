#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
def duqu():
    shuju=[]
    f=xlrd.open_workbook(r'C:\Users\admin\Desktop\xiaogege\QQ空间登录\data\账号.xls')
    sheet=f.sheets()[0]
    num=sheet.nrows
    for i in range(1,num):
        aa = sheet.row_values(i)
        shuju.append(aa)
    return shuju
# shuju=[]
# f=xlrd.open_workbook(r'C:\Users\admin\Desktop\xiaogege\QQ空间登录\data\账号.xls')
# sheet = f.sheets()[0]
# num = sheet.nrows
# for i in range(1, num):
#     aa = sheet.row_values(i)
#     shuju.append(aa)
# print(shuju)