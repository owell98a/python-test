from urllib import request
import re
url='https://movie.douban.com/top250'
hl=request.urlopen(url)   #返回HTTPResponse对象
print (hl.code)          #可获得状态码 ，头信息等

content=hl.read()          #再次请求,获取网页数据为bytes对象
print (type(content))      #为bytes格式
html=content.decode('utf-8')  #转化为string
print(html) #进行utf-8解码操作

listurl=re.findall(r'<img width=".*?" alt="(.*?)".*?src="(.*?)"',html)  #html需为string格式，(.*?)为非贪婪模式
                                                                          # .*为贪婪模式

print(listurl)

listpage=re.findall(r'<link rel="next" href="(.*?)"/>',html)
print(listpage)

