import requests
import json
import time
import random



class Spiders():
    def __init__(self):
        self.url='http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=14566&index='
        self.headers={
            'Referer': 'https://piao.qunar.com/ticket/detail_1141263143.html?st=a3clM0QlRTklQkUlOTklRTglODQlOEElRTYlQTIlQUYlRTclOTQlQjAlMjZpZCUzRDE0NTY2JTI2dHlwZSUzRDAlMjZpZHglM0QxJTI2cXQlM0RuYW1lJTI2YXBrJTNEMiUyNnNjJTNEV1dXJTI2YWJ0cmFjZSUzRGJ3ZCU0MCVFNiU5QyVBQyVFNSU5QyVCMCUyNnVyJTNEJUU1JThDJTk3JUU0JUJBJUFDJTI2bHIlM0QlRTglQjQlQjUlRTYlQjglQUYlMjZmdCUzRCU3QiU3RA%3D%3D',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'authority': 'piao.qunar.com',
            'method': 'GET',
            'path': '/ticket/detailLight/sightCommentList.json?sightId=14566&index=1&page=1&pageSize=10&tagType=0',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-fetch-mode':'cors',
            'ec-fetch-site': 'same-origin'
            }
        
        self.img_headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'img1.qunarzz.com',
            'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:01 GMT',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            }
        
        self.img_headers1={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'mp-piao-admincp.qunarzz.com',
            'If-Modified-Since': 'Tue, 12 Feb 2019 09:05:01 GMT',
            'If-None-Match': "e70653e324d7de7ac7fed4b75bf43482",
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            }
        
        
    def spiders(self):
        try:
        
            for i in range(1,1102):
            
                url=self.url+str(i)+'&page='+str(i)+'&pageSize=10&tagType=0'
                print(url)
                
                req=requests.get(url,headers=self.headers)
                dic_data=req.text
                html_data=json.loads(dic_data)
                
                for index in range(0,len(html_data['data']['commentList'])):
                    
                    comment_data=html_data['data']['commentList'][index]['content']
                    date_data=html_data['data']['commentList'][index]['date']
                    author_data=html_data['data']['commentList'][index]['author']
                    score_data=html_data['data']['commentList'][index]['score']
                    comment_id=html_data['data']['commentList'][index]['commentId']
                    
                    print(author_data+"\t"+str(score_data)+"\t"+date_data+"\t"+comment_data)
                    
                    with open('../test/更新/去哪儿(纯评论)2020.2.11.txt','a',encoding='utf-8') as f:
                        f.write(comment_data+'\n')
                       
                    
                    with open('../test/更新/去哪儿评论2020.2.11.txt','a',encoding='utf-8') as f:
                        f.write(str(date_data)+'\t'*2)
                        f.write(str(author_data)+'\t'*2)
                        f.write(str(score_data)+'\t'*2)
                        f.write(str(comment_data)+'\n')
                        
                with open('../test/更新/去哪儿(纯评论)2020.2.11.txt','a',encoding='utf-8') as f:
                    f.write('\n')
                with open('../test/更新/去哪儿评论2020.2.11.txt','a',encoding='utf-8') as f:   
                    f.write('\n')
                    
                    '''
                                #获取每个评论的图片 
                    for imgs in range(0,len(html_data['data']['commentList'][index]['imgs'])):
                        img_url=html_data['data']['commentList'][index]['imgs'][imgs]['big']
                        with open('../test/去哪儿图片连接.txt','a') as f:
                            f.write(img_url+'\n')
                        
                        img_req=requests.get(img_url,headers=self.img_headers)
                        
                        img_path="../images/"+comment_id+str(imgs+1)+".jpg"
                        with open(img_path,'wb') as f:
                            f.write(img_req.content)
                        
                        #break
                        print("第"+str(index+1)+'个用户的第'+str(imgs+1)+'张图片下载完成！\n')
                    
                    #break
                    '''
                        
                print("第"+str(i)+'页获取完毕！\n')
                print('正在获取第下一页')
                
                t=random.choice(range(10,15))
                time.sleep(t)
                print("延时:"+str(t)+'秒')    
                
        except Exception as err:
            print(err)
        
            
            






if __name__ == '__main__':
    spiders=Spiders()
    spiders.spiders()


