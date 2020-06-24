#auchor JCC

import requests
import random
import time
from lxml import etree

class Spider():
    def __init__(self):
        self.num=1
        self.oper=requests.session()
        
        self.first_url='https://you.ctrip.com/travels/longjititian970/t2-p'
        self.main_headers={
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'authority': 'you.ctrip.com',
            'method': 'GET',
            'path': '/travels/longjititian970/s2-p1.html',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            }
        self.content_headers={
            'referer': 'https://you.ctrip.com/travels/longjititian970/s2-p1.html',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'authority': 'you.ctrip.com',
            }
    
    def Main_spiders(self):
        for i in range(1,86):
            page_url=self.first_url+str(i)+'.html'
            print(page_url)
            req=self.oper.get(page_url,headers=self.main_headers)
            html=etree.HTML(req.text)
            
            '''获取每篇游记的URL'''
            title_url=html.xpath('//div[@class="journalslist cf"]/a[@class="journal-item cf"]/@href')
            for i in range(0,len(title_url)):
                title_url[i]='https://you.ctrip.com'+title_url[i]
            title=html.xpath('//div[@class="iteminner"]/dl/dt/text()')
            print(title_url) 
            print(title)
            
            #爬取游记内容
            self.content_spider(title_url)

        
    def content_spider(self,url_list): 

        title_list=[]
        content_list=[]
        print(len(url_list))
        index=0
        
        for url in url_list:
            #try:                
                req=self.oper.get(url,headers=self.content_headers)
                html=etree.HTML(req.text)
                #date=html.xpath('//div[@class="ctd_content"]/h3//text()')   
                content=html.xpath('//div[@class="ctd_content"]/p//text()')  
                title=html.xpath('//div[@class="ctd_head"]/div[@class="ctd_head_left"]/h2//text()')
                title1=html.xpath('//div[@class="ctd_head_con cf"]/h1//text()')

                if len(title)==0:
                    
                    title_list.append(title1[0].strip())
                    print(title_list[index])
                    with open('../test/携程游记2019.9.16.txt','a',encoding='utf-8')as f:
                        f.write(title_list[index]+'\n'+'-'*80+'\n')
                    print('\n')
                else:
                    
                    title_list.append(title[0].strip())
                    print(title_list[index])
                    with open('../test/携程游记2019.9.16.txt','a',encoding='utf-8')as f:
                        f.write(title_list[index]+'\n'+'-'*80+'\n')
                    print('\n')
                
                for i in content:
                    print(i) 
                       
                for x in content:
                    
                    with open('../test/携程游记2019.9.16.txt','a',encoding='utf-8')as f:
                        f.write(x+'\n')
                        
                with open('../test/携程游记2019.9.16.txt','a',encoding='utf-8')as f:
                        f.write('\n'*6)    
                
                print('\t\t\n'+'第'+str(self.num)+'篇爬去完成！'+'\n')  
                print("-"*80)    
                index+=1   
                self.num+=1
                t=random.choice(range(2,7))
                print("延迟"+str(t)+"秒钟!")
                time.sleep(t)        
                #break
                
                
                '''    
            except Exception as err:
                print(err)
                index+=1 
                continue
                '''
            
    
        

if __name__ == '__main__':
    spider=Spider()
    spider.Main_spiders()
    
    
    
    
    