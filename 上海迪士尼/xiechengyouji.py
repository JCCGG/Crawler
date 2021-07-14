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
        self.page=1
        self.first_url = 'https://you.ctrip.com/travels/shanghaidisneyresort1446916/t2'
    def Main_spiders(self):
        for i in range(1, 9):
            print("")
            mUrl=""
            if i==1:
                mUrl=self.first_url+'.html'
            else:
                mUrl=self.first_url+'-p'+str(i)+'.html'
            main_headers = {
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'authority': 'you.ctrip.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'referer': mUrl,
                'upgrade-insecure-requests': "1",
            }
            print(mUrl)
            req = self.oper.get(mUrl, headers=main_headers)
            html = etree.HTML(req.text)

            title_url = html.xpath('//div[@class="journalslist cf"]/a[@class="journal-item cf"]/@href')
            for i in range(0, len(title_url)):
                title_url[i] = 'https://you.ctrip.com' + title_url[i]
            title = html.xpath('//div[@class="iteminner"]/dl/dt/text()')
            print(title_url)
            print(title)
            # 爬取游记内容
            self.content_spider(title_url,title)

    def content_spider(self, url_list,title):
        print(len(url_list))
        index=0
        content_headers = {
            'referer': 'https://you.ctrip.com/travels/shanghaidisneyresort1446916/t3.html',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'authority': 'you.ctrip.com',
        }

        for url in url_list:
            print(url)
            req = self.oper.get(url, headers=content_headers)
            soup=BeautifulSoup(req.text,'lxml')
            c=soup.find("div","ctd_content")
            if c!=None:
                content=c.get_text(strip=True)
                print(content)
                with open('携程游记.txt','a',encoding='utf-8') as f:
                    f.write(title[index]+"\n")
                with open('携程游记.txt', 'a', encoding='utf-8')as f:
                        f.write(content + '\n')
            # with open('携程游记.txt','a',encoding='utf-8') as f:
            #     f.write('\n' * 6+'\n')

            # html = etree.HTML(req.text)
            # date=html.xpath('//div[@class="ctd_content"]/h3//text()')
            # content = html.xpath('//div[@class="ctd_content"]/p//text()')
            # with open('携程游记.txt','a',encoding='utf-8') as f:
            #     f.write("游记"+str(self.num)+"\n"+"*"*60+"\n")
            # for c in content:
            #     print(c)
            #     with open('携程游记.txt', 'a', encoding='utf-8')as f:
            #         f.write(c + '\n')
            # with open('携程游记.txt','a',encoding='utf-8') as f:
            #     f.write('\n' * 6+'\n')

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




