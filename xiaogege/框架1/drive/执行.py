#/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
from 框架1.report.报告 import Test_run
if __name__=='__main__':
    run=Test_run()
    with open(r'c:\Users\admin\Desktop\xiaogege\框架1\data\run.txt','r') as f:
        aa=f.readlines()
        print(aa)

        if 'all' in aa:
            run.run_all()
        else:
            run.run_报告(aa)