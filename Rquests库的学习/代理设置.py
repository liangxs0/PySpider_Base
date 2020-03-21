import requests
proxies = {
    'http':'http://10.1.1.1:1000',
    'https':'http://1.1.1.1:1000'
}
proxies1 = {
    'https':'http://use"passwork@1.1.1.1:200'#需要以上认证时候
}
#socket协议代理
proxies2 = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}
requests.get('https://httpbin.org/get',proxies=proxies)


