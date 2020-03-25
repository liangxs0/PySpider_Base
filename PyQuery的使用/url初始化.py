from pyquery import PyQuery as pq
#qyquery首先请求这个url然后再将返回的html内容完成初始化
doc = pq(url = "https://blog.csdn.net/qq_36389249")
print(doc('title'))