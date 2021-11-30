import pymysql
import urllib.request
from urllib import request

# 存在重复测试某个代理的问题，改用test_proxy.py
#
#
#
#
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
get_row = "select count(*) from proxy_ip"
cursor.execute(get_row)
row = cursor.fetchone()
for i in range(0, row[0]):
    sql = "select ip,port,proxy_type from proxy_ip ORDER BY `port` limit {},1".format(i)
    cursor.execute(sql)
    result = cursor.fetchone()
    ip_port = "{}:{}".format(result[0], result[1])
    proxy_type = result[2].lower()
    proxy = {proxy_type: ip_port}
    print(proxy)
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
                      "Safari/537.36 "
    }
    request = urllib.request.Request(url='http://httpbin.org/get', headers=headers, method='GET')
    try:
        response = opener.open(request)
    except Exception as e:
        sql = "update proxy_ip set available='N' where ip='{}'".format(result[0])
        cursor.execute(sql)
        conn.commit()
        print("失效代理已标记")
        continue
    else:
        sql = "update proxy_ip set available='Y' where ip='{}'".format(result[0])
        cursor.execute(sql)
        conn.commit()
        print(response.status)
        print("可用代理已标记")
        continue
conn.close()
