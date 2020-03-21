import requests

r0 = requests.get('http://httpbin.org/get')
# print(r0.text)
r1 = requests.get('http://httpbin.org/get?name=tom&age=18')
# print(r1.text)
data = {
    "name":"tom",
    "age":18
}
r2 = requests.get('http://httpbin.org/get',params=data)
# print(r2.text)
print(r2.json())
print(type(r2.json()))