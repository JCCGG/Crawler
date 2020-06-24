#author:JCC
import requests
import re
import random
import time


class Spiders():
    def __init__(self):
        self.oper=requests.session()
        self.first_url='https://travel.qunar.com/place/api/html/comments/poi/715419?poiList=true&sortField=0&rank=0&pageSize=10&page='
        self.first_headers={
            'referer': 'https://travel.qunar.com/p-oi715419-longjititian-0-1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            }
        
        
        
        
    def Main_spiders(self):
        for j in range(1,100):
            name_num=0
            date_num=0
            '''
            with open('../test/11去哪儿旅游网2019.7.17.txt','a',encoding='utf-8')as f:
                f.write('\n'+'-'*30+'第'+str(j)+'页'+'-'*30+'\n'*2)  
            '''
            url=self.first_url+str(j)
            req=self.oper.get(url,headers=self.first_headers)
            all_data=req.text
            
            #匹配评论
            pat_comment='<div class=\\\\"e_comment_content\\\\"><p class=\\\\"first\\\\">(.*?)</p>'
            comment=re.compile(pat_comment).findall(all_data)
            print(comment)
            
            
            #匹配日期
            pat_date='<div class=\\\\"e_comment_add_info\\\\"><ul><li>(.*?)</li>'
            date=re.compile(pat_date).findall(all_data)
            for date_index in date:
                if len(date[date_num])>20:
                    date[date_num]='获取不到评论日期！'
                    
                date_num+=1
            print(date)
            
            #匹配用户名
            pat_username='<div class=\\\\"e_comment_usr_name\\\\">(.*?)&nbsp;<a rel=\\\\"nofollow\\\\" href=\\\\"javascript:;\\\\">(.*?)</a></div>'
            username=re.compile(pat_username).findall(all_data) 
            for name in username:
                username[name_num]=name[0]+'-'+name[1]
                #print(username[name_num])
                if len(username[name_num])>20:
                    username[name_num]='获取不了用户名'    
                name_num+=1
            print(username)
            
            
            for i in range(0,len(username)):
                with open('../test/11去哪儿旅游网2019.7.17.txt','a',encoding='utf-8')as f:
                    f.write(date[i]+"\t"+username[i]+'\t\t'+comment[i]+'\n')
                   
            
                       
            print('\n'+'-'*30+'第'+str(j)+'页爬取完成！'+'-'*30) 
            t=random.choice(range(1,3))
            print("本次延时%ds"%t)
            time.sleep(t) 


if __name__ == '__main__':
    spiders=Spiders()
    spiders.Main_spiders()
    
    
    
    
    

