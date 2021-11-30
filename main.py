from urllib import request, parse
from bs4 import BeautifulSoup
import bs4
import urllib
import re
import xlwt

# url = ''
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
#                   "Safari/537.36 "
# }
# req = request.Request(url=url, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

find_date = re.compile(r'<b>(.*)</b>')
find_value = re.compile(r'<span>(.*)</span>')


f = open('info.txt', 'r', encoding='utf-8')
html = f.read()
bs = BeautifulSoup(html, "html.parser")
result = bs.find_all('div', class_='fjlist-box boxstyle2', limit=1)
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for text in result:
    text = str(text)
    data = find_date.findall(text)
    value = find_value.findall(text)
    # for i, j in zip(data, value):
    #     print(i, j)
    for i in range(0, 12):
        worksheet.write(i, 0, data[i])
        worksheet.write(i, 1, value[i])
workbook.save('test.xls')

