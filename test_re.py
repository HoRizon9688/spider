import re

text = '''{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-6251b649-380e733e2b145f1268077369"
  }, 
  "origin": "58.53.43.193", 
  "url": "http://httpbin.org/get"
}'''

# find_date = re.compile(r'<b>(.*)</b>')
# find_value = re.compile(r'<span>(.*)</span>')
# data = find_date.findall(text)
# value = find_value.findall(text)
# for i, j in zip(data, value):
#     print(i, j)

find_origin = re.compile(r'"origin": "(.*)",')
origin = find_origin.findall(text)
print(origin)
