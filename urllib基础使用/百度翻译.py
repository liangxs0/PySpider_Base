# -*-coding:UTF-8-*-
from urllib import request,parse
import json

# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

def Translate(world):

    FormData = {
        'i': world,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15828778323845',
        'sign': '90be1da5a7a15ef728a7cf35ddaf131b',
        'ts': '1582877832384',
        'bv': '0ed2e07b89acaa1301d499442c9fdf79',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    
    }
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
                'Cookie': '_ntes_nnid=c606c320f23843194b1e6f8ac06b0f29,1575276964464; OUTFOX_SEARCH_USER_ID_NCOO=310576985.85310274; OUTFOX_SEARCH_USER_ID=230197344@10.108.160.127; JSESSIONID=aaaTq7vVEkwgO8NbQ3kcx; ___rl__test__cookies=1582879205875'}
    #使用Urlencode进行格式转换
    data = parse.urlencode(FormData).encode('utf-8')
    #传递Request对象和转换完格式数据携带头
    req = request.Request(url=url,data=data,headers=headers)
    #带有报文得数据区请求
    res = request.urlopen(req)
    #获取信息然后进行解码
    print(res.getcode())
    html = res.read().decode('utf-8')
    #使用json接收数据
    translate = json.loads(html)
    print(translate["translateResult"][0][0]["tgt"])

while(True):
    print("please input worlds：",end="")
    world = input()
    Translate(world)


