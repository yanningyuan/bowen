#/usr/bin/env python
# -*- coding:utf-8 -*-


# 图形化界面         tkinter(Python自带)     Gui     pygame
#  pillow   模块
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
def closeWindow():
    messagebox.showinfo(title='留下',message='眼睛不好还想跑')
    return

def Love():
    #顶级窗口：在window窗口的基础之上再新建一个窗口
    love=Toplevel(window)
    love.geometry('190x75+500+150')
    label = Label(love,text='真有眼光',font=('微软雅黑',20))
    label.grid(row=0,column=0,sticky=W)
    button1 = Button(love, text='么么哒',width =10,height=1,command=closeallwindow)  # 设置宽和高width   宽    height   高
    button1.grid(row=3, column=1, sticky=E)
    love.mainloop()
def NoLove():
    nolove=Toplevel(window)
    nolove.title('莫得生存欲望')
    nolove.geometry('220x90+700+150')
    label = Label(nolove, text='自己选择一种死法', font=('微软雅黑', 20))
    label.grid(row=0, column=0, sticky=W)
    button = Button(nolove, text='蠢死',width =10,height=2,command=nolove.destroy)
    button.grid(row=1, column=0, sticky=E)
    nolove.protocol('WM_DELETE_WINDOW',closeWindow)
               #WM_DELETE_WINDOW 事件名称   作用：不让关闭窗口
               #逗号后面的函数名：指的是关闭窗口之后做的动作
    nolove.mainloop()
def closeallwindow():
    window.destroy()



#新建窗口
window = Tk()
#设置窗口的标题
window.title('爱我嘛')
#设置窗口出现的位置,第一个数字是x轴，第二个是y轴
window.geometry('+500+150')
#设置窗口的大小
window.geometry('367x760')  #第一个是长，第二个是宽
#window.geometry('400x400+500+150')    可以写在一起
#定义一个文本框来写字（文本控件）
label = Label(window,text = '阿姨,看这里',font=('微软雅黑',15))
label.grid(row=0,column=0,sticky=W)   #grid  以网格的方式显示的
                            ##sticky  对齐方式，以东西南北    东：E  西：W  南：S  北：N
labe2 = Label(window,text = '花花是小仙女吗',font=('微软雅黑',20))
labe2.grid(row=1,column=0,sticky=E)    #定义标签在窗口的位置，第一个数字是行，第二个是列，

img = Image.open('cc.png')
image = ImageTk.PhotoImage(img)
# image = PhotoImage(file = 'cc.png')
image_label = Label(window,image=image)
image_label.grid(row=2,column=0)
# 按钮标签,设置按钮，点击同意或者不同意
button = Button(window,text='是呀',width =13,height=2,command=Love)  # 设置宽和高width   宽    height   高
button.grid(row=3,column=0,sticky=W)
button1 = Button(window,text='那必须不是',width =13,height=2,command=NoLove)
button1.grid(row=3,column=0,sticky=E)
#设置用户不允许点击关闭窗口事件
window.protocol('WM_DELETE_WINDOW',closeWindow)
#显示窗口
window.mainloop()



#1.创建窗口      window = Tk()
#2.添加文本标签，设置文本信息和文本的位置
#3.添加图片
#4.添加按钮，按钮跳转
#5.关闭窗口

#在cmd
#打包  pyinstaller -F  文件名
# 去掉黑窗口     pyinstall  -F   -w  图形化界面.py


# socket:套接字，提供了网络间通讯的基本功能(向网络发送请求、应答网络请求)
# server 端
# import socket
# #  创建socket  封装协议(ipv4协议)
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定ip和端口号  bind 接收的参数是元组
# a=('192.168.0.36',3000) # 三中地址
# s.bind(a)
# # 监听   数字指  最大等待数
# s.listen(3)
# while True:
#     #接收请求
#     a,b=s.accept()   #  第一个结果a:是客户端的连接信息
#                      #  第二个结果b:客户端的Ip地址
#     #接收数据
#     msg=a.recv(1024)  #  1024  每次接收到的最大字节数
#     print(msg.decode('utf-8'))
#     #发送响应
#     reg='welcome'
#     a.send(reg.encode('utf-8'))




# import socket
# #  创建socket  封装协议(ipv4协议)
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 绑定ip和端口号  bind 接收的参数是元组
# a=('192.168.0.36',6666) # 三中地址
# s.bind(a)
# while True:
#     #接收数据
#     a,b=s.recvfrom(1024)  #  第一个结果a:客户端发送的请求数据
#                           #  第二个结果b:客户端的IP地址和端口号
#     print(a.decode('utf-8'))
#     print(b)
#     #发送响应数据
#     msg='welcome'
#     s.sendto(msg.encode('utf-8'),b)  #括号中前面代表发送的数据，后面代表发送给谁


















