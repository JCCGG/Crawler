#-*- coding:utf-8 -*-

import requests
import random
import re
import time
import this


class mySpider:
    def __init__(self,url):
        self.url=url
        self.post_data={}
    
    #--------------------------用户代理池-----------------------------
    
    def ua(self):           
        uapools=[
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
            ]
        h=random.choice(uapools)
        #print("本次使用用户代理为：%s"%head)
        return h    
    def getCookie(self,r):
        url='https://you.ctrip.com/sight/longjititian970/14892.html'
        headers={
            'authority': 'you.ctrip.com',
            ':method': 'GET',
            ':path': '/sight/longjititian970/14892.html',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
        re=r.get(url,headers)
        print(re.cookies)
    def getHeader(self):
        h=self.ua() #后去用户代理
        headers={
                'authority': 'you.ctrip.com',
                'method': 'POST',
                'path': '/destinationsite/TTDSecond/SharedView/AsynCommentView',
                'scheme': 'https',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'content-length': '149',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://you.ctrip.com',
                'referer': 'https://you.ctrip.com/sight/longjititian970/14892.html',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': h,
                'x-requested-with': 'XMLHttpRequest' 
            }
        
        return headers
    def post_data_init(self,index): 
      page=index  
      self.post_data={
        'poiID': '10558732',
        'districtId': '970',
        'districtEName': 'Thelongjiyaoandzhuangethnicterrace',
        'pagenow': str(page),
        'order':'1',
        'star': '0.0',
        'tourist': '0.0',
        'resourceId': '14892',
        'resourcetype': '2',
        }    
    
    def spider(self):
        r=requests.session()
        #self.getCookie(r)
        
        page_index=1
        while(page_index<311):
            headers=self.getHeader()#headers
            #print(headers)
            self.post_data_init(page_index)#post_data---页数
            #print(self.post_data)
            
            res=r.post(self.url,headers=headers,data=self.post_data)
            
            pat_content='<span class="heightbox">(.*?)</span>'
            this_page_content=re.compile(pat_content).findall(res.text)
            #print(this_page_content)
            print(len(this_page_content))
            #print(res.url)
            for i in this_page_content:
                with open('../test/更新1/携程纯评论(纯评论)2020.3.3.txt','a',encoding='utf-8') as f:
                    f.write(i+"\n")
                    print(i)
                    
            rand=random.choice(range(5,8))
            print("/n第"+str(page_index)+"页OK---延迟:"+str(rand)+'秒')
            page_index+=1
            time.sleep(rand)


if __name__ == '__main__':
    url='https://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'
    
    m=mySpider(url)
    m.spider()
    
    
    
    
    