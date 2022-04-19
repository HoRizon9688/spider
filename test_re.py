import re

text = '''<span>15489元/㎡</span>
'''

# find_date = re.compile(r'<b>(.*)</b>')
# find_value = re.compile(r'<span>(.*)</span>')
# data = find_date.findall(text)
# value = find_value.findall(text)
# for i, j in zip(data, value):
#     print(i, j)

# find_origin = re.compile(r'"origin": "(.*)",')
# origin = find_origin.findall(text)
# print(origin)

# find_ip = re.compile(r'<img.*src=".*"/>(\d*\.\d*\.\d*\.\d*)</a>')
# find_port = re.compile(r'<td>(\d*)</td>')
#
# ip = find_ip.findall(text)
# port = find_port.findall(text)
# print(ip)
# print(port)

find_price = re.compile(r'<span>(\d*)元')
price = find_price.findall(text)
print(price)

