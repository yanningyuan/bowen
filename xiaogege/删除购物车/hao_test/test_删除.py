#/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from 删除购物车.config.删除_接口 import 删除_购物车
from 删除购物车.data.duqu_商品 import duqu
class 删除(unittest.TestCase):
    tes_删除=删除_购物车().删除
    shuju=duqu()
    def test_1(self):
        html = self.tes_删除(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(html['code'], str(int(self.shuju[0][2])))

    # def test_1(self):
    #     html = self.tes_删除(int(self.shuju[0][0]),int(self.shuju[0],[1]))
    #     # print(html)
    #     self.assertEqual(html['code'], str(int(self.shuju[0][2])))
    #     # self.assertIn(len(html['data']), range(int(self.shuju[0][2])))

    def test_2(self):
        html = self.tes_删除(int(self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertEqual(html['code'], str(int(self.shuju[1][2])))
        # self.assertEqual(len(html['data']), int(self.shuju[1][2]))

    def test_3(self):
        html = self.tes_删除(self.shuju[2][0],int(self.shuju[2][1]))
        self.assertEqual(html[''], str(int(self.shuju[2][2])))
        # self.assertEqual(len(html['data']), int(self.shuju[2][2]))

    def test_4(self):
        html=self.tes_删除(self.shuju[3][0],int(self.shuju[3][1]))
        self.assertEqual(html['code'], str(int(self.shuju[3][2])))
    def test_5(self):
        html = self.tes_删除(self.shuju[4][0], int(self.shuju[4][1]))
        self.assertEqual(html['code'], str(int(self.shuju[4][2])))
    def test_6(self):
        html = self.tes_删除(self.shuju[2][0], int(self.shuju[2][1]))
        self.assertEqual(html['shang'], str(int(self.shuju[2][2])))

# if __name__ == '__main__':
#     unittest.main()