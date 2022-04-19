import urllib.request
from urllib import request, parse
import time
import random
import pymysql
import re
import xlwt
from bs4 import BeautifulSoup


def get_data(area_name):
    baseurl = "http://www.anjuke.com/fangjia/chongqing2021/"
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
    find_value = re.compile(r'<span>(\d*)元')
    error_area = {}

    for key, value in area_name.items():
        url = baseurl + value
        print(url)
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        error_count = 0
        for i in range(1, 5):
            sql = "select distinct ip,port,proxy_type from proxy_ip group by ip order by rand() limit 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            ip_port = "{}:{}".format(result[0], result[1])
            proxy_type = result[2].lower()
            proxy = {proxy_type: ip_port}
            proxy_handler = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(proxy_handler)
            print(proxy)
            try:
                response = opener.open(req, timeout=20)
            except Exception:
                error_count += 1
                print("代理失效，第{}次尝试重新选取代理".format(i))
                time.sleep(random.randint(5, 10))
                # del_sql = "delete from proxy_ip where ip='{}'".format(result[0])
                # cursor.execute(del_sql)
                # conn.commit()
                continue
            else:
                html = response.read().decode('utf-8')
                # print(html)
                bs = BeautifulSoup(html, "html.parser")
                info = bs.find('div', class_='fjlist-box boxstyle2')
                break
        if error_count == 4:
            print("代理应用失败，使用本机直接访问")
            try:
                response = urllib.request.urlopen(req)
            except Exception:
                print("获取失败")
                error_area[key] = value
                continue
            else:
                html = response.read().decode('utf-8')
                # print(html)
                bs = BeautifulSoup(html, "html.parser")
                info = bs.find('div', class_='fjlist-box boxstyle2')
            # for i in info:
            #     data = find_date.findall(str(i))
            #     num = find_value.findall(str(i))
            #     for j, k in zip(data, num):
            #         print(j, k)
        print("正在处理{}".format(key))
        data = find_date.findall(str(info))
        timestamp = []
        for item in data:
            val_time = re.sub('[\u4e00-\u9fa5]', '', item)
            timestamp.append(val_time)
        num = find_value.findall(str(info))
        timestamp.reverse()
        num.reverse()
        if timestamp:
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('sheet1')
            worksheet.write(0, 0, "id")
            worksheet.write(0, 1, "timestamp")
            worksheet.write(0, 2, "price")
            for i in range(0, len(timestamp)):
                worksheet.write(i+1, 0, area_id[key])
                worksheet.write(i+1, 1, timestamp[i])
                worksheet.write(i+1, 2, num[i])
            workbook.save('{}.xls'.format(key))
            print("Start : %s" % time.ctime())
            time.sleep(random.randint(10, 25))
            print("End : %s" % time.ctime())
        else:
            print("获取失败")
            # del_sql = "delete from proxy_ip where ip='{}'".format(result[0])
            # cursor.execute(del_sql)
            # conn.commit()
            error_area[key] = value
        if error_area:
            for k in error_area.keys():
                print(k)

    return error_area


area_name = {"渝北": "yubei", "江北": "jiangbei", "沙坪坝": "shapingba", "南岸": "nanana", "九龙坡": "jiulongpo",
             "渝中": "yuzhong", "巴南": "banan", "大渡口": "dadukou", "北碚": "beibei", "万州": "wanzhouqu", "璧山": "bishanqu",
             "合川": "hechuanqu", "永川": "yongchuanqu", "江津": "jiangjinqu", "涪陵": "fulingqu", "铜梁": "tongliangqu",
             "长寿": "changshouqu", "潼南": "tongnanqu", "荣昌": "rongchangqu", "开州": "kaizhouqukaixian", "大足": "dazhuqu",
             "南川": "nanchuanqu", "垫江": "dainjiangxian", "綦江": "qijiangqu", "梁平": "liangpingxian",
             "丰都": "fengduxian", "武隆": "wulongxian", "奉节": "fengjiexian", "云阳": "yunyangxian",
             "石柱": "shizhutujiazuzizhixian", "秀山": "xiushantujiazumiaozuzizhixian", "忠县": "zhongxian",
             "彭水": "pengshuimiaozutujiazuzizhixian", "黔江": "qianjiangqu", "巫山": "cqwushanxian",
             "酉阳": "youyangtujiazumiaozuzizhixian", "巫溪": "wuxixian"}

area_id = {"渝北": "1", "江北": "2", "沙坪坝": "3", "南岸": "4", "九龙坡": "5",
           "渝中": "6", "巴南": "7", "大渡口": "8", "北碚": "9", "万州": "10", "璧山": "11",
           "合川": "12", "永川": "13", "江津": "14", "涪陵": "15", "铜梁": "16",
           "长寿": "17", "潼南": "18", "荣昌": "19", "开州": "20", "大足": "21",
           "南川": "22", "垫江": "23", "綦江": "24", "梁平": "25",
           "丰都": "26", "武隆": "27", "奉节": "28", "云阳": "29",
           "石柱": "30", "秀山": "31", "忠县": "32",
           "彭水": "33", "黔江": "34", "巫山": "35",
           "酉阳": "36", "巫溪": "37"}

error_area = get_data(area_name)
while error_area:
    print("获取失败的地区：")
    for key in error_area.keys():
        print(key)
    error_area = get_data(error_area)
print("获取完毕")
