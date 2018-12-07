#/usr/bin/env python
# -*- coding:utf-8 -*-
# requests  第三方库需要下载
# 爬虫：又叫网络蜘蛛（spider)
# 模仿浏览器,根据自己制定的规则批量下载网络中的资源
#  正则表达式 ：匹配文件中的内容

# 模仿浏览器的模块 ： urllib,urllib3,requests

# 匹配内容的模块：re,bs4,xpath
# 爬虫分类：1.焦爬虫（只爬取某个网站的资源） 2.搜索爬虫（爬取某个网络中的资源）

#面向对象的代码
# 爬虫第一步：分析网址的变化
# 爬虫第二部：分析html文件 过滤并下载想要的资源
# 'https://www.qiushibaike.com/text/page/{}/'.format()
# import requests
# import re
# import xlwt
# #
# class Qiushi(object):
#
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
        #发送请求
        # response=requests.get(url=url)
        #读取结果的方式：
        # print(response.text)  #1.以字符串的方式读取
        # print(response.content.decode('utf-8')) #2.以字节码的方式读取
#
# class Qiushi(object):
#     def qingqiu(self, page):
#         url ='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         response=requests.get(url=url)
#         html=response.content.decode('utf-8')
#         return html
#     def goulv(self,abc):
#         shuju=[]
#         patt=re.compile('<div class="content">(.*?)</div>',re.S)
#         itmes=patt.findall(abc)
#         for i in itmes:
#             i=i.replace('<span>','')
#             i=i.replace('</span>','')
#             i=i.replace('<br/>','')
#             i=i.strip()
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8')as f:
#             for i in shuju:
#                 f.write(i+'\n')
# qiushi=Qiushi()
# jieguo=qiushi.qingqiu(1)
# shuju=qiushi.goulv(jieguo)
# qiushi.save(shuju)


# class a():
#     def aa(self,page):
#         url = 'https://book.douban.com/top250?start={}/'.format(page)
#         response = requests.get(url=url)
#         html = response.content.decode('UTF-8')
#         return html
#     def goulv(self,abc):
#         shuming=[]
#         patt1 = re.compile('title="(.*?)"', re.S)
#         itmes=patt1.findall(abc)
#         for i in itmes:
#             shuming.append(i)
#         # print(shuming)
#         return shuming
#     def goulv1(self,ac):
#         jieshao=[]
#         patt = re.compile('<span class="inq">(.*?)</span>', re.S)
#         itme = patt.findall(ac)
#         for j in itme:
#             jieshao.append(j)
#         # print(jieshao)
#         return jieshao
# qiushi=a()
# jieguo=qiushi.aa(0)
# sm=qiushi.goulv(jieguo)
# js=qiushi.goulv1(jieguo)
# print(sm)
# print(js)
    # def save(self,sm,js):
    #     f = xlwt.Workbook(encoding='utf-8')


# url = 'https://book.douban.com/top250?start={}/'.format(0)
# response = requests.get(url=url)
# html = response.content.decode('UTF-8')
# shuming = []
# jieshao=[]
# patt1 = re.compile('title="(.*?)"', re.S)
# itmes = patt1.findall(html)
# patt=re.compile('<span class="inq">(.*?)</span>',re.S)
# itme=patt.findall(html)
# for i in itmes:
#     shuming.append(i)
# for j in itme:
#     jieshao.append(j)
# print(jieshao)








# 导入正则模块  # 只能匹配字符串
# 贪婪模式：近可能多的去匹配最后的字符串  带*的是贪婪
# 非贪婪模式：近可能少的去匹配最后的字符串  带？的是非贪婪
# import re
# a="""qwe4
# 56qwe123qwe"""
# 将要匹配的正则编译
#.匹配任意一个字符，除了换行符

# b=re.compile('qwe(.{3})qwe')
# b=re.compile('qwe(.*?)qwe',re.S)    # 到目的字符串中去查找
# re.S让.可以匹配包括换行符在内的所有字符
# b=re.compile('QWE(.*?)qwe',re.I)
# re.I匹配的字符不区分大小写
#到目的字符串中去查找
# c=b.findall(a)
# print(c)



# import requests
# import re
#
# url='http://www.doutula.com/article/list/?page=2'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# response=requests.get(url=url,headers=head)
# html=response.content.decode('UTF-8')
# print(html)
# "http://www.doutula.com/article/detail/6032166"


# import requests
# import re
#
# # url='http://www.doutula.com/article/list/?page=1'
# # head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# # response=requests.get(url=url,headers=head)
# # html=response.content.decode('UTF-8')
# # patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# # items=patt.findall(html)
# #
# #
# # for i in items:
# #     response = requests.get(url=i, headers=head)
# #     html1 = response.content.decode('UTF-8')
# #     patt1=re.compile(r'<img src="https://ws(.*?) alt')
# #     items1=patt1.findall(html1)
# #
# #
# # for j,i in enumerate(items1):
# #     i=i.replace('"','')
# #     i='https://ws'+i
# #     #保存图片
# #     tupian=requests.get(i)
# #     res1=tupian.content
# #     with open ('{}.jpg'.format(j),'wb') as f:
# #         f.write(res1)
#
# # url='http://www.meizitu.com'
# # head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# # response=requests.get(url=url,headers=head)
# # html=response.content.decode('gbk')
# # patt=re.compile(r'<img src="http://mm.chinasareview.com/wp-content/uploads/2017a/07/[0-9]{2}/01.jpg" style="width:100%;" />')
# #
# # items=patt.findall(html)
# # print(items)
#
# # url='https://www.qqtn.com/tp/sgtp_1.html'
# # head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# # res=requests.get(url=url,headers=head)
# # html=res.content.decode('gbk')
# # patt=re.compile(r'<img src="(.*?).jpg" alt')
# # tupian=patt.findall(html)
# # print(tupian)
#
#
# #  QQ头像，背景图
# # class a():
# #     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# #     def qingqiu(self,page):
# #         url = 'https://www.qqtn.com/tx/weimeitx_{}.html'.format(page)
# #         res = requests.get(url=url, headers=head)
# #         html = res.content.decode('gbk')
# #         return html
# #     def guolv(self,html):
# #         tupian=[]
# #         patt = re.compile(r'<li><a href="(.*?)" target="_blank" title="', re.S)
# #         itmes = patt.findall(html)
# #         for i in itmes:
# #             i = i.replace("'", '')
# #             i = 'https://www.qqtn.com' + i
# #             res1 = requests.get(url=i, headers=head)
# #             html5 = res1.content.decode('gbk')
# #             patt2 = re.compile(r'<p align="center"><img src="(.*?)"/></p>', re.S)
# #             itme2 = patt2.findall(html5)
# #             for i in itme2:
# #                 tupian.append(i)
# #         return tupian
# #     def baocun(self,tupian):
# #         for i,j in enumerate(tupian):
# #             res=requests.get(url=j, headers=head)  #发送请求
# #             html2=res.content  #获取照片的二进制
# #             with open(r'E:\头像1\{}{}.jpg'.format(w,i),'wb') as f:
# #                 f.write(html2)
# # for w in range(1):
# #     beijingtu = a()
# #     bbb = beijingtu.qingqiu(w)
# #     ccc = beijingtu.guolv(bbb)
# #     beijingtu.baocun(ccc)
#
#
#
#
# #
#
#
# # class a():
# #     head={}
# #     def qingqiu(self):
# #         url=()
# #         res=requests.get(url=url,headers=head)
# #         html=res.content.decode('gbk')
# #         return html
# #     def guolv(self):
# #         patt=re.compile()
# #         patt=re.compile()
# #         itmes=patt.findall()
# #         for i in itmes:
# #             res1=requests.get(url=i)
# #             html1=res1.content.decode()
#
#
# # 客户端
# # import socket
# # #创建socket  封装协议
# # soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # #连接服务器  接收的参数元祖
# # soc.connect(('192.168.0.36',3000))
# # #发送请求
# # aaa='你好吗'
# # soc.send(aaa.encode('utf-8'))
# # #接收请求
# # msg=soc.recv(1024)
# # print(msg.decode('utf-8'))
#
#
#
#
#
#
# # import socket
# #  # 创建socket  封装协议
# # soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # #发送请求数据
# # a=('192.168.0.36',6666)
# # reg='你好吗'
# # soc.sendto(reg.encode('utf-8'),a)
# # #接收响应
# # c=soc.recv(1024)
# # print(c.decode('utf-8'))
#
#
#
#
# # import socket
# #  # 创建socket  封装协议
# # soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # #发送请求数据
# # while True:
# #
# #     a = ('192.168.0.36', 6666)
# #     input('输入')
# #     reg = '你好吗'
# #     soc.sendto(reg.encode('utf-8'), a)
# #     # 接收响应
# #     c = soc.recv(1024)
# #     print(c.decode('utf-8'))
#
#
# import socket
# soc=socket.socket(socket.Af_INET,socket.SOCK_STAEAM)
# soc.connect()
# reg=''
# soc.send(reg.encode('utf-8'))
# c=soc.recv(1024)
# print(c.decode('utf-8'))
#
# import socket
# soc=socket.socket
# a=()
# soc.bind(a)
# soc.listen(3)
# while Ture:
#     a,b=soc.accept()
#     msg=a.recv(1024)
#     print
#     reg=
#     soc.send(reg.encode('utf-8'))







# 图形化界面         tkinter(Python自带)     Gui     pygame
#  pillow   模块
# from tkinter import *
# from PIL import Image
# from PIL import ImageTk
# from tkinter import messagebox
# def closeWindow():
#     messagebox.showinfo(title='哈哈哈',message='不要嘛')
#     return
#
# def Love():
#     #顶级窗口：在window窗口的基础之上再新建一个窗口
#     love=Toplevel(window)
#     love.geometry('200x100+500+150')
#     label = Label(love,text='好巧，我也是!!!',font=('微软雅黑',20))
#     label.grid(row=0,column=0,sticky=W)
#     button1 = Button(love, text='爱你',width =13,height=2,command=closeallwindow)  # 设置宽和高width   宽    height   高
#     button1.grid(row=1, column=0, sticky=E)
#     love.mainloop()
# def NoLove():
#     nolove=Toplevel(window)
#     nolove.title('再考虑考虑')
#     nolove.geometry('150x100+700+150')
#     label = Label(nolove, text='呜呜呜呜呜', font=('微软雅黑', 20))
#     label.grid(row=0, column=0, sticky=W)
#     button = Button(nolove, text='确定',width =10,height=2,command=nolove.destroy)
#     button.grid(row=1, column=0, sticky=E)
#     nolove.protocol('WM_DELETE_WINDOW',closeWindow)
#                #WM_DELETE_WINDOW 事件名称   作用：不让关闭窗口
#                #逗号后面的函数名：指的是关闭窗口之后做的动作
#     nolove.mainloop()
# def closeallwindow():
#     window.destroy()
# #新建窗口
# window = Tk()
# #设置窗口的标题
# window.title('爱我嘛')
# #设置窗口出现的位置,第一个数字是x轴，第二个是y轴
# window.geometry('+500+150')
# #设置窗口的大小
# window.geometry('380x395')  #第一个是长，第二个是宽
# #window.geometry('400x400+500+150')    可以写在一起
# #定义一个文本框来写字（文本控件）
# label = Label(window,text = 'Hey,小姐姐',font=('微软雅黑',15))
# label.grid(row=0,column=0,sticky=W)   #grid  以网格的方式显示的
#                             ##sticky  对齐方式，以东西南北    东：E  西：W  南：S  北：N
# labe2 = Label(window,text = '喜欢我吗',font=('微软雅黑',20))
# labe2.grid(row=1,column=0,sticky=E)    #定义标签在窗口的位置，第一个数字是行，第二个是列，
#
# img = Image.open('cc.png')
# image = ImageTk.PhotoImage(img)
# # image = PhotoImage(file = 'cc.png')
# image_label = Label(window,image=image)
# image_label.grid(row=2,column=0)
# # 按钮标签,设置按钮，点击同意或者不同意
# button = Button(window,text='好的呀',width =13,height=2,command=Love)  # 设置宽和高width   宽    height   高
# button.grid(row=3,column=0,sticky=W)
# button1 = Button(window,text='滚呐',width =13,height=2,command=NoLove)
# button1.grid(row=3,column=0,sticky=E)
# #设置用户不允许点击关闭窗口事件
# window.protocol('WM_DELETE_WINDOW',closeWindow)
# #显示窗口
# window.mainloop()



#1.创建窗口      window = Tk()
#2.添加文本标签，设置文本信息和文本的位置
#3.添加图片
#4.添加按钮，按钮跳转
#5.关闭窗口

#在cmd
#打包  pyinstaller -F  文件名
# 去掉黑窗口     pyinstall  -F   -w  图形化界面.py



import requests
import re
import xlwt
# class zhilian():
#     def qinqiu(self):
#         a=['https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.01097835&x-zp-page-request-id=e0f56c50c62c4f84b5bfaec445247355-1541768917339-961731'
#                    ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.27393779&x-zp-page-request-id=7161854b4ce84b72a606216d33ca1a46-1541814546568-870708'
#                    ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.34573786&x-zp-page-request-id=5ca57d70af1245d688194da90a1acf7f-1541814748861-951786'
#                    ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=763&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.93934657&x-zp-page-request-id=da763ba5f7124d928d0c5be0471767b9-1541814818979-678695']
#         aa=[]
#         for i in a:
#             for j in range(0,180,60):
#                 kk=i.format(j)
#                 aa.append(kk)
#
#         zhiwei1=[]
#         xinzi1=[]
#         didian1=[]
#         time1=[]
#         renshu1=[]
#         jinyan1=[]
#         for dd in aa:
#             url=dd
#             head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#             response=requests.get(url=url,headers=head)
#             html=response.content.decode('utf-8')
#             zhiwei=re.compile(r'jobName":"(.*?)","',re.S)
#             xinzi=re.compile(r'"salary":"(.*?)","',re.S)
#             didian=re.compile(r'city":{"items":(.*?)"},"applyType',re.S)
#             time=re.compile(r'updateDate":"(.*?)","',re.S)
#             renshu=re.compile(r'size":{"(.*?)"},"type',re.S)
#             jinyan=re.compile(r'workingExp":{"(.*?)"},"eduLevel')
#
#             items=zhiwei.findall(html)
#             zhiwei1.append(items)
#             items1=xinzi.findall(html)
#             xinzi1.append(items1)
#             items2=time.findall(html)
#             time1.append(items2)
#             items3=renshu.findall(html)
#             renshu1.append(items3)
#             items4=didian.findall(html)
#             didian1.append(items4)
#             items5=jinyan.findall(html)
#             jinyan1.append(items5)
#         return   zhiwei1,xinzi1,didian1,time1,renshu1,jinyan1
#
#     def baocun(self,a,b,c,d,e,nn):
#         dd=1
#         f=xlwt.Workbook(encoding='utf-8')
#         sheet = f.add_sheet('智联')
#         sheet.write(0,0,'职位')
#         sheet.write(0,1,'薪资')
#         sheet.write(0,2,'公布时间')
#         sheet.write(0,3,'公司人数')
#         sheet.write(0,4,'公司地址')
#         sheet.write(0,5,'工作经验')
#         k = 1
#         m = 1
#         n = 1
#         aa = 1
#         bb = 1
#         cc = 1
#         for j in range(12):
#             for i in a[j]:
#                 sheet.write(k, 0, '{}'.format(i))
#                 k += 1
#         for j in range(12):
#             for i in b[j]:
#                 sheet.write(m, 1, '{}'.format(i))
#                 m += 1
#         for j in range(12):
#             for i in c[j]:
#                 sheet.write(n, 2, '{}'.format(i))
#                 n += 1
#         for j in range(12):
#             for i in d[j]:
#                 i = i.split('"')
#                 sheet.write(aa, 3, '{}'.format(i[-1]))
#                 aa += 1
#         for j in range(12):
#             for t in e[j]:
#                 t = t.split('"')
#                 sheet.write(bb, 4, '{}'.format(t[-1]))
#                 bb += 1
#         for j in range(12):
#             for ff in nn[j]:
#                 ff = ff.split('"')
#                 sheet.write(cc, 5, '{}'.format(ff[-1]))
#                 cc += 1
#
#         f.save('智联招聘.xls')
#
# aa=zhilian()
# a,b,c,d,e,nn=aa.qinqiu()
# aa.baocun(a,b,c,d,e,nn)

a=['https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.01097835&x-zp-page-request-id=e0f56c50c62c4f84b5bfaec445247355-1541768917339-961731'
           ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.27393779&x-zp-page-request-id=7161854b4ce84b72a606216d33ca1a46-1541814546568-870708'
           ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.34573786&x-zp-page-request-id=5ca57d70af1245d688194da90a1acf7f-1541814748861-951786'
           ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=763&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.93934657&x-zp-page-request-id=da763ba5f7124d928d0c5be0471767b9-1541814818979-678695']
aa=[]
for i in a:
    for j in range(0,180,60):
        kk=i.format(j)
        aa.append(kk)

zhiwei1=[]
xinzi1=[]
didian1=[]
time1=[]
renshu1=[]
jinyan1=[]
for dd in aa:
    url=dd
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response=requests.get(url=url,headers=head)
    html=response.content.decode('utf-8')
    zhiwei=re.compile(r'jobName":"(.*?)","',re.S)
    xinzi=re.compile(r'"salary":"(.*?)","',re.S)
    didian=re.compile(r'city":{"items":(.*?)"},"applyType',re.S)
    time=re.compile(r'updateDate":"(.*?)","',re.S)
    renshu=re.compile(r'size":{"(.*?)"},"type',re.S)
    jinyan=re.compile(r'workingExp":{"(.*?)"},"eduLevel')

    items=zhiwei.findall(html)
    zhiwei1.append(items)
    items1=xinzi.findall(html)
    xinzi1.append(items1)
    items2=time.findall(html)
    time1.append(items2)
    items3=renshu.findall(html)
    renshu1.append(items3)
    items4=didian.findall(html)
    didian1.append(items4)
    items5=jinyan.findall(html)
    jinyan1.append(items5)

f=xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('智联')
sheet.write(0,0,'职位')
sheet.write(0,1,'薪资')
sheet.write(0,2,'公布时间')
sheet.write(0,3,'公司人数')
sheet.write(0,4,'公司地址')
sheet.write(0,5,'工作经验')
k = 1
m=1
n=1
aa=1
bb=1
cc=1
for j in range(12):
    for i in zhiwei1[j]:
        sheet.write(k,0,'{}'.format(i))
        k+=1
for j in range(12):
    for i in xinzi1[j]:
        sheet.write(m,1,'{}'.format(i))
        m+=1
for j in range(12):
    for i in time1[j]:
        sheet.write(n,2,'{}'.format(i))
        n+=1
for j in range(12):
    for i in renshu1[j]:
        i=i.split('"')
        sheet.write(aa,3,'{}'.format(i[-1]))
        aa+=1
for j in range(12):
    for t in didian1[j]:
        t = t.split('"')
        sheet.write(bb,4,'{}'.format(t[-1]))
        bb+=1
for j in range(12):
    for ff in jinyan1[j]:
        ff = ff.split('"')
        sheet.write(cc,5,'{}'.format(ff[-1]))
        cc+=1


f.save('智联招聘.xls')
















































