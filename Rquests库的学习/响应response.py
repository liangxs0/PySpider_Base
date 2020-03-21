import requests
r = requests.get('https://static1.scrape.cuiqingcai.com/')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)
exit() if not (r.status_code == requests.codes.ok) else print("request ok")

