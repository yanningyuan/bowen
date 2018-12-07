#/usr/bin/env python
# -*- coding:utf-8 -*-
#获取浏览器的地址
#print(dr.current_url)
#保证所有的测试用例在同一环境下测试
#
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()  #打开浏览器
# dr.get('http://www.baidu.com')  # 请求网址
# sleep(2)
# # 通过id属性定位   定位到ID等于kw的位置
# dr.find_element_by_id('kw').send_keys('摩尔精英')
# sleep(2)
# dr.find_element_by_id('su').click()

#通过class属性定位  定位到class=s_ipt 的位置
# dr.find_element_by_class_name('s_ipt').send_keys('美女')


# 通过name属性定位   定位到name=wd的位置
# dr.find_element_by_name('wd').send_keys('美女')

#link_text  通过文本定位  保证定位元素的唯一性
# df.find_element_by_link_text('企业').click




#获取网站的标题（title）
# print(dr.title) #通常用来做断言
# 设置浏览器大小
# dr.set_window_size(200,200)
#设置浏览器的位置
# dr.set_window_position(500,500)
# dr.maximize_window()  #浏览器最大化
# dr.minimize_window()  #浏览器最小化
# dr.get('http://www.jd.com')
# sleep(3)
# dr.back()  # 后退
# sleep(3)
# dr.forward() # 前进
# dr.quit()  #关闭浏览器

#link_text  通过文本定位  保证定位元素的唯一性
# df.find_element_by_link_text('企业').click

#partial_link_text   通过模糊文本来定位
# dr.find_element_by_partial_link_text('登').click()

#tag_name  通过标签名称去定位
# dr.find_element_by_tag_name('').click()
# dr.find_element_by_xpath('').click()
# 通过xpath路径定位



# 摩尔精英
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

# dr = webdriver.Chrome()
# dr=webdriver.Firefox()  #打开浏览器
# dr.get('http://www.moore.ren/login/login.htm')  # 请求网址
# sleep(2)
# dr.get('http://www.moore.ren/')

# sleep(2)
# 通过id属性定位   定位到ID等于kw的位置
# dr.find_element_by_id('emailInput').send_keys('1124260878@qq.com')
# # sleep(2)
# dr.find_element_by_id('passwordInput').send_keys('yny19970312')
# sleep(2)

#通过xpath
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(5)

#link_text  通过文本定位  保证定位元素的唯一性
# dr.find_element_by_link_text('企业').click()


#partial_link_text   通过模糊文本来定位
# dr.find_element_by_partial_link_text('登').click()


# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[1]/a').click()

# wd=dr.find_elements_by_class_name('menu-box')
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


# dr.get('http://www.jd.com')
# sleep(2)
# wd=dr.find_elements_by_class_name('cate_menu_item')
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

#层级定位
# wd=dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul').find_elements_by_tag_name('li')
# print(len(wd))
# dr.quit()  #关闭浏览器

#
# wd=dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[5]/ul[1]/li[1]/a')
# print(wd.get_attribute('href'))  #(获取某元素下标的值)

# dr.get('http://192.168.0.254')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# f=[]
# for i in range(1,5):
#     a=dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i)).get_attribute('src')
#     patt = re.compile(r'/imgs/(.*?).gif')
#     # print(patt)
#     i = patt.findall(a)
#     # print(i)
#     f.append(i[0])
# dr.find_element_by_xpath('//*[@id="input1"]').send_keys(f)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd=dr.switch_to_alert()  #切换弹出框
# print(wd.text)  #获取弹出框上边的文本
# wd.accept()   #点击确定


# dr.get('http://www.ctrip.com')
# dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
# sleep(2)
# for i in range(1,11):
#     dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
#     sleep(2)
#     dr.find_element_by_xpath('// *[ @ id = "J_roomCountList"] / option[{}]'.format(i)).click()
#     sleep(2)
# dr.quit()

# dr.get('http://www.moore.ren/')
# print(dr.current_window_handle)  #获取当前窗口的句柄
# # print(dr.window_handles)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]/a').click()
# sleep(2)
# print(dr.window_handles)
# wd=dr.window_handles   #  获取所有窗口的句柄
# dr.switch_to.window(wd[-1])   #  切换当前窗口的句柄  dr.switch_to_window(wd[-1])
# sleep(2)
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('1124260878@qq.com')



#  喔影网络科技有限公司
# http://www.alltuu.com/login?url=http://www.alltuu.com/v
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()  #打开浏览器
# dr.get('http://www.alltuu.com/login?url=http://www.alltuu.com/v')  # 请求网址
# sleep(2)
# # 通过id属性定位   定位到ID等于kw的位置
# dr.find_element_by_id('loginUsername').send_keys('15237873020')
# sleep(2)
# dr.find_element_by_id('loginUsername').send_keys('15237873020')
# sleep(2)
# dr.find_element_by_xpath('/html/body/ul/li[1]').click()
# sleep(2)
# # wd=dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
# for i in wd:
#     if '.com' not in i.text:
#         i.click()
# # dr.quit()

# dr.find_element_by_id('loginPassword').send_keys('yny19970312')
# sleep(2)
# dr.find_element_by_id('main').click()
# sleep(2)
# dr.find_element_by_id('login').click()
# sleep(5)
# dr.quit()  #关闭浏览器


# dr.get('https://qzone.qq.com')
# sleep(2)
# 只能根据：id属性的值  或者name属性的值  定位到框架
# dr.switch_to.frame()  #切换到内嵌框架中

# dr.switch_to.default_content()  #退出到原始的页面  退出框架
# dr.switch_to.parent_frame()  #   切换到上一层的框架
# # 定位到框架
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')
# sleep(2)
# dr.switch_to.frame(wd)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1124260878')
# sleep(2)
# #  id
# dr.switch_to.frame('login_frame')
# #  name
# dr.switch_to.frame('login_frame')



#
# dr.get('http://192.168.0.254')
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
#  #  弹出框(alert)
# wd=dr.switch_to_alert()  #切换弹出框
# print(wd.text)  #获取弹出框上边的文本
# wd.accept()   #点击确定
# wd.dismiss()   #点击取消
# wd.send_keys('输入内容')  #向弹出框中输入内容



# dr.get('https://mail.qq.com/cgi-bin/loginpage')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1124260878')


# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# f=[]
# for i in range(1,5):
#     a=dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i)).get_attribute('src')
#     patt = re.compile(r'/imgs/(.*?).gif')
#     # print(patt)
#     i = patt.findall(a)
#     # print(i)
#     f.append(i[0])
# dr.find_element_by_xpath('//*[@id="input1"]').send_keys(f)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd=dr.switch_to_alert()  #切换弹出框
# wd.accept()


# wd2=dr.find_element_by_xpath('//*[@id="Content"]')
# dr.switch_to_frame(wd2)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="04"]').click()
#  切换内嵌框
# wd2=dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
# dr.switch_to_frame(wd2)
# dr.find_element_by_xpath('//*[@id="04_image"]').click()  # 防火墙
# sleep(2)
# dr.find_element_by_xpath('//*[@id="041"]/span').click()  #策略
# sleep(2)
# #  返回初始框
# dr.switch_to.default_content()
# sleep(2)
# wd1=dr.find_element_by_xpath('//*[@id="main"]')
# dr.switch_to_frame(wd1)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
# sleep(2)
# # wd4=dr.find_element_by_xpath('//*[@id="Content"]/frameset/frame[1]').click()


# wd=dr.find_elements_by_xpath('//*[@id="0_wrap"]').find_elements_by_xpath('//*[@id="04"]').find_elements_by_tag_name('div')
# for i in wd:
#     if '防火墙'  in i.text:
#         i.click()
# dr.find_elements_by_xpath('//*[@id="0_wrap"]')

# dr.get('http://www.alltuu.com')
# sleep(2)
#  移动滚动条  属于浏览器的，不属于当前访问的页面   JavaScript语言

#  var q=document.documentElement.scrollTop=10000
#  10000表示的事当前页面
# 控制滚动条的JavaScript代码
#
# js='var q=document.documentElement.scrollTop=10000'
# dr.execute_script(js)  #执行JavaScript

#  2.根据定位到的元素   移动滚动条
#  定位一个元素
# wd=dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[1]/p[1]')
#
#
# js="arguments[0].scrollIntoView();"
# dr.execute_script(js,wd)


#  拖拽
# dr.get('http://qzone.qq.com')
# sleep(2)
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')
# sleep(2)
# dr.switch_to.frame(wd)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1124260878')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('wef')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
#
# wd1=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(wd1)
# sleep(2)
# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ActionChains(dr).drag_and_drop_by_offset(start,200,0).perform()
# sleep(4)
# dr.quit()
# /html/body/div[1]/div[11]/div[2]/iframe
# //*[@id="login_frame"]


# end=dr.find_element_by_xpath('/html/body/div[1]/div[3]/div[6]/div[1]')


# dr = webdriver.Chrome()
# # dr=webdriver.Firefox()
#
# dr.get('http://www.moore.ren/')
#
# #  强制等待
# sleep(2)
#
# #  智能等待   设置控制器dr等待
# # wait = ui.WebDriverWait(dr, 10)
# # wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())
#
# wait=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed()
# # is_displayed()   判断元素是否显示   结果：  True   Flase
# # is_enabled()     判断元素是否为灰化状态
#
# print(wait)
#
# # dr.quit()
#
#
# dr.get_screenshot_as_file('abc.png')    #截图并保存
#
#
# dr.get_screenshot_as_png()
# dr.save_screenshot('aaa.png')   #保存截图
#











