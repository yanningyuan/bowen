#/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

dr = webdriver.Chrome()
# dr=webdriver.Firefox()

dr.get('http://www.moore.ren/')
sleep(2)
dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
wd=dr.window_handles
dr.switch_to_window(wd[-1])
dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys('112426087')
















