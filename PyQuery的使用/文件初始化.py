from pyquery import PyQuery as pq

with open("demo.html",'r') as f:
    print(f.readlines())

doc = pq("demo.html")
print(doc('li'))