# 测试代理池中代理
import urllib.request
import pymysql
import re
import urllib.error
from urllib.request import urlopen

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
get_iplist = "select ip from proxy_ip group by ip"
get_portlist = "select port from proxy_ip group by ip"
get_typelist = "select proxy_type from proxy_ip group by ip"
cursor.execute(get_iplist)

iplist = cursor.fetchall()
cursor.execute(get_portlist)
portlist = cursor.fetchall()
cursor.execute(get_typelist)
typelist = cursor.fetchall()

real_ip = urlopen("https://checkip.amazonaws.com/")
print("real_ip:", real_ip.read().decode('utf-8'))

num = len(iplist)

for i in range(0, num):
    ip_port = "{}:{}".format(iplist[i][0], portlist[i][0])
    proxy_type = typelist[i][0].lower()
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
        response = opener.open(request, timeout=10)
    except Exception as e:
        sql = "update proxy_ip set available='N' where ip='{}'".format(iplist[i][0])
        cursor.execute(sql)
        conn.commit()
        print("失效代理已标记")
    else:
        # 还需要对返回内容进行判断
        result = response.read().decode('utf-8')
        find_origin = re.compile(r'"origin": "(.*)",')
        origin = find_origin.findall(result)

        if origin and origin[0] != real_ip.read().decode('utf-8'):
            sql = "update proxy_ip set available='Y' where ip='{}'".format(iplist[i][0])
            cursor.execute(sql)
            conn.commit()
            print(response.status)
            print("可用代理已标记")
        else:
            sql = "update proxy_ip set available='N' where ip='{}'".format(iplist[i][0])
            cursor.execute(sql)
            conn.commit()
            print("失效代理已标记")
conn.close()
