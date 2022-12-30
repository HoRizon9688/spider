from urllib import request
import pymysql
from bs4 import BeautifulSoup
import urllib
import re

# 获取网站验证的第一页
find_ip = re.compile(r'<img src=".*?"/>(\d*\.\d*\.\d*\.\d*)</a>')
find_port = re.compile(r'<td>(\d*?)</td>')

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
url = "https://ip.ihuan.me/?page=b97827cc"
headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                      "Chrome/71.0.3578.98 "
                      "Safari/537.36 "
    }
req = urllib.request.Request(url=url, headers=headers, method='GET')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")
result = bs.find('table', class_='table table-hover table-bordered')
# print(result)
ip = find_ip.findall(str(result))
port = find_port.findall(str(result))
print(ip)
print(port)


for i, j in zip(ip, port):
    sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','HTTP')".format(i, j)
    cursor.execute(sql)
    conn.commit()
conn.close()
