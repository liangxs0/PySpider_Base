html = '''
<div id="contain">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item item</a></li>
    </ul>
</div>
'''
from pyquery import PyQuery as pq

doc = pq(html)

print(doc('#contain .list li'))
print(type(doc('#contain .list li')))
#数据类型依旧为<class 'pyquery.pyquery.PyQuery'>
#数据内容获取
for item in doc('#contain .list li').items():
    print(item.text())
#---------------------------------------------------------
#子节点查询
print("-"*40)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
#--------------------------------------------------------
print("-"*40)
lis = items.children()
print(lis)
print(type(lis))
#------------------------------------------------------
print("-"*40)
lis = items.children(".active")
print(lis)
print(type(lis))
#========================================================
#父节点
html = '''
<div class="wrap">
    <div id="contain">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item item</a></li>
        </ul>
</div>
</div>
'''
print("="*40)
doc = pq(html)
items = doc(".list")
container = items.parent()
print(type(container))
print(container)
#===========================================
#先祖节点
print("="*40)
container = items.parents()#container = items.parents(".warp")加入选择器 
print(type(container))
print(container)
#********************************************
#兄弟节点
print("*"*40)
li = doc(".list .item-0.active")
print(li.siblings())#
print("加入CSS选择器")
print(li.siblings(".active"))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#遍历
#多个节点时需要通过遍历获取
lis = doc("li").items()
print("@"*40)
print(type(lis))
for li in lis:
    print(li,type(li))
################################################
#获取信息
#获取属性
