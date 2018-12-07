#/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


class 删除_购物车():
    def 删除(self, a,b):
        querystring = {"uid": "{}".format(a), "pid": "{}".format(b)}

        url = "http://www.zhaoapi.cn/product/deleteCart"

        # querystring = {"uid": "977", "pid": "8"}

        # payload = "undefined="
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            # 'cache-control': "no-cache",
            'Postman-Token': "7d2624bb-847e-4fdc-9b5c-34025ba42073"
        }

        response = requests.get(url=url, headers=headers, params=querystring)
        html = response.json()
        return html
# a=删除_购物车()
# b=a.删除('977','9')
# print(b)











