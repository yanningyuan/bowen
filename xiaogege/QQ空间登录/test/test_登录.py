#/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from QQ空间登录.config.QQ空间登录 import 空间_登录
from QQ空间登录.data.账号 import duqu
import re
from selenium import webdriver
from time import sleep


#
class denglu(unittest.TestCase):
    # tes_登录 = 空间_登录().登录
    tes_yanzheng=空间_登录().yanzheng
    tes_yanzheng1 = 空间_登录().yanzheng1
    # gouwu=空间_登录().添加购物车
    shuju = duqu()
    def test_1(self):
        # denglu = self.tes_登录(int(self.shuju[0][0]),str(self.shuju[0][1]))
        wd=self.tes_yanzheng(int(self.shuju[0][0]),str(self.shuju[0][1]))

        self.assertEqual(wd, str(self.shuju[0][2]))
        sleep(2)
        # self.dr.quit()
        # denglu = self.tes_登录(int(self.shuju[1][0]), str(self.shuju[1][1]))
        # wd = self.tes_yanzheng(int(self.shuju[1][0]), str(self.shuju[1][1]))
        # self.assertEqual(wd, str(self.shuju[1][3]))
    def test_2(self):
        # denglu = self.tes_登录(int(self.shuju[1][0]), str(self.shuju[1][1]))
        sd = self.tes_yanzheng1(int(self.shuju[1][0]), str(self.shuju[1][1]))
        self.assertEqual(sd, str(self.shuju[1][2]))
        sleep(2)
        # self.dr.quit()
    def test_3(self):
        # wd=self.gouwu
        # self.assertEqual(wd,'商品已成功加入购物车！')
        dr = webdriver.Chrome()
        dr.get('https://item.jd.com/35821336743.html')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
        sleep(2)
        txt = dr.find_element_by_xpath('//*[@id="result"]/div/div/div[1]/div[1]/h3').text
        self.assertEqual(txt, '商品已成功加入购物车！')
        dr.quit()
