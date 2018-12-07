#/usr/bin/env python
# -*- coding:utf-8 -*-
url='https://fe-api.zhaopin.com/c/i/sou/page-title?start=60&pageSize=60&cityId=653&areaId=&businessarea=%7B%7D&industry=&salary=&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&bj=&sj=&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22653%22,%22kw%22:%22%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88%22,%22kt%22:%223%22%7D&companyNo=&companyName=&_v=0.70079790&x-zp-page-request-id=35055afa843f476abefa64498ade03ad-1541770363016-118816'
head='user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
res=requests.get(url=url,headers=head)
html=res.content.decode('utf-8')
patt=re.complice('')







































