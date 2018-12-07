#/usr/bin/env python
# -*- coding:utf-8 -*-
#接口测试：发送请求，验证响应是否符合需求的过程
#postman|jmeter

#requests 发送http请求   assert来做断言处理

import requests
import unittest
import HTMLTestRunnertest
import HTMLTestRunne
import time
import xlrd
# url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
# a=input('地区')
# querystring = {"filterInput":"{}".format(a)}
#
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#     'cache-control': "no-cache",
#     'Postman-Token': "620e3ca0-2919-43c1-943e-e190e5dc8404"
#     }
#
# response = requests.get(url=url, headers=headers, params=querystring)
# html=response.json()
# print(html['code'])
# class 学校():
#     def test_学校(a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         a = input('地区')
#         querystring = {"filterInput": "{}".format(a)}
#
#         headers = {
#             'Content-Type': "application/x-www-form-urlencoded",
#             'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#             'cache-control': "no-cache",
#             'Postman-Token': "620e3ca0-2919-43c1-943e-e190e5dc8404"
#         }
#
#         response = requests.get(url=url, headers=headers, params=querystring)
#         html = response.json()
#         assert

def tes_学校(a):
    url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
    querystring = {"filterInput": "{}".format(a)}

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
        'cache-control': "no-cache",
        'Postman-Token': "620e3ca0-2919-43c1-943e-e190e5dc8404"
    }

    response = requests.get(url=url, headers=headers, params=querystring)
    html = response.json()
    return html






# unittest:pytthon自带单元测试自动化测试框架
# unittest.TestCase:  用来做用例管理
# unittest.TestSuite: 测试套件
# unittest.TestLoader: 测试载入：测试用例加载到测试套件中
# unittest.TestRunner: 执行测试用例
#  封装了检验返回的结果  俗称断言
# class 学校(unittest.TestCase):
#     # def setUp(self):   #初始化测试环境   每次执行测试用例前执行
#     #     print(123)
#     # def tearDown(self):  # 清理环境  每次用例执行之后去执行
#     #     print(567)
#     def test_1(self):
#         html=tes_学校('北京')
#         self.assertEqual(html['code'],0)
#         self.assertEqual(html['data'][0]['schoolName'],'北京七中')
#
#     def test_2(self):
#         html = tes_学校('abcd')
#         self.assertNotEqual(html['code'],0)
#     def test_3(self):
#         html = tes_学校(123456)
#         self.assertEqual(html['code'],0)
# if __name__ == '__main__':
#     # unittest.main()
#     #生成测试报告  创建一个测试套件
#     suit=unittest.TestSuite()
#     #添加测试用例   将测试用例添加到测试套件中
#     #suit.addTest(
#     # suit.addTest(学校('test_1'))
#     # suit.addTest(学校('test_2'))
#     # suit.addTest(学校('test_3'))
#     #将整个类中的所有测试用例添加到测试套件中
#     suit.addTest(unittest.makeSuite(学校))
#     now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#     f = open('abc.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
#                                              description='测试结果如下:',
#                                              title='好分数测试报告',
#                                              stream=f)
#     runner.run(suit)
#     f.close()




def tes_数据(self):
        shuju=[]
        f=xlrd.open_workbook('借口.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            aaa=sheet.row_values(i)
            shuju.append(aaa)
        return shuju


class 学校(unittest.TestCase):
    def tes_数据(self):
        shuju = []
        f = xlrd.open_workbook('借口.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1, num):
            aaa = sheet.row_values(i)
            shuju.append(aaa)
        return shuju
    # def setUp(self):   #初始化测试环境   每次执行测试用例前执行
    #     print(123)
    # def tearDown(self):  # 清理环境  每次用例执行之后去执行
    #     print(567)
    def test_1(self):
        shuju=self.tes_数据()
        html=tes_学校(shuju[0][0])
        self.assertEqual(html['code'],int(shuju[0][1]))
        self.assertIn(len(html['data']),range(int(shuju[0][2])))

    def test_2(self):
        shuju = self.tes_数据()
        html = tes_学校(shuju[1][0])
        self.assertEqual(html['code'], int(shuju[1][1]))
        self.assertEqual(len(html['data']),int(shuju[1][2]))
    def test_3(self):
        shuju = self.tes_数据()
        html = tes_学校(shuju[2][0])
        self.assertEqual(html['code'], int(shuju[2][1]))
        self.assertEqual(len(html['data']), int(shuju[2][2]))
if __name__ == '__main__':
    # unittest.main()
    #生成测试报告  创建一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例   将测试用例添加到测试套件中
    #suit.addTest(
    # suit.addTest(学校('test_1'))
    # suit.addTest(学校('test_2'))
    # suit.addTest(学校('test_3'))
    #将整个类中的所有测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(学校))
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open('abc.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
                                             description='测试结果如下:',
                                             title='好分数测试报告',
                                             stream=f)
    runner.run(suit)
    f.close()




import requests















