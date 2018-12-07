#/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunnertest
from 框架.hao_test.text_学校 import 学校
import xlrd
# def 生成():
#     suit=unittest.TestSuite()
#     suit.addTest(unittest.makeSuite(学校))
#     now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#     f = open('abc.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
#                                              description='测试结果如下:',
#                                              title='好分数测试报告',
#                                              stream=f)
#     runner.run(suit)
#     f.close()
# 生成()
# def yongli():
#     shuju = []
#     f = xlrd.open_workbook(r'c:\Users\admin\Desktop\xiaogege\框架\driver\用例.xls')
#     sheet = f.sheets()[0]
#     num = sheet.nrows
#     for i in range(num):
#         aaa = sheet.row_values(i)
#         shuju.append(aaa)
#     return shuju

# class Test_run:
#     def run_多个(self):
#         suit=unittest.TestSuite()
#         for i in yongli():
#             print(i)
#             suit.addTest(unittest.makeSuite({}).format(i[0]))
#             now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#             f = open('abc.html', 'wb')
#             runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
#                                                        description='测试结果如下:',
#                                                        title='好分数测试报告',
#                                                        stream=f)
#             runner.run(suit)
#             f.close()
# print(yongli())
# a=Test_run()
# a.run_多个()
# class Test_run:
#     def run_多个(self):
#             suit=unittest.TestSuite()
#
#             suit.addTest(unittest.makeSuite(学校))
#             now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#             f = open('abc.html', 'wb')
#             runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
#                                                        description='测试结果如下:',
#                                                        title='好分数测试报告',
#                                                        stream=f)
#             runner.run(suit)
#             f.close()
#
#     def run_all(self):
#         suit = unittest.TestSuite()
#         discover = unittest.defaultTestLoader.discover(r'c:\Users\admin\Desktop\xiaogege\框架\driver\hao_text', pattern='test*.py')
#         suit.addTest(discover)
#         now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#         f = open('abc.html', 'wb')
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
#                                                    description='测试结果如下:',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()
# # run=Test_run()
# # run.run_all()
# # tex_1=open(r'c:\Users\admin\Desktop\xiaogege\框架\driver\run.txt','r',encoding='utf-8')
# # du=tex_1.readlines()
# # tex_1.close()
# # print(du)
# # if __name__ == '__main__':
# #     # if 'all' in du:
# #         run.run_all()
# #     # else:
# #         run.run_多个()
# if __name__ == '__main__':
#     run=Test_run()
#     run.run_all()










class Test_run():

    def run_多个(self):
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(学校))
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('abc.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
                                                   description='测试结果如下:',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()


    def run_all(self):
        suit=unittest.TestSuite()  #添加测试套件
        discover=unittest.defaultTestLoader.discover(r'c:\Users\admin\Desktop\xiaogege\框架\hao_test',pattern='text*.py')
        #                                            测试用例所在的路径         匹配
        suit.addTest(discover)  #添加测试用例
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('abc.html','wb')

        runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
                                                  description='测试结果如下:',
                                                  title='好分数测试报告',
                                                  stream=f)
        runner.run(suit)
        f.close()

if __name__=='__main__':
    a=Test_run()   #调用
    a.run_all()