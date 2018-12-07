#/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from 自动化web.config.注册摩尔_ import 注册_摩尔
from 自动化web.data.注册_账号 import duqu
import re
from selenium import webdriver
from time import sleep
# a=注册_摩尔()
# c=a.注册()
# print(c[1])


# class zhuce(unittest.TestCase):
#     tes_注册 = 注册_摩尔().注册
#     wd1=注册_摩尔().wenben
#     shuju = duqu()
#     def test_1(self):
#         html = self.tes_注册(int(self.shuju[0][0]))
#         wd=self.wd1(int(self.shuju[0][0]))
#         self.assertEqual(wd, str(self.shuju[0][1]))
class zhuce(unittest.TestCase):
    a = 注册_摩尔()
    c = a.注册()
    b=c[0]
    wd1=c[1]
    shuju=duqu()
    def test_1(self):
        zhu=self.b(int(self.shuju[0][0]))
        wd = self.wd1(int(self.shuju[0][0]))
        self.assertEqual(wd, str(self.shuju[0][1]))


