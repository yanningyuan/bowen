#/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

# class 注册_摩尔():
#     def 注册(self,a):
#         # dr = webdriver.Chrome()
#         dr=webdriver.Firefox()
#
#         dr.get('http://www.moore.ren/')
#         dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
#         sleep(2)
#         wd = dr.window_handles
#         dr.switch_to_window(wd[-1])
#         sleep(2)
#         zhanghao=dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys("{}".format(a))
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('123456')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()
#         return zhanghao
#     def wenben(self,a):
#         dr = webdriver.Firefox()
#
#         dr.get('http://www.moore.ren/')
#         dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
#         sleep(2)
#         wd = dr.window_handles
#         dr.switch_to_window(wd[-1])
#         sleep(2)
#         zhanghao = dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys("{}".format(a))
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('123456')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()
#         wd2 = dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/span').text
#         return wd2


class 注册_摩尔():
    def 注册(self,a):
        # dr = webdriver.Chrome()
        dr=webdriver.Firefox()
        dr.get('http://www.moore.ren/')
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
        sleep(2)
        wd = dr.window_handles
        dr.switch_to_window(wd[-1])
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
        sleep(2)
        youxiang = dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys("{}".format(a))
        # youxiang = dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('hini@mooreelite.com')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456')
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[3]/form/input[7]').click()
        sleep(2)
        wd1=dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[3]/form/div[1]/span').text
        return youxiang,wd1


