import requests
import time
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'  
}

r = requests.get('https://static1.scrape.cuiqingcai.com/',headers=headers)
print(r.status_code)

