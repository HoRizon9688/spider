import urllib.request
from bs4 import BeautifulSoup
import re
import pymysql
from io import BytesIO
import gzip
import urllib

url = "http://httpbin.org/get"
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}

req = urllib.request.Request(url=url, headers=headers, method='GET')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
print(result)
# if result == '{':
#     print("no")

# try:
#     conn = pymysql.connect(host='localhost',
#                          user='root',
#                          password='chy200412',
#                          database='proxy_pool')
#     cursor = conn.cursor()
#     print('连接数据库成功！')
# except Exception as e:
#     print(e)
# else:
#     for i, j, k in zip(ip, port, proxy_type):
#         sql = "insert into proxy_ip(ip,port,proxy_type) values ('{}','{}','{}')".format(i, j, k)
#         cursor.execute(sql)
#         conn.commit()
#     conn.close()
