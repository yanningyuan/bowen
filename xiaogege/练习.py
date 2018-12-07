#/usr/bin/env python
# -*- coding:utf-8 -*-
#  客户端
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# import sockect
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect('192.168.0.56',3000)
# aaa='你好吗'
# soc.send(aaa.encode('utf-8'))
#
# c=soc.recv(1024)
# print(c.decode('utf-8'))
#
#
# # 服务器
# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('192.168.0.56',3000)
#
# soc.bind(a)
# soc.listen(3)
# while True:
#     a,b=accept()
#     reg=a.recv(1024)
#     paint(reg.decode('utf-8'))
#     meg='welcome'
#     print(meg.encode('utf-8'))
#
#
#
# #  udp  客户端
# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.56',3000)
# reg='你好吗'
# soc.sendto(reg.encode('utf-8'),a)
# c=soc.recv(1024)
# print(c.decode('utf-8'))
#
#
# #  服务器
#
# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.56',3000)
# soc.bind(a)
# while True:
#     a,b=soc.recvfrom(1024)
#     print(a.decode('utf-8'))
#     print(b)
#     reg='welcome'
#     soc.sendto(reg.encode('utf-8'),b)
#
#
#
#
# import  socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_STAEAM)
# soc.connect('192.168.0.56',3000)
# aaa='你好吗'
# soc.send(aaa.encode('utf-8'))
# c=soc.revc(1024)
# print(c.decode('utf-8'))
#
#
# soc=socket.socket(socket.AF_INET,socket.SOCK_STAEAM)
# a=('192.168.0.56',3000)
# soc.bind(aaa)
# soc.listen(3)
# while True:
#     a,b=accept()
#     reg=a.recv


# dr = webdriver.Chrome()
# dr.get('http://qzone.qq.com')
# sleep(2)
# wd = dr.find_element_by_xpath('//*[@id="login_frame"]')
# sleep(2)
# dr.switch_to.frame(wd)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# # zhanghao = dr.find_element_by_xpath('//*[@id="u"]').send_keys('1124260878')
# # sleep(2)
# # mima = dr.find_element_by_xpath('//*[@id="p"]').send_keys('yny19970312')
# # sleep(2)
# # dr.find_element_by_xpath('//*[@id="login_button"]').click()
# # sleep(2)
#
# # wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# # dr.switch_to_frame(wd1)
# # sleep(2)
# # start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# # ActionChains(dr).drag_and_drop_by_offset(start, 187, 0).perform()
# # sleep(2)
# #
# # wd2 = dr.find_element_by_xpath('//*[@id="aMainPage"]/span').text
# # sleep(2)
# wd3 = dr.find_element_by_xpath('//*[@id="title_2"]').text
# sleep(2)
# print(wd3)



import requests
import re
import xlwt
import pymysql
url='https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&scity=101010100&industry=&position='
head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
response=requests.get(url=url,headers=head)
html=response.content.decode('utf-8')


patt1=re.compile(r'<div class="job-title">(.*?)</div>')
patt2=re.compile(r'<span class="red">(.*?)</span>')
patt3=re.compile(r'target="_blank">(.*?)</a></h3>')
patt4=re.compile(r'div class="info-detail"></div>(.*?)</em>',re.S)
zhiwei=patt1.findall(html)


xinzi=patt2.findall(html)
gsm=patt3.findall(html)
didian=patt4.findall(html)
dian=[]


for i in didian:
    patt7=re.compile('<p>(.*?)<em class="vline">')
    didian1=patt7.findall(i)
    dian.append(didian1)

abc=pymysql.connect(host='192.168.0.182',port=3306,user='root',password='654321',charset='utf8')
aa=abc.cursor()
# aa.execute('')
aa.execute('use python4;')

# aa.execute('drop table 考试;')
aa.execute('create table biao4({} varchar(3000),{} varchar(2555),{} varchar(255),{} varchar(255));'.format('公司名称','地点','职位','薪资'))
for i in range(29):
    aa.execute('insert into biao4 values("{}","{}","{}","{}");'.format(gsm[i],dian[i],zhiwei[i],xinzi[i]))
abc.commit()









