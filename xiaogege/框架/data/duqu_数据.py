#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd

def duqu():
        shuju=[]
        f=xlrd.open_workbook(r'c:\Users\admin\Desktop\xiaogege\框架\data\借口.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        print(num)
        for i in range(1,num):
            aaa=sheet.row_values(i)
            shuju.append(aaa)
        return shuju
a=duqu()
print(a)