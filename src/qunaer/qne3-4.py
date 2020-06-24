#-*- coding:utf-8 -*-

import requests
import random
import re
import time
import this
import json
import xlwt


class mySpider:
    def __init__(self,url):
        self.url=url
    
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

    def getHeader(self):
        h=self.ua() #后去用户代理
        headers={
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'piao.qunar.com',
                'Referer': 'http://piao.qunar.com/ticket/detail_1141263143.html?in_track=pc_dujia_search_poi',
                'User-Agent':h,
                'X-Requested-With': 'XMLHttpRequest'
            }
        
        return headers
    def get_page_url(self,pg):
        self.url=url+str(pg)+'&page='+str(pg)+'&pageSize=10&tagType=0'
    
    #写入excel
    def toExcel(self,myBook,mySheet,content,row):
        mySheet.write(row,0,content)
        myBook.save('../test/更新1/去哪儿.xls')
    
    def spider(self):
        r=requests.session()
        #self.getCookie(r)
        
        page_index=1
        
        try:
            myBook=xlwt.Workbook(encoding='utf-8')
            mysheet=myBook.add_sheet('去哪儿评论') 
            
            while(page_index<1215):
                self.get_page_url(page_index)
                headers=self.getHeader()
                res=r.get(url=self.url,headers=headers)
                result=json.loads(res.text)
                
                print(res.cookies)
                print(result) 
                
                excel_row=0
                for i in result['data']['commentList']:
                    print(i['content'])
                    content=i['content']
                    
                    #写入excel
                    self.toExcel(myBook,mysheet,content,excel_row)
                    excel_row+=1
                    
                    #写入txt
                    with open('../test/更新1/去哪儿(纯评论)2020.3.4.txt','a',encoding='utf-8') as f:
                        f.write(content+"\n")      
                            
    
                print('本页长度：'+str(len(result['data']['commentList'])))
                          
                ra=random.choice(range(10,15))
                print("\n第"+str(page_index)+"页OK---延迟:"+str(ra)+'秒')
                page_index+=1
                time.sleep(ra)
        except Exception as err:
            print(err)
            
        finally:
#             with open('../test/更新1/去哪儿(纯评论)2020.3.4.txt','a',encoding='utf-8') as f:
#                 f.write("\n爬到第"+str(page_index)+"页")
            pass


if __name__ == '__main__':
    url='http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=14566&index='
    
    m=mySpider(url)
    m.spider()
    
    
    
    
    