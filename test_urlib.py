import urllib.request
from urllib import request, parse
import time
import random
import pymysql
import re
import xlwt
from bs4 import BeautifulSoup

baseurl = "http://www.anjuke.com/fangjia/chongqing2020/"
area_name = {"巫溪": "wuxixian"}

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}

find_date = re.compile(r'<b>(.*)</b>')
find_value = re.compile(r'<span>(.*)</span>')

for key, value in area_name.items():
    url = baseurl + value
    print(url)
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    error_count = 0
    for i in range(1, 5):
        sql = "select ip,port,proxy_type from proxy_ip group by ip order by rand() limit 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        ip_port = "{}:{}".format(result[0], result[1])
        proxy_type = result[2].lower()
        proxy = {proxy_type: ip_port}
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        print(proxy)
        try:
            response = opener.open(req, timeout=30)
        except Exception as e:
            error_count += 1
            print("代理失效，第{}次尝试重新选取代理".format(i))
            del_sql = "delete from proxy_ip where ip='{}'".format(result[0])
            cursor.execute(del_sql)
            conn.commit()
            continue
        else:
            html = response.read().decode('utf-8')
            # print(html)
            bs = BeautifulSoup(html, "html.parser")
            info = bs.find_all('div', class_='fjlist-box boxstyle2', limit=1)
            break
    if error_count == 4:
        print("使用本机直接访问")
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
        bs = BeautifulSoup(html, "html.parser")
        info = bs.find_all('div', class_='fjlist-box boxstyle2', limit=1)
        # for i in info:
        #     data = find_date.findall(str(i))
        #     num = find_value.findall(str(i))
        #     for j, k in zip(data, num):
        #         print(j, k)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    for text in info:
        text = str(text)
        data = find_date.findall(text)
        num = find_value.findall(text)
        for i in range(0, 12):
            worksheet.write(i, 0, data[i])
            worksheet.write(i, 1, num[i])
    workbook.save('{}.xls'.format(key))
    print("正在处理{}".format(key))
    print("Start : %s" % time.ctime())
    time.sleep(random.randint(30, 60))
    print("End : %s" % time.ctime())
