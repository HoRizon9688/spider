import random
import time
from urllib import request
import pymysql
from bs4 import BeautifulSoup
import urllib
import re

# 获取网站验证的第一页
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}
for i in range(1, 4):
    url = "http://ip.jiangxianli.com/?page={}&protocol=http".format(i)
    find_ip = re.compile(r'<td>(\d*\.\d*\.\d*\.\d*)</td>')
    find_port = re.compile(r'<td>(\d*)?</td>')
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    bs = BeautifulSoup(html, "html.parser")
    result = bs.find('table', class_='layui-table')
    ip = find_ip.findall(str(result))
    port = find_port.findall(str(result))
    print(ip)
    print(port)

    for j, k in zip(ip, port):
        sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','HTTP')".format(j, k)
        cursor.execute(sql)
        conn.commit()
    print("正在处理第{}页".format(i))
    print("Start : %s" % time.ctime())
    time.sleep(random.randint(20, 40))
    print("End : %s" % time.ctime())
conn.close()
