# -*- coding:utf-8 -*-
'''
Created on 2019��7��7��

#@author: JCC
'''

import re
import random
import requests
import json
import time


#--------------------------用户代理池-----------------------------

def ua():           
    uapools=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
        ]
    h=random.choice(uapools)
    head={'User-Agent':h}
    #print("本次使用用户代理为：%s"%head)
    return h
 
#--------------------------爬虫程序-------------------------------
    
def spider(url,pn,ps):
    '''
    with open('longji.txt','a') as f:
                    f.write("评论时间\t\t\t评分\t   买票情况\t\t游客ID\t\t\t评论内容\n\n")  
    '''    
                                
    for i in range(0,316):
        try:
            print('\n'+'-'*30+"正在爬取第%d页"%pn+'-'*30+'\n')
            h=ua()        
            data={"pageid":10650000804,"viewid":14892,"tagid":0,"pagenum":pn,"pagesize":ps,"contentType":"json","head":{"appid":"100013776","cid":"09031065210975000377","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","extension":[]},"ver":"7.10.3.0319180000"}
            header={'User-Agent':h,
                    'Content-Type':'application/json',
                    'cookieorigin':'https://piao.ctrip.com',
                    'Origin':'https://piao.ctrip.com',
                    'Referer':'https://piao.ctrip.com/ticket/dest/t14892.html',
                    'Cookie':'_abtest_userid=358a8ae6-89e3-45ad-b01e-a548542db12c; _bfa=1.1562559090530.3cqhqu.1.1562559090530.1562559090530.1.3; _bfs=1.3; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&Expires=1563163893187; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _RF1=113.14.161.176; _RSG=GMaiVNq7067GegXk6MA._A; _RDG=281ec0aa902b772fb53f82c9d6b7616437; _RGUID=71801f45-dfb2-4590-affe-2961ae86aa10; MKT_OrderClick=ASID=4897155952&CT=1562559093189&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={"pc_vid":"1562559090530.3cqhqu"}; _jzqco=%7C%7C%7C%7C1562559098908%7C1.1439564606.1562559093252.1562559098435.1562559102082.1562559098435.1562559102082.undefined.0.0.3.3; __zpspc=9.1.1562559093.1562559102.3%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%25E7%25BD%2591%7C%23; _bfi=p1%3D290564%26p2%3D100101991%26v1%3D2%26v2%3D1; MKT_Pagesource=PC; appFloatCnt=2'
                }
            
            #请求网页
            data=json.dumps(data)
            
            response=requests.post(url, data=data,headers=header,timeout=5)
            
            #判断网页是否访问正常
            if(response.status_code==200):
                print("网页返回值为200，第%s页访问正常！"%str(i+1))
            else:
                print("网页请求失败！")
            all_data=response.text
            
            #游客信息
            pat_uid='"uid":"(.*?)"'
            this_page_uid=re.compile(pat_uid).findall(all_data)
            #筛选评论日期
            pat_date='"date":"(.*?)",'
            this_page_date=re.compile(pat_date).findall(all_data)            
            #筛选评论内容
            pat_content='"content":"(.*?)",'
            this_page_content=re.compile(pat_content).findall(all_data)
            #买票情况
            pat_commentOrderInfo='"commentOrderInfo":"(.*?)"'
            this_page_commentOrderInfo=re.compile(pat_commentOrderInfo).findall(all_data)
            #评分情况
            pat_score='"score":"(.*?)"'
            this_page_score=re.compile(pat_score).findall(all_data)
                       
            
            for j in range(0,ps):
                if(this_page_commentOrderInfo[j]==''):
                    this_page_commentOrderInfo[j]='游客没用填写买票情况'
                print("%s\t %s\t %s分\t %s\t\t\t %s"%(this_page_date[j],this_page_commentOrderInfo[j],this_page_score[j],this_page_uid[j],this_page_content[j]))
                #写入本地文件
                with open('../test/更新1/携程纯评论(纯评论)2020.3.3.txt','a',encoding='utf-8') as f:                    
                    #f.write(this_page_date[j]+'\t\t')
                    #f.write(this_page_score[j]+'分\t')
                    #f.write(this_page_commentOrderInfo[j]+'      \t\t')                   
                    #f.write(this_page_uid[j]+'\t\t')
                    f.write(this_page_content[j]+'\n'*2)   
                    
                with open('../test/更新1/携程纯评论2020.3.3.txt','a',encoding='utf-8') as f:                    
                    f.write(this_page_date[j]+'\t\t')
                    f.write(this_page_score[j]+'分\t')
                    f.write(this_page_commentOrderInfo[j]+'      \t\t')                   
                    f.write(this_page_uid[j]+'\t\t')
                    f.write(this_page_content[j]+'\n')                  
                
            pn+=1
            
            t=random.choice(range(8,15))
            print("本次延时%ds"%t)
            time.sleep(t)
        except Exception as err:
            print("出现错误：%s"%err)
            pn+=1
            continue

    print("全部爬取完成！")



if __name__ == '__main__':
        
    ps=10     #请求评论数   
    pn=1      #从第几页开始请求
    url="https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031158211833888224"
    spider(url,pn,ps)










