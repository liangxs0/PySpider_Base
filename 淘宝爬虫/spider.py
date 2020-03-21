from selenium import webdriver
import time
from scrapy import Selector
import urllib
import random
url = "https://zhizesm.tmall.com/search.htm?spm=a1z10.1-b.w5002-2631402129.1.2779328cotaeRN&search=y"
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get(url=url)
browser.maximize_window()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="sn-bd"]/div/ul/li[1]/div/a').click()
time.sleep(10)
browser.get(url=url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="shop2631402129"]/div/div/div/div/a/span').click()
time.sleep(3)
print(type(browser.page_source))
text = browser.page_source
page = Selector(text=text)

for i in range(0,5):
	text = browser.page_source
	page = Selector(text=text)
	file = open(str(i)+".txt","a+",encoding="utf-8")
	file.write(text)
	try:
		browser.find_element_by_xpath('//*[@id="J_ShopSearchResult"]/div/div[2]/p/a[2]').click()
	except:
		browser.find_element_by_xpath('//*[@id="J_ShopSearchResult"]/div/div[2]/p/a').click()
		#//*[@id="J_ShopSearchResult"]/div/div[2]/p/a
		#//*[@id="J_ShopSearchResult"]/div/div[2]/p/a[2]
	time.sleep(random.randint(4,9))


# description = page.xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div[1]/dl[1]/dd[2]/a/text()').extract_first()
#                        //*[@id="J_ShopSearchResult"]/div/div[3]/div[1]/dl[2]/dd[2]/a
#                        ////*[@id="J_ShopSearchResult"]/div/div[3]/div[2]/dl[1]/dd[2]/a
#                       //*[@id="J_ShopSearchResult"]/div/div[3]/div[7]/dl[1]/dd[2]/a
#                       //*[@id="J_ShopSearchResult"]/div/div[3]/div[9]/dl[2]/dd[2]/a

# #                       //*[@id="J_ShopSearchResult"]/div/div[3]/div[5]/dl[1]/dd[1]/a
# href = page.xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div[1]/dl[1]/dd[2]/a/@href').extract_first()
# print(description)
# print(href)
# href = urllib.parse.urljoin("https:",href)
# print(description)
# print(href)

browser.close()


