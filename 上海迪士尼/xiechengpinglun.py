# auchor JCC

import requests
import random
import time
from lxml import etree
from bs4 import BeautifulSoup
import json


class Spider():
    def __init__(self):
        self.num = 1
        self.oper = requests.session()
        self.page=1
        self.first_url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031169213527919769'
    def Main_spiders(self):
        index=0
        for i in range(1, 333):
            data={
                "arg":{"channelType":2,
                       "collapseType":0,
                       "commentTagId":0,
                       "pageIndex":i,
                       "pageSize":50,
                       "poiId":13412802,
                       "sourceType":1,
                       "sortType":3,
                       "starType":0},
                "head":{"cid":"09031169213527919769",
                        "ctok":"",
                        "cver":"1.0",
                        "lang":"01",
                        "sid":"8888",
                        "syscode":"09",
                        "auth":"",
                        "xsid":"",
                        "extension":[]}
            }
            data=json.dumps(data)
            main_headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'authority': 'm.ctrip.com',
                'path': '/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031169213527919769',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'referer': 'https://you.ctrip.com/',
                'cookieorigin': 'https://you.ctrip.com',
                'origin': 'https://you.ctrip.com',
                'upgrade-insecure-requests': "1",
            }
            req = self.oper.post(self.first_url,data=data, headers=main_headers)
            print(req.text)
            req_data=json.loads(req.text)
            print(req_data['code'])
            if req_data['code']==200:
                items=req_data['result']['items']
                print(len(items))
                for item in items:
                    content=item['content']
                    print(content)
                    with open('携程评论66.txt', 'a', encoding='utf-8')as f:
                        f.write(content + '\n')

            print('\n' + '第' + str(self.num) + '篇爬取完成！' + '\n')
            print("-" * 80)
            self.num += 1
            index+=1
            t = random.choice(range(2, 7))
            print("延迟" + str(t) + "秒钟!")
            time.sleep(t)


if __name__ == '__main__':
    spider = Spider()
    spider.Main_spiders()




