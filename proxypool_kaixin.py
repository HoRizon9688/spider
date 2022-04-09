import random
import time
from urllib import request
import pymysql
from bs4 import BeautifulSoup
import urllib
import re

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
print("成功连接数据库")
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}

find_ip = re.compile(r'<td>(\d*\.\d*\.\d*\.\d*)</td>')
find_port = re.compile(r'<td>(\d*)</td>')

url = 'http://www.kxdaili.com/dailiip/1/2.html'
req = urllib.request.Request(url=url, headers=headers, method='GET')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")
result = bs.find('table', class_='active')

ip = find_ip.findall(str(result))
port = find_port.findall(str(result))

for i, j in zip(ip, port):
    print(i+":"+j)
    sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','HTTP')".format(i, j)
    cursor.execute(sql)
    conn.commit()
conn.close()
