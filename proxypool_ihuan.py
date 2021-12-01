from urllib import request
import pymysql
from bs4 import BeautifulSoup
import urllib
import re

# 获取网站验证的第一页
# find_ip = re.compile(r'<img src="/flag/CN.svg"/>(.*?)</a>')
# find_port = re.compile(r'<td>(\d*)</td>')
#
# conn = pymysql.connect(host='localhost',
#                        user='root',
#                        password='chy200412',
#                        database='proxy_pool')
# cursor = conn.cursor()
# url = "https://ip.ihuan.me/address/5Lit5Zu9.html"
# headers = {
#         'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
#                       "Chrome/71.0.3578.98 "
#                       "Safari/537.36 "
#     }
# req = urllib.request.Request(url=url, headers=headers, method='GET')
# response = urllib.request.urlopen(req)
# html = response.read().decode('utf-8')
# bs = BeautifulSoup(html, "html.parser")
# result = bs.find('table', class_='table table-hover table-bordered')
# ip = find_ip.findall(str(result))
# port = find_port.findall(str(result))
# print(ip)
# print(port)
#
# for i, j in zip(ip, port):
#     sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','HTTP')".format(i, j)
#     cursor.execute(sql)
#     conn.commit()
# conn.close()

f = open('ihuan.txt', 'r', encoding='utf-8')
result = f.read()
proxy_list = []
find_proxy = re.compile(r'(.*)@')
ip_port = find_proxy.findall(result)
print(ip_port)
for i in ip_port:
    proxy = {'http': i}
    proxy_list.append(proxy)
print(proxy_list)

for i in proxy_list:
    proxy_handler = urllib.request.ProxyHandler(i)
    opener = urllib.request.build_opener(proxy_handler)
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
                      "Safari/537.36 "
    }
    request = urllib.request.Request(url='http://httpbin.org/get', headers=headers, method='GET')
    try:
        response = opener.open(request, timeout=20)
    except Exception as e:
        proxy_list.remove(i)
    else:
        # 还需要对返回内容进行判断
        result = response.read(1).decode('utf-8')
        if result != '{':
            proxy_list.remove(i)
        else:
            print("代理可用")

