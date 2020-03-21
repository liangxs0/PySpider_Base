from selenium import webdriver
import random
from scrapy import Selector
import time


url = 'https://telesky.tmall.com/shop/view_shop.htm?shopId=113500236&search=y&keyword=%B4%AB%B8%D0%C6%F7%C4%A3%BF%E9'
url2 = 'https://telesky.tmall.com/search.htm?spm=a1z10.3-b-s.w4011-16538328900.50.40733d6cWmD1Vm&search=y&keyword=%B4%AB%B8%D0%C6%F7%C4%A3%BF%E9&pageNo=1&tsearch=y#anchor'
broswer = webdriver.Chrome()
broswer.get(url=url)
broswer.maximize_window()
time.sleep(2)
broswer.find_element_by_xpath('//*[@id="sn-bd"]/div/ul/li[1]/div/a').click()
time.sleep(10)
broswer.get(url=url2)
time.sleep(2)
broswer.refresh()
 file = open("a.txt","a+",encoding="UTF-8")
# broswer.find_element_by_xpath('//*[@id="shop16538328897"]/div/div[1]/div[2]/div[1]/a').click()
time.sleep(30)
for i in range(0,3):
    file = open(str(i)+".txt","a+",encoding="UTF-8")
    text = broswer.page_source
    file.write(text)
    file.close()
    time.sleep(5)
    try:
        broswer.find_element_by_xpath('//*[@id="J_ShopSearchResult"]/div/div[2]/p/a[2]').click()
    except:
        broswer.find_element_by_xpath('//*[@id="J_ShopSearchResult"]/div/div[2]/p/a').click()
broswer.close()

