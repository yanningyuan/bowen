#/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class 空间_登录():
    def yanzheng(self,a,b):
        dr = webdriver.Chrome()
        dr.get('http://qzone.qq.com')
        sleep(2)
        wd = dr.find_element_by_xpath('//*[@id="login_frame"]')
        sleep(2)
        dr.switch_to.frame(wd)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        zhanghao=dr.find_element_by_xpath('//*[@id="u"]').send_keys("{}".format(a))
        sleep(2)
        mima=dr.find_element_by_xpath('//*[@id="p"]').send_keys("{}".format(b))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)

        # wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
        # dr.switch_to_frame(wd1)
        # sleep(2)
        # start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        # ActionChains(dr).drag_and_drop_by_offset(start, 190, 0).perform()
        # sleep(2)
        # wd2 = dr.find_element_by_xpath('//*[@id="aMainPage"]/span').text
        try:
            wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
            dr.switch_to_frame(wd1)
            sleep(2)
            start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
            ActionChains(dr).drag_and_drop_by_offset(start, 187, 0).perform()
            sleep(2)
        except:
            pass
        wd2 = dr.find_element_by_xpath('//*[@id="aMainPage"]/span').text
        sleep(2)
        return wd2
    def yanzheng1(self,a,b):
        # dr = webdriver.Firefox()
        dr = webdriver.Chrome()
        dr.get('http://qzone.qq.com')
        sleep(2)
        wd = dr.find_element_by_xpath('//*[@id="login_frame"]')
        sleep(2)
        dr.switch_to.frame(wd)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)

        wd3 = dr.find_element_by_xpath('//*[@id="title_2"]').text
        sleep(2)
        zhanghao = dr.find_element_by_xpath('//*[@id="u"]').send_keys("{}".format(a))
        sleep(2)
        mima = dr.find_element_by_xpath('//*[@id="p"]').send_keys("{}".format(b))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)

        # wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
        # dr.switch_to_frame(wd1)
        # sleep(2)
        # start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        # ActionChains(dr).drag_and_drop_by_offset(start, 190, 0).perform()
        try:
            wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
            dr.switch_to_frame(wd1)
            sleep(2)
            start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
            ActionChains(dr).drag_and_drop_by_offset(start, 187, 0).perform()
            sleep(2)
        except:
            pass

        return wd3
    # def 添加购物车(self):
    #         dr = webdriver.Chrome()
    #         dr.get('https://item.jd.com/26689180344.html?jd_pop=41dec140-c10d-4ab9-9d0f-c0830f1cce24&abt=0')
    #         sleep(2)
    #         dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
    #         sleep(2)
    #         txt = dr.find_element_by_xpath('//*[@id="result"]/div/div/div[1]/div[1]/h3').text
    #         return txt






