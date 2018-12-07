# str  字符串
# 1.不可变的  2.支持通过下标位置取值 3.支持切片
# list  列表
# 以中括号为标识，以逗号隔开 [ 1,2,3]
# 1.可变的  2.支持索引  3.支持切片
# tuple  元组
# 以小括号为标识，以逗号隔开
# 1.不可变的 2.支持索引 3.支持切片
# dict  字典
# 以大括号为标识，以逗号隔开
# a={'name':'小明','age':18}
# 1.可变的 2.无序的 3.不支持索引
# set  集合
# 以大括号标识，以逗号分隔开
# 1.不重复的 2.无序的  3.不支持索引

def gouwuche(a):
    b = [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20},
         {'name': '美女', 'price': 998}]
    for i, j in enumerate(b):
        print(i + 1, j)
    c = []
    for d in range(1, 10):
        e = int(input('大兄弟买啥就点啥，买完按5'))
        if e < 5:
            c.append(e)
        if e == 5:
            print('小哥哥，结账')
            break
def chongzhi(h):
            for k in range(h):
                l = int(input('卖身换的钱'))
                a += l
                m = int(input('1继续卖身2虚了不卖了'))
                if m == 1:
                    print('扁扁的钱包')
                    print(a)
                    continue
                if m == 2:
                    print('哼，卖身后有钱了')
                    print(a)
                break
def goumai(a):
        print('商品价格')
        print(s)
        print('余额')
        print(a - s)
        print('好开心哟，又把购物车清了')





 