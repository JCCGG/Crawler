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
    def Main_spiders(self):
        index=0
        for i in range(1, 103):
            first_url = 'https://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=jQuery18103208114032348699_1619703509758&_ts=1619709609673&_sn=397798c3fb&_=1619709609675'
            params={
                "poi_id":"6102028",
                "page":i,
                "just_comment":1}
            main_headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'authority': 'pagelet.mafengwo.cn',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'referer': 'https://www.mafengwo.cn/poi/6102028.html',
                'upgrade-insecure-requests': "1",
                'path': '/poi/pagelet/poiCommentListApi?callback=jQuery18103208114032348699_1619703509758&params=%7B%22poi_id%22%3A%226102028%22%2C%22page%22%3A1%2C%22just_comment%22%3A1%7D&_ts=1619709351286&_sn=ca67f86519&_=1619709351287'
            }
            req = self.oper.get(first_url,headers=main_headers,params=params)
            print(req.text)

            # req_data=json.loads(req.text)
            # print(req_data['errcode'])
            # if req_data['errcode']==0:
            #     items=req_data['data']
            #     # print(items)
            #     soup=BeautifulSoup(str(items),'lxml')
            #     content=soup.select(".e_comment_content")
            #     print(len(content))
            #     for c in content:
            #         comment=c.get_text()
            #         print(c.get_text())
            #         with open('马蜂窝评论.txt', 'a', encoding='utf-8')as f:
            #             f.write(comment + '\n')

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




