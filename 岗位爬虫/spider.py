import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

def GetJson(url,page):
	data = {
		"first":"false",
		"pn":page,
		"kd":"python"
	}
	headers = {
		# 'Host':'www.lagou.com',
		# 'Origin': 'https://www.lagou.com',
		'Referer': 'https://www.lagou.com/jobs/list_python/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput=',
		# 'X-Anit-Forge-Code': '0',
		# 'X-Anit-Forge-Token': 'None',
		# 'X-Requested-With': 'XMLHttpRequest',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
	}
	# s = requests.Session()
	# s.get(url,headers=headers,timeout=4)
	# cookies = s.cookies
	# print(cookies)
	cookies = {'Cookie':' _qddaz=QD.1tyi4i.ok3b8y.k3tlqaju; user_trace_token=20200209142957-61f07bcb-fccc-43ab-9c23-a4a313a21584; _ga=GA1.2.922404317.1581229798; LGUID=20200209142958-b7cdcdee-0353-4d0f-ade2-cbbb0e15b168; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217028a42ba6534-08ece9604bdfdc-b383f66-1327104-17028a42ba7a7d%22%2C%22%24device_id%22%3A%2217028a42ba6534-08ece9604bdfdc-b383f66-1327104-17028a42ba7a7d%22%7D; gate_login_token=8369ea5007a7f71443507f5872aaec4af88ca9f46346a3e438624492928e79a0; LG_LOGIN_USER_ID=6d31e88f1445a88201a8936ea528047ad5f5bbf229b4ddbf22fb52660fe4ab25; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E4%B8%8A%E6%B5%B7; privacyPolicyPopup=false; LGSID=20200211151540-91f43eb1-e87a-40db-8932-577a98cc0f52; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw%5F0k2Ph0FNkUsauNDFX00000F2xgNC00000x2U7y0.THL0oUhY1x60UWdBmy-bIfK15ymYPHcsmHf3nj0srHPBnHm0IHdKrDP7rDFDPj6dPDcknDD4nDR3PWm1PjuAfbckP1b1w6K95gTqFhdWpyfqn1n1nWfkn1nYnBusThqbpyfqnHmhIAYqniuB5HD0uHdCIZwsT1CEQLILIz4%5FmyIEIi4WUvYEUA78uA-8uzdsmyI-QLKWQLP-mgFWpa4CIAd%5F5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqn1c3rjT%26tpl%3Dtpl%5F11534%5F21264%5F17382%26l%3D1516085138%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E3%252580%252591-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3332413342%5Fcanvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D232%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581229798,1581405340; _putrc=B02BCA36DD54FD83123F89F2B170EADC; JSESSIONID=ABAAAECABBJAAGI9A034A7A5F80ADD63553B27E7A613C87; login=true; unick=%E6%A2%81%E6%99%93%E5%A3%B0; WEBTJ-ID=20200211151603-170331adb79722-01dd2ce41a86d8-b383f66-1327104-170331adb7a2f7; _gid=GA1.2.1415870771.1581405364; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=e45c01562705ffcf9495041851ef6b0e5c9acde791; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581405949; LGRID=20200211152549-5dde95fd-5757-4ea6-a6a6-168e530eb6f3; SEARCH_ID=59cba8b1741f4cc3a34dbec54ff6d052'}
	json = requests.post(url=url,data=data,headers=headers,cookies=cookies).json()
	print(json)

GetJson(url=url,page=1)