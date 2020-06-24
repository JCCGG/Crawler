import requests
import lxml.etree
import time
import random
import xlwt


class Spiders():
    
    
    
    def __init__(self):
        self.static_num=0
        self.url='https://www.tripadvisor.cn/Attraction_Review-g1159371-d503008-Reviews-or'
        self.headers={
            'Host': 'www.tripadvisor.cn',
            'Origin': 'https://www.tripadvisor.cn',
            'Referer': 'https://www.tripadvisor.cn/Attraction_Review-g1159371-d503008-Reviews-or30-Dragon_s_Backbone_Rice_Terraces-Longsheng_County_Guangxi.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Puid': 'XZ-Pt8CoATIABU-Y3K4AAABH',
            'X-Requested-With': 'XMLHttpRequest'
            }
        self.data={
            'reqNum':'1',
            'isLastPoll': 'false',
            'paramSeqId': '0',
            'waitTime': '14',
            'changeSet': 'REVIEW_LIST',
            'puid': 'XZ-Pt8CoATIABU-Y3K4AAABH',
            }
        
        self.oper=requests.session()
    def toExcel(self,myBook,mySheet,content):
        for i in range(0,len(content)):
            mySheet.write(self.static_num,0,content[i])
            myBook.save('../test/更新1/猫途鹰(纯评论)2020.2.9.xls')
            self.static_num+=1
    def Spiders_main(self):
        try:
            myBook=xlwt.Workbook(encoding='utf-8')
            mySheet=myBook.add_sheet("猫途鹰评论")
            
            
            for i in range(0,30):
                if(i==0):
                    url='https://www.tripadvisor.cn/Attraction_Review-g1159371-d503008-Reviews-Dragon_s_Backbone_Rice_Terraces-Longsheng_County_Guangxi.html'
                else:
                    url=self.url+str(i*10)+'-Dragon_s_Backbone_Rice_Terraces-Longsheng_County_Guangxi.html'
                print(url)
                req=self.oper.post(url,headers=self.headers,data=self.data)
                
                #pat='<div class="entry"><p class="partial_entry" >(.*?)</p></div>'
                #html_data=re.compile(pat).findall(req.text)
                html_data=lxml.etree.HTML(req.text)
                content_data=html_data.xpath('//div[@class="entry"]/p[@class="partial_entry"]//text()')
                username_data=html_data.xpath('//div[@class="info_text pointer_cursor"]/div//text()')
                date_data=html_data.xpath('//div[@class="ui_column is-9"]/span[@class="ratingDate"]/text()')
                

                #打印出来并写入本地文档 
                
#                 with open("../test/更新/猫途鹰2020.2.9.txt",'a',encoding='utf-8') as f:
#                     for i in range(0,10):
#                         #print(date_data[i]+"\t"+content_data[i])   
#                         f.write(date_data[i]+"\t"*2+content_data[i]+'\n'*2)
#                     f.write("-"*100+"\n"*2)
                
                self.toExcel(myBook, mySheet,content_data)
                
                with open("../test/更新1/猫途鹰(纯评论)2020.2.9.txt",'a',encoding='utf-8') as f:
                    for content in content_data:  
                        content=content.replace("\n", "")      
                        f.write(content+'\n')
                        print(content)
                               
                print("本页 长度："+str(len(content_data)) )   
                        
                rand=random.choice(range(5,8)) 
                print('*'*30+'第'+str(i+1)+'页爬取完成！延迟：'+str(rand)+'秒'+'*'*100)   
                time.sleep(rand)
        except Exception as err:
            print(err) 
                

if __name__ == '__main__':
    spider=Spiders() 
    spider.Spiders_main()
    
    
    