import re
import urllib.request
from bs4 import BeautifulSoup
import pymysql
import random
import time
from io import BytesIO
import gzip

find_ip = re.compile(r'<td data-title="IP">(.*)</td>')
find_port = re.compile(r'<td data-title="PORT">(.*)</td>')
find_type = re.compile(r'<td data-title="类型">(.*)</td>')

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
print("数据库连接成功")
for i in range(1, 4):
    baseurl = "https://www.kuaidaili.com/free/inha/"
    url = baseurl + str(i)
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                      "Chrome/71.0.3578.98 "
                      "Safari/537.36 "
    }
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    response = urllib.request.urlopen(req)
    data = response.read()
    flag = data[0:2]
    if flag == b'\x1f\x8b':
        buff = BytesIO(data)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')
        print("gzip")
    else:
        html = data.decode("utf-8")
        print("default")
    bs = BeautifulSoup(html, "html.parser")
    result = bs.find("table", class_="table table-bordered table-striped")
    ip = find_ip.findall(str(result))
    port = find_port.findall(str(result))
    proxy_type = find_type.findall(str(result))
    for j, k, l in set(zip(ip, port, proxy_type)):
        sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','{}')".format(j, k, l)
        cursor.execute(sql)
        conn.commit()
    print("正在处理第{}页".format(i))
    # 等待随机时间
    # print("Start : %s" % time.ctime())
    # time.sleep(random.randint(6, 12))
    # print("End : %s" % time.ctime())
conn.close()
