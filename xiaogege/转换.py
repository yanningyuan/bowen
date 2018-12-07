#  import pymysql
# # abc=pymysql.connect(host='192.168.0.21',port=3306,user='root',password='977521',charset='utf8')
# # aaa=abc.cursor()

# 1.   数据库转a.txt
# import pymysql
# conn=pymysql.connect(host='192.168.0.199',port=3306,user='root',password='sz960828',charset='utf8')
# aaa=conn.cursor()
# aaa.execute('show databases;')
# aaa.execute('use shujuku;')
# aaa.execute('select * from biao1;')
# shuju=aaa.fetchall()
# aaa.execute('desc biao1')
# biaotou=aaa.fetchall()
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             f.write(biaotou[i][0])
#         else:
#             f.write(biaotou[i][0]+',')
#     for j in shuju:
#         f.write('\n'+'{},{}{}'.format(j[0],j[1],j[2]))



# import pymysql
# conn=pymysql.connect(host='192.168.0.130',port=3306,user='root',password='123456',charset='utf8')   #连接数据库
# aaa=conn.cursor()    #创建游标
# 对数据库进行操作
# aaa.execute('use shujuku;')
# aaa.execute('select * from biao3;')
# b=aaa.fetchall()
# # print(len(b))
# print(b)
# # print(b[0])
# # print(b[1])
# # print(b[2])
# aaa.execute('desc biao3;')
# biaotou=aaa.fetchall()
# print(biaotou[0][0])
# # 对txt文档进行操作
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             f.write(biaotou[i][0])
#         else:
#             f.write(biaotou[i][0] + ',')
#     for j in b:                                #大循环循坏一次，小循环，循坏一轮
#         for k in range(len(j)):
#             if k==0:
#                 f.write('\n'+j[k]+',')
#             elif k==len(j)-1:
#                 f.write(j[k])
#             else:
#                 f.write(str(j[k])+',')


# 2. a.txt转数据库
# import pymysql
# conn=pymysql.connect(host='192.168.0.22',port=3306,user='root',password='sz960828',charset='utf8')
# with open ('a.txt','r',encoding='utf-8') as f:
#     a=f.readline()
#     b=a.split(',')
#     print(b)
#     c=f.read()
#     d=c.split('\n')
#     print(d)
# aaa=conn.cursor()
# aaa.execute('use shujuku;')
# # aaa.execute('create table biao({} char(30),{} int,{} char(30));'.format(b[0],b[1],b[2]))
# for j in range(1,30):
#     e=d[j-1].split(',')
#     aaa.execute('insert into biao values("{}","{}","{}");'.format(e[0],int(e[1]),e[2]))
# conn.commit()
# aaa.execute('select * from biao')
# print(aaa.fetchall())





# 3. 文件转excel
# import xlwt
# with open ('a.txt','r',encoding='utf-8') as f:
#     a=f.readline()
#     b=a.split(',')
#     # print(b)
#     c=f.read()
#     d=c.split('\n')
# e=xlwt.Workbook.(encoding='utf-8')
# sheet=e.add_sheet('文件导入表格')
# for i,j in enumerate(b):
#     print(j)
#     sheet.write(0,i,j)
#
# for k,m in enumerate(d):

#     o=m.split(',')
    # print(o)
#     for n in range(len(o)):
#         sheet.write(k+1,n,o[n])
# e.save('text.xls')



# 4 .excel转文件0
# import xlrd
# #对表格的操作
# f=xlrd.open_workbook('text.xls')
# sheet=f.nsheets   #获取有多少个标签页
# sheet=f.sheets()[0]   #索引获取标签页
# b=sheet.nrows   #有多少行
# c=sheet.row_values(0)   #显示第0行的内容
# d=len(c)   #统计0行里有多少个元素
# print(d)
# print(c)
#对文件进行操作
# with open('a.txt','w',encoding='utf-8') as e:
#     for i in range(d):
#         if i==d-1:
#             e.write(c[i])
#         else:
#             e.write(c[i] + ',')
#
#     for k in range(1,b):  # 显示所有的内容
#         m=sheet.row_values(k)

        # for j in range(len(m)):
        #     if j==len(m)-1:
        #         e.write(m[j]+'\n')
        #     else:sssssssssssss
        #         e.write(m[j]+',')


# 5.数据库转excel

####②数据库到Excel
# import pymysql   #前提
# #连接数据库
# abc=pymysql.connect(host="192.168.0.182",
#               port=3306,
#               user="root",
#               password="654321",
#               charset="utf8")
# #创建游标
# aaa = abc.cursor()
# aaa.execute("use python1;")
# aaa.execute("desc biao1")
# biaotou=aaa.fetchall()
# print(biaotou)
# aaa.execute("select * from biao1")
# shuju=aaa.fetchall()
# import xlwt
# f=xlwt.Workbook(encoding="utf-8")
# sheet=f.add_sheet("数据库到Excel")
# for i in range(len(biaotou)):
#     sheet.write(0,i,biaotou[i][0])
# for d,j in enumerate(shuju):
#     for k in range(len(j)):
#         sheet.write(d+1,k,j[k])
# f.save("text11.xls")




# 6. excel转数据库2
# import xlrd
# import pymysql
# conn=pymysql.connect(host='192.168.0.129',port=3306,user='root',password='123456',charset='utf8')
# # 对表格的操作
# f=xlrd.open_workbook('text.xls')  #打开excel表格
# sheet=f.sheets()[0]    #  获                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            取标签页
# a=sheet.nrows  #  获取有多少行
# b=sheet.row_values(0)   # 获取第0行的内容

# aaa=conn.cursor()
# aaa.execute('create database shujuku1;')
# aaa.execute('use shujuku1')
# aaa.execute('create table biao1({} char(255),{} char(255),{} char(255));'.format(b[0],b[1],b[2]))
#
# for i in range(1,a):    #  显示所有的内容
#     shuju=sheet.row_values(i)
#     aaa.execute('insert into biao1 values("{}","{}","{}");'.format(shuju[0], int(shuju[1]), shuju[2]))


