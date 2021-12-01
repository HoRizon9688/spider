import urllib.request
from urllib import request, parse
import time
import random
import pymysql
import re
import xlwt
from bs4 import BeautifulSoup

baseurl = "https://www.anjuke.com/fangjia/chongqing2020/"
area_name = {"渝北": "yubei", "江北": "jiangbei", "沙坪坝": "shapingba", "南岸": "nanana", "九龙坡": "jiulongpo",
             "渝中": "yuzhong", "巴南": "banan", "大渡口": "dadukou", "北碚": "beibei", "万州": "wanzhouqu", "璧山": "bishanqu",
             "合川": "hechuanqu", "永川": "yongchuanqu", "江津": "jiangjinqu", "涪陵": "fulingqu", "铜梁": "tongliangqu",
             "长寿": "changshouqu", "潼南": "tongnanqu", "荣昌": "rongchangqu", "开州": "kaizhouqukaixian", "大足": "dazuqu",
             "南川": "nanchuanqu", "垫江": "dianjiangxian", "綦江": "qijiangqu", "万盛": "wansheng", "梁平": "liangpingxian",
             "丰都": "fengduxian", "武隆": "wulongxian", "奉节": "fengjiexian", "云阳": "yunyangxian",
             "石柱": "shizhutujiazuzizhixian", "秀山": "xiushantujiazumiaozuzizhixian", "忠县": "zhongxian",
             "彭水": "pengshuimiaozutujiazuzizhixian", "黔江": "qianjiangqu", "巫山": "cqwushanxian",
             "酉阳": "youyangtujiazumiaozuzizhixian", "城口": "chengkouxian", "巫溪": "wuxixian"}


# conn = pymysql.connect(host='localhost',
#                        user='root',
#                        password='chy200412',
#                        database='proxy_pool')
# cursor = conn.cursor()

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
                  "Safari/537.36 "
}

url = baseurl+"shapingba"
print(url)
req = urllib.request.Request(url=url, headers=headers, method='GET')
response = request.urlopen(req)
html = response.read().decode('utf-8')
# print(html)
find_date = re.compile(r'<b>(.*)</b>')
find_value = re.compile(r'<span>(.*)</span>')
bs = BeautifulSoup(html, "html.parser")
info = bs.find_all('div', class_='fjlist-box boxstyle2', limit=1)
for i in info:
    data = find_date.findall(str(i))
    num = find_value.findall(str(i))
    for j, k in zip(data, num):
        print(j, k)
