import requests
from requests.auth import HTTPBasicAuth
# r = requests.get('https://static3.scrape.cuiqingcai.com/',auth=HTTPBasicAuth('admin','admin'))
# print(r.status_code)
r = requests.get('https://static3.scrape.cuiqingcai.com/',auth=('admin','admin'))
print(r.status_code)