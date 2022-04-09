# 测试单个代理
import re
import urllib.request
import urllib
from urllib.request import urlopen

real_ip = urlopen("https://checkip.amazonaws.com/")
print(real_ip.read().decode('utf-8'))

ip = "125.118.195.225"
port = "7890"
ip_port = "{}:{}".format(ip, port)

proxy_handler = urllib.request.ProxyHandler({"HTTP": ip_port})
opener = urllib.request.build_opener(proxy_handler)
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}

url1 = 'http://httpbin.org/get'
url2 = 'https://httpbin.org/get'
url3 = 'http://baidu.com'

request = urllib.request.Request(url='http://httpbin.org/get', headers=headers, method='GET')
response = opener.open(request)
print(response.status)
result = response.read().decode('utf-8')
print(result)

find_origin = re.compile(r'"origin": "(.*)",')
origin = find_origin.findall(result)
print(origin[0])

if origin and response.status == 200 and origin[0] != real_ip:
    print("PASS")
