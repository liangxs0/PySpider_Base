import requests
from bs4 import BeautifulSoup
import re
import time
start_url = "https://www.vmgirls.com/"
url = 'https://www.vmgirls.com/12985.html'
page_url = []
picUrls = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

res = requests.get(url=start_url,headers=headers)

page = BeautifulSoup(res.text,"lxml")

urls = page.find("section",class_="list-bordered-padding")
print(type(urls))
for url in urls:
    url = BeautifulSoup(str(url),"lxml")
    for info in  url.find_all(name="a",attrs={"href":re.compile(r'http')}):
        if info["href"] not in page_url:
            page_url.append(info["href"])
            print("-"*40)
            print(info["href"])
            for i in range(1,50):
                try:
                    NewUrl = info["href"][0:-5]+'/page-'+str(i)+'.html'
                    print(NewUrl)
                    res_ = requests.get(NewUrl,headers=headers)
                    print(res_.status_code)
                    if res_.status_code > 400:
                        break
                    PicUrl = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',res_.text)
                    for p in PicUrl:
                        picUrls.append(p)
                    time.sleep(2)
                except Exception as e:
                    break

with open('E:\\桌面\\,\\爬虫授课资料文件\\爬起妹子图\\pic\\url.txt',"a+",encoding="utf-8") as f:
    for u in picUrls:
        f.write(u+"\n")