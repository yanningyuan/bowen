#/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
class 学校_查询():
    def 学校_快查(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        querystring = {"filterInput": "{}".format(a)}

        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
            'cache-control': "no-cache",
            'Postman-Token': "620e3ca0-2919-43c1-943e-e190e5dc8404"
        }

        response = requests.get(url=url, headers=headers, params=querystring)
        html = response.json()
        return html

    def 学校_考试快查(self,a):
        pass
    def 学校_列表(self):
        pass







































