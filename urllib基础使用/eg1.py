# -*-coding:utf-8-*-
from urllib import request
import chardet

url = "https://fanyi.baidu.com"

response = request.urlopen(url=url)
html = response.read()
charset = chardet.detect(html)#获取编码格式
print(charset)
html = html.decode(charset["encoding"])
print(html)

url = "http://fanyi.baidu.com/"
response = request.urlopen(url=url)
print("geturl:%s"%(response.geturl()))
print("*"*30)
print("info:%s"%(response.info()))
print("*"*30)
print("getcode:%s"%(response.getcode()))
url1 = "http://fanyi.baidu.com/v2transapi?from=en&to=zh"

