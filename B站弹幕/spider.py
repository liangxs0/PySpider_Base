import requests
import jieba
import numpy as np
from lxml import etree
from wordcloud import WordCloud as wc
from PIL import Image
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=152796906'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

res = requests.get(url=url,headers=headers)

print(res.status_code)
with open("./B站弹幕/bilibli.xml","wb") as f:
    f.write(res.content)
result = []
html = etree.parse("./B站弹幕/bilibli.xml",etree.HTMLParser())
text = html.xpath("//d//text()")
with open ('./B站弹幕/a.txt',"a+",encoding="utf-8") as f:
    for t in text:
        f.write(t+'\n')