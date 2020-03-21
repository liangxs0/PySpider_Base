import requests
r = requests.get('http://www.baidu.com')
print(r.cookies)
print(type(r.cookies))
for key,value in r.cookies.items():
    print(key+'='+value)