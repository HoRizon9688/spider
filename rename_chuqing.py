# -*- coding: utf-8 -*-
# @Project: spider
# @Author: HoRizon
# @Time: 2023/2/22 10:49

import os
import re


path = r'D:/spider/结算单/'

oldname_list = os.listdir(path)
newname_list = []

for i in oldname_list:
    new_name = re.sub('[\u4e00-\u9fa5]', '', i)
    newname_list.append(new_name.replace(' ', ''))

# print(newname_list)

index = 0
for i in newname_list:
    oldname = path + oldname_list[index]
    newname = path + newname_list[index]
    os.rename(oldname, newname)
    index += 1


