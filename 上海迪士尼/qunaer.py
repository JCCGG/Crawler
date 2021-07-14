# auchor JCC

import requests
import random
import time
from lxml import etree
from bs4 import BeautifulSoup


class Spider():
    def __init__(self):
        self.num = 1
        self.oper = requests.session()
        self.first_url = 'https://travel.qunar.com/travelbook/list/22-shanghaidishinidujiaqu-1062172/hot_ctime/'

    def Main_spiders(self):
        for i in range(1,7):
            mUrl=self.first_url+str(i)+'.htm'
            main_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'authority': 'travel.qunar.com',
                'Upgrade-Insecure-Requests': "1",
                'Referer': mUrl
            }
            req = requests.get(mUrl, headers=main_headers)
            # print(req.text)
            soup=BeautifulSoup(req.text,'lxml')
            data=soup.select('.list_item>h2')

            title=[]
            title_url=[]
            for d in data:
                title_url.append(d.a.get('href'))
                title.append(d.get_text())

            print(title)
            print(title_url)
            self.content_spider(title_url,title)
    def content_spider(self, url_list,title):
        print(len(url_list))
        index=0
        for url in url_list:
            cUrl='https://travel.qunar.com'+url
            content_headers = {
                'Referer': 'https://travel.qunar.com/travelbook/list/22-shanghaidishinidujiaqu-1062172/hot_ctime/1.htm',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                 'authority': 'travel.qunar.com',
                 }
            print(cUrl)
            req = requests.get(cUrl, headers=content_headers)
            soup=BeautifulSoup(req.text,'lxml')
            c=soup.find("div","e_main")
            if c!=None:
                content=c.get_text(strip=True)
                print(content)
                with open('去哪儿游记.txt', 'a', encoding='utf-8')as f:
                    f.write(title[index]+"\n")
                with open('去哪儿游记.txt', 'a', encoding='utf-8')as f:
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




