#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
def duqu():
    shuju=[]
    f=xlrd.open_workbook(r'C:\Users\admin\Desktop\xiaogege\自动化web\data\邮箱.xls')
    sheet=f.sheets()[0]
    num=sheet.nrows
    for i in range(1,num):
        aa = sheet.row_values(i)
        shuju.append(aa)
    return shuju

