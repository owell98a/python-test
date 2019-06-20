from urllib import request
import re
url='https://movie.douban.com/top250'

req=request.urlopen(url)
html=req.read()
content=html.decode('utf-8')
print (content)

parse=re.findall(r'<img width="100" alt="(.*?)".*?src="(.*?)" class="">',content)
test=re.findall(r'<a href="?start=225&amp;filter=">10</a>',content)
print (parse)
print(test)

for i in range (10):
    html_url=url+f'?start={25*i}&amp;filter='
    print (html_url)


class GetImg_url:
    