import xlwt

data = ["2020年12月房价", "2020年11月房价", "2020年10月房价"]
num = ["12015元/㎡", "11984元/㎡", "11939元/㎡"]
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(0, 3):
    worksheet.write(i, 0, data[i])
    worksheet.write(i, 1, num[i])
workbook.save('xlwt.xls')
worksheet = workbook.add_sheet('sheet2')
worksheet.write(0,0,"test")
workbook.save('xlwt.xls')