import requests
data = {
    'name':'tom',
    'age':18
    }
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)