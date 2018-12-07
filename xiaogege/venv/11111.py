#/usr/bin/env python
# -*- coding:utf-8 -*-
import json
data={'name':'wefwerf'}
将json数据更改为字符串
data1=json.dumps(data)
print(data1)
将json数据更改为字典
data2=json.loads(data1)
print(data2)












