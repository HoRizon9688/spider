# -*- coding: utf-8 -*-
# @Project: spider
# @Author: HoRizon
# @Time: 2022/12/30 10:25

from bs4 import BeautifulSoup
import re
import copy
import xlwt

# 正则待补充
find_datetime = re.compile(r'<td>(.*:.*)</td>')
find_prediction = re.compile(r'<td>(.*\.[0-9])</td>')


file = open('rengongyubao.jsp.html', 'rb')
html = file.read()

bs = BeautifulSoup(html, "html.parser")

target = bs.find_all('table', id='YCTable')

# 通过正则提取得到两个长度为96(4*24)的list,时间为00:15到第二天00:00
datetime = find_datetime.findall(str(target))
origin_pre = find_prediction.findall(str(target))


# print(datetime)
# print(origin_pre)

flag = "y"
modified_pre = copy.deepcopy(origin_pre)

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

worksheet.write(0, 0, "时间")
worksheet.write(0, 3, "原始预测功率")
worksheet.write(0, 5, "人工预测功率")
style = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue')
for i in range(96):
    worksheet.write(i+1, 0, datetime[i])
    worksheet.write(i+1, 3, origin_pre[i])

while True:
    if flag == 'y':
        start_time = input("输入开始时间: ")
        end_time = input("输入结束时间: ")
        rate = input("输入倍率: ")

        # 测试用例
        # start_time = "00:30"
        # end_time = "02:00"
        # rate = "1.2"

        # 时间处理
        start_hour = start_time.split(":")[0]
        start_minute = start_time.split(":")[1]

        end_hour = end_time.split(":")[0]
        end_minute = end_time.split(":")[1]

        # 小时数第一位为0则删去
        if start_hour[0] == '0':
            start_hour = start_hour[1]
        if end_hour[0] == '0':
            end_hour = end_hour[1]

        start_index = int(start_hour) * 4 + int(start_minute) // 15 - 1
        end_index = int(end_hour) * 4 + int(end_minute) // 15 - 1

        # print(start_index)
        # print(end_index)

        # modified_pre = copy.deepcopy(origin_pre)
        modified_pre = [float(x) for x in modified_pre]

        for i in range(start_index, end_index + 1):
            modified_pre[i] = float(format(modified_pre[i] * float(rate), '.1f'))

        print("------------------------------------------------")
        flag = input("是否继续修改？ (y\\n)  ")

        for i in range(start_index, end_index + 1):
            worksheet.write(i+1, 5, modified_pre[i], style)

    else:
        break

# print(origin_pre)
# print(modified_pre)

# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('sheet1')
#
# worksheet.write(0, 0, "时间")
# worksheet.write(0, 3, "原始预测功率")
# worksheet.write(0, 5, "人工预测功率")
# style = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue')

# for i in range(96):
#     worksheet.write(i+1, 0, datetime[i])
#     worksheet.write(i+1, 3, origin_pre[i])
#     worksheet.write(i+1, 5, modified_pre[i])

workbook.save('test.xls')
