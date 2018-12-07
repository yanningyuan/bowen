#/usr/bin/env python
# -*- coding:utf-8 -*-
#读取excel表格
# import xlrd
#打开一个文件
# f=xlrd.open_workbook('text.xls')

#  两种获取标签页的方式

#1.通过索引来获取
# sheet=f.nsheets  #获取总共有多少个标签页
# sheet=f.sheets()[0]   #s索引获取标签页
# print(sheet.nrows)  #获取文件中有多少行
#
# print(sheet.row_values(0))   #row_values()  读取第几行的内容，第一行从0开始
# a=sheet.nrows
# for i in range(a):
#     print(sheet.row_values(i))


# print(sheet.ncols)    #获取有多少列
# print(sheet.col_values(1))      #读取第几列的内容，第一列从0开始
# print(sheet.cell(0,2).value)    #读取某一个单元格的内容

#2.通过标签页的名称
# print(f.sheet_names())  #获取所有标签页的名称
# sheet=f.sheet_by_name('python操作excel表格')


#excel表格的追加
# import xlrd
#
# from xlutils.copy import copy
# f=xlrd.open_workbook('text.xls')
#  复制文件
# new_f=copy(f)
#  操作复制的文件
# a=new_f.get_sheet(0)
#
# a.write(4,4,'哈哈哈')
# new_f.save('text.xls')


#   封装了ssh协议   作用：远程连接
# import paramiko

#创建一个ssh客户端
# ssh123=paramiko.SSHClient()
#  将要连接的主机添加到 know_host 文件中
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh123.connect(hostname='192.168.0.21',
#                port=22,
#                username='root',
#                password='123456')
# 执行命令  产生三个结果
# stuin,stuout,stuerr=ssh123.exec_command('ping -c 3 192.168.0.199')
# # 第一个变量：执行的命令，输入
#第二个变量：命令的结果，输出
#第三个变量：命令的报错

#输入的命令只能是有结果的命令
# print(stuout.read().decode())
# ssh123.close() #断开连接

# while True:
#         a=input('输入你要用的命令，断开连接输入exit')
#         stuin,stuout,stuerr = ssh123.exec_command(a)
#         print(stuout.read().decode())
#         # ssh123.close()
#         if a=='exit':
#             break




# import paramiko
#创建一个传输通道
# ssh123=paramiko.Transport(('192.168.0.21',22))
# ssh123.connect(username='root',password='123456')

#  传输文件使用sftp协议，  创建一个sftp实例
# sftp=paramiko.SFTPClient.from_transport(ssh123)

#  get 是从linux下载文件到本地
# sftp.get('anaconda-ks.cfg','./a.cfg')

#  put是从本地向linux 上传文件
# sftp.put('a.txt','/etc/aa.py')


# import smtplib  #  发送邮件的协议
# import email.mime.text  #处理发送的内容
# import email.mime.multipart  # 处理邮件的表头
# sender='15237873020@163.com'  #发送者
# recver='1335859763@qq.com'  #接收者
# server='smtp.163.com'   #服务器地址
# passwd='yny19970312'   #授权码
# # 创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #发件人
# message['from']=sender
# #收件人
# message['to']=recver
# #主题
# message['subject']='白晓媛大傻子'
# #正文
# text="""
# 好好学习
# 你是最菜的
# 你在每日
# 掉发
# 的道路上
# 越走越远
#"""
#处理文本信息
# text=email.mime.text.MIMEText(text)
# #将处理后的信息添加到邮件里
# message.attach(text)
# #定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(sender,passwd)
# #发送邮件
# smtp123.sendmail(sender,recver,message.as_string())
# #断开连接
# smtp123.close()

#带附件的
# text=email.mime.text.MIMEText(text)
# #将处理后的信息添加到邮件里
# message.attach(text)
# att2=email.mime.text.MIMEText(open('转换.py','rb').read(),'base64','utf-8')
# att2["Content-Type"]='applicacation/octet-stream'
# att2["Content-Disposeition"]='attachment;filename="shazi.py"'
# message.attach(att2)
# #定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(sender,passwd)
# #发送邮件
# smtp123.sendmail(sender,recver,message.as_string())
# #断开连接
# smtp123.close()

# import time
# 时间戳   代表从公元1970年到现在经过的 秒数
# print(time.time())

# 本地时间  元组   默认显示的是当前时间
# print(time.localtime())

#  格式化成现代的时间
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime()))
# print(time.strptime('1970 6 6','%Y %m %d'))

# a=time.strptime('1970 6 6','%Y %m %d')
# # 将元组时间转化为时间戳
# print(time.mktime(a))

#休眠
# time.sleep(3)
# print(1)        
# a= input(">>输入年月日>>")
# b= time.strptime("{}".format(a),'%Y %m %d')
# if (b[0]%4 == 0 and b%100 != 0) or b%400 == 0:
#     time.sleep(2)
#     print('{}是闰年,今天是星期{}，是一年中的第{}天'.format(b[0],b[6]+1,b[7]))
# else:
#     time.sleep(2)
#     print('{}是平年,今天是星期{}，是一年中的第{}天'.format(b[0],b[6]+1,b[7]))

















































