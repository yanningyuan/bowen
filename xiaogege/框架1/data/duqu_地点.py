#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
def duqu():
    shuju=[]
    f=xlrd.open_workbook(r'c:\Users\admin\Desktop\xiaogege\框架1\data\地点.xls')
    sheet=f.sheets()[0]
    num=sheet.nrows
    for i in range(1,num):
        aa=sheet.row_values(i)
        shuju.append(aa)
    return shuju
