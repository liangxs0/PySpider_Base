#!/usr/bin/python 
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def download_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
	res = requests.get(url=url,headers=headers)
	return res.text

def get_content(html,page):
	output = """第{}页 作者：{} 性别：{} 年龄：{} 点赞：{} 评论：{}\n{}\n------------\n""" # 最终输出格式
	soup = BeautifulSoup(html,'html.parser')
	con = soup.find(id="content-left")
	con_list = con.find_all("div",class_="article")
	for i in con_list:
		author = i.find("h2").string
		content = i.find("div",class_="content").find("span").get_text()
		stats = i.find("div", class_="stats")
		comment = stats.find('span', class_='stats-comments').find('i', class_='number').string
		vote = stats.find("span",class_="stats-vote").find("i",class_="number").string
		author_info = i.find("div",class_="articleGender")
		if author_info is not None:
			class_list = author_info["class"]
			if "womenIcon" in class_list:
				gender = "女"
			elif "manIcon" in class_list:
				gender = "男"
			else:
				gender = ""
			age = author_info.string
		else:
			gender = ""
			age = ""
		save_text(output.format(page, author, gender, age, vote, comment, content))
def save_text(*args):
	for i in args:
		with open ("qiushi.txt","a+",encoding="utf-8") as f:
			f.write(i)

def main():
	for i in range(10,14):
		url = "https://www.qiushibaike.com/text/page/{}".format(i)
		print(url)
		html = download_page(url)
		get_content(html,i)
if __name__ == "__main__":
	main()