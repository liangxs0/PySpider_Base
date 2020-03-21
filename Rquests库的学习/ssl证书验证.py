#https://static2.scrape.cuiqingcai.com/
import requests

# res = requests.get('https://static2.scrape.cuiqingcai.com/')
# print(res.status_code)
# res = requests.get('https://static2.scrape.cuiqingcai.com/',verify=False)
# print(res.status_code)

from requests.packages import urllib3
urllib3.disable_warnings()
res = requests.get('https://static2.scrape.cuiqingcai.com/',verify=False)
print(res.status_code)
