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
        self.first_url = 'http://www.mafengwo.cn/search/q.php?q=%E4%B8%8A%E6%B5%B7%E8%BF%AA%E5%A3%AB%E5%B0%BC&t=notes&seid=A67EC6A3-0E6E-48B9-81EE-C6372C40AA19'

    def Main_spiders(self):
        main_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'www.mafengwo.cn',
            'Upgrade-Insecure-Requests': "1",
            'Referer': 'http://www.mafengwo.cn/search/q.php?q=%E4%B8%8A%E6%B5%B7%E8%BF%AA%E5%A3%AB%E5%B0%BC&t=notes&seid=73B3B050-F4C6-4F15-BAC4-603CBD148051&mxid=&mid=&mname=&kt=1'
        }
        req = requests.get(self.first_url, headers=main_headers)
        # print(req.text)
        soup=BeautifulSoup(req.text,'lxml')
        data=soup.select('.ct-text>h3>a')
        title=[]
        title_url=[]
        for d in data:
            title_url.append(d.get('href'))
            title.append(d.get_text())

        print(title)
        print(title_url)
        self.content_spider(title_url,title)
    def content_spider(self, url_list,title):
        print(len(url_list))
        index=0
        for url in url_list:
            content_headers = {
                'Referer': url,
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Host': 'www.mafengwo.cn',
                'Cookie': 'mfw_uuid=6086aab6-0f22-08c6-911d-874e356f3f27; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-04-26+19%3A57%3A42%22%3B%7D; __jsluid_h=f42604e54dbe7cfe2d4d91175cba7991; __omc_chl=; __omc_r=; __mfwc=direct; uva=s%3A78%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1619438263%3Bs%3A10%3A%22last_refer%22%3Bs%3A6%3A%22direct%22%3Bs%3A5%3A%22rhost%22%3Bs%3A0%3A%22%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1619438263%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=6086aab6-0f22-08c6-911d-874e356f3f27; UM_distinctid=1790e0ae7dd64-0f28538dff4c45-3e604809-144000-1790e0ae7de8f9; PHPSESSID=frvharv0e1ng2r1o3ui2768vq2; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1619438266,1619449227,1619488849; bottom_ad_status=0; __mfwa=1619438265360.22437.4.1619488847882.1619497748771; __mfwlv=1619497748; __mfwvn=4; CNZZDATA30065558=cnzz_eid%3D843139026-1619434381-%26ntime%3D1619498776; __jsl_clearance=1619501463.508|0|z6gd3FEiVYFppsUn8lCKd7Glg3U%3D; __mfwb=5baa24d75edb.16.direct; __mfwlt=1619501467; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1619501469'
            }
            print(url)
            req = requests.get(url, headers=content_headers)
            soup=BeautifulSoup(req.text,'lxml')
            c=soup.find("div","_j_content_box")
            # print(req.text)
            if c!=None:
                content=c.get_text(strip=True)
                print(content)

                with open('马蜂窝游记.txt','a',encoding='utf-8') as f:
                    f.write(title[index]+"\n")

                with open('马蜂窝游记.txt', 'a', encoding='utf-8')as f:
                        f.write(content + '\n')
                # with open('马蜂窝游记.txt','a',encoding='utf-8') as f:
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




