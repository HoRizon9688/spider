# -*- coding: utf-8 -*-
# @Project: spider
# @Author: HoRizon
# @Time: 2022/12/30 10:25

from bs4 import BeautifulSoup
import re
import xlwt

# 正则待补充
# find_datetime = re.compile('<td>(.*)</td>')
# find_prediction = re.compile('<td></td>')


file = open('rengongyubao.jsp.html', 'rb')
html = file.read()
# print(html)

bs = BeautifulSoup(html, "html.parser")


target = bs.find_all('table', class_='table table-striped table-bordered table-hover table-full-width')
print(target)
