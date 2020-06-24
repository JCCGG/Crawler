#-*- coding:utf-8 -*-

import requests
import random
import re
import time


class mySpider:
    def __init__(self,url):
        self.url=url
        self.post_data={}
    
    def getHeader(self):
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
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest' 
            }
        return headers
    
    def post_data_init(self,index): 
      self.post_data={
        'poiID': '10558732',
        'districtId': '970',
        'districtEName': 'Thelongjiyaoandzhuangethnicterrace',
        'pagenow': str(index),
        'order':'1',
        'star': '0.0',
        'tourist': '0.0',
        'resourceId': '14892',
        'resourcetype': '2',
        }    
    
    def spider(self):
        r=requests.session()
        page_index=1
        try:
            while(page_index<311):#1-310页
                headers=self.getHeader()#headers
                self.post_data_init(page_index)#post_data---页数
                
                res=r.post(self.url,headers=headers,data=self.post_data)
                #print(res.text)
                
                pat_content='<span class="heightbox">(.*?)</span>'
                this_page_content=re.compile(pat_content).findall(res.text)
                  
                print("本页评论："+str(len(this_page_content))+'\n')
                #写入txt
                for i in this_page_content:
                    with open('cs.txt','a',encoding='utf-8') as f:
                        f.write(i+"\n")
                        print(i)
                    
                        
                rand=random.choice(range(5,8))
                print("\n第"+str(page_index)+"页OK---延迟:"+str(rand)+'秒')
                page_index+=1
                time.sleep(rand)
                
        except Exception as err:
            print(err)


if __name__ == '__main__':
    url='https://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'
    m=mySpider(url)
    m.spider()
    
    
    
    
    