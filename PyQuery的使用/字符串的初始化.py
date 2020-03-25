html = '''
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item item</a></li>
    </ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)#将字符串初始化为pyquery的对象
print(doc('li'))#将css选择器

