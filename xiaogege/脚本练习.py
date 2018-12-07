#/usr/bin/env python
# -*- coding:utf-8 -*-

# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('>>'))
# f=''
# while True:
#     c=b%16


import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
dr = webdriver.Firefox()

dr.get('http://www.moore.ren/')
dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
sleep(2)
wd = dr.window_handles
dr.switch_to_window(wd[-1])
sleep(2)
zhanghao = dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys('18674687')
sleep(2)
dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('123456')
sleep(2)
dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()

wd2 = dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[2]/form/div[1]/span').text
print(wd2)






































