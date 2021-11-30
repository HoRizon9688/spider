# import urllib.request
#
# proxy_handler = urllib.request.ProxyHandler({"http": "175.10.223.95:8060"})
# opener = urllib.request.build_opener(proxy_handler)
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 "
#                   "Safari/537.36 "
# }
# request = urllib.request.Request(url='http://httpbin.org/get', headers=headers, method='GET')
# response = opener.open(request)
# print(response.status)
# print(response.read().decode('utf-8'))

try:
    x = 'a'
    raise Exception
except:
    x = 'b'
finally:
    print(x.upper())