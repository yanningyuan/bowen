#/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import HTMLTestRunnertest
import unittest
class Test_run():
    def run_报告(self,aa):
        suit=unittest.TestSuite()
        for i in aa:
            discover=unittest.defaultTestLoader.discover(r'c:\Users\admin\Desktop\xiaogege\删除购物车\hao_test',pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'c:\Users\admin\Desktop\xiaogege\删除购物车\report\abc.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
                                                      description='测试结果如下:',
                                                      title='删除购物车测试报告',
                                                      stream=f)
        runner.run(suit)
        f.close()
    def run_all(self):
        suit=unittest.TestSuite()  #添加测试套件
        discover=unittest.defaultTestLoader.discover(r'c:\Users\admin\Desktop\xiaogege\删除购物车\hao_test',pattern='test*.py')
        #                                            测试用例所在的路径         匹配
        suit.addTest(discover)  #添加测试用例
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'c:\Users\admin\Desktop\xiaogege\删除购物车\report\abcd.html','wb')

        runner = HTMLTestRunnertest.HTMLTestRunner(tester='小哥哥',
                                                  description='测试结果如下:',
                                                  title='删除购物车测试报告',
                                                  stream=f)
        runner.run(suit)
        f.close()





