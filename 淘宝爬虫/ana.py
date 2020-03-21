from scrapy import Selector
import urllib
for i in range(0,5):
	file = open(str(i)+".txt","r",encoding="utf-8")
	data = file.read()
	file.close()
	page = Selector(text=data)
	print("-*-"*30)
	for j in range(1,13):
		for k in range(1,6):
			description = page.xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div['+str(j)+']/dl['+str(k)+']/dd[2]/a/text()').extract_first()
			href = page.xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div['+str(j)+']/dl['+str(k)+']/dd[2]/a/@href').extract_first()
			href = urllib.parse.urljoin("https:",href)
			if description == None:
				continue
			f = open("./data.txt",'a+',encoding="utf-8")
			f.write(description+'\t\t\t'+href+"\n")
			print(description)
			print(href)

