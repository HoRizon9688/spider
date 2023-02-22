# -*- coding: utf-8 -*-
# @Project: spider
# @Author: HoRizon
# @Time: 2023/2/22 9:23
# 结算电量核对

import re
import xlwt
import pandas as pd
import os


path_changzhan = r'D:/spider/功率预测/'
path_chuqing = r'D:/spider/结算单/'

list_changzhan = os.listdir(path_changzhan)
list_chuqing = os.listdir(path_chuqing)

# for i in range(len(list_chuqing)):
#     df2 = pd.read_excel(path_chuqing + list_chuqing[i], sheet_name=0)
#     target2 = df2.iloc[2:26, 8]
#     chu_qing = []
#     for j in target2:
#         chu_qing.append(j)
#     print(chu_qing)

# 计算每日的分时电量（对应核算单中的场站）
for i in range(len(list_changzhan)):
    df = pd.read_excel(path_changzhan + list_changzhan[i], sheet_name=2)
    target = df.iloc[1:, 2]
    fen_shi = []  # 分时电量
    for j in range(0, 96, 4):
        temp = target[j:j+4].sum()
        fen_shi.append(float(format(temp / 4, '.4f')))
    print(fen_shi)


    df2 = pd.read_excel(path_chuqing + list_chuqing[i], sheet_name=0)
    target2 = df2.iloc[2:26, 8]
    chu_qing = []  # 出清电量
    for k in target2:
        chu_qing.append(k)
    print(chu_qing)


    diff = []
    for l in range(len(fen_shi)):

        diff.append(round(chu_qing[l] - fen_shi[l], 3))
    print(diff)
