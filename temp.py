import urllib.request
from bs4 import BeautifulSoup
import re
import pymysql
from io import BytesIO
import gzip


# f = open('proxy_ip.txt', 'r', encoding='utf-8')
# html = f.read()

url = "https://www.kuaidaili.com/free/inha/2"
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}
req = urllib.request.Request(url=url, headers=headers, method='GET')
response = urllib.request.urlopen(req)
data = response.read()
flag = data[0:2]

# print(flag, type(flag))
# if flag == b'\x1f\x8b':
#     print("yes")


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
find_ip = re.compile(r'<td data-title="IP">(.*)</td>')
find_port = re.compile(r'<td data-title="PORT">(.*)</td>')
find_type = re.compile(r'<td data-title="类型">(.*)</td>')
ip = find_ip.findall(str(result))
port = find_port.findall(str(result))
proxy_type = find_type.findall(str(result))
for i, j, k in zip(ip, port, proxy_type):
    print(i, j, k)

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
