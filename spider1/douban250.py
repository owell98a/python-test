from urllib import request
import re
import os
'''
url='https://movie.douban.com/top250'

req=request.urlopen(url)
html=req.read()
content=html.decode('utf-8')
print (content)

parse=re.findall(r'<img width="100" alt="(.*?)".*?src="(.*?)" class="">',content)
test=re.findall(r'<a href="?start=225&amp;filter=">10</a>',content)
print (parse)

for i in range (10):
    html_url=url+f'?start={25*i}&amp;filter='
    print (html_url)
'''
class Get_img:

    def __init__(self,path='./'):    #保存地址
        self.path=path

    def start(self,start_url):
        page_url=self.get_url(start_url)
        self.get_img_url(page_url)


    def get_url(self,url):          #获取每页url
        parse_list=[]
        for i in range(10):
            html_url = url + f'?start={25 * i}&amp;filter='
            parse_list.append(html_url)
        return parse_list

    def readimg(self,url):
        if url:
            req=request.urlopen(url)
            if req.code==200:
                return req.read()

    def save_img(self,parse):

        for i in parse:
            img = self.readimg(i[1])
            fname=i[0]+'.'+i[1].rsplit('.',1)[-1]
            fpath=os.path.join(self.path,fname)
            with open(fpath,'wb') as f:
                f.write(img)


    def get_img_url(self,parse_list):    #获取img的url与海报名
        for i in parse_list:
            url=i
            req = request.urlopen(url)
            html = req.read()
            content = html.decode('utf-8')
            #print(content)
            parse = re.findall(r'<img width="100" alt="(.*?)".*?src="(.*?)" class="">', content)
            self.save_img(parse)



if __name__=='__main__':
    url='https://movie.douban.com/top250'
    spider=Get_img()
    spider.start(url)
    