import time
import urllib.request
import urllib.parse

url = 'http://www.pctowap.com/air/m.blog.csdn.net/article/details?id=54632384#'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'WHY',
          'location': 'SDU',
          'language': 'Python'}

headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data, headers)
cnt = 1
while cnt <= 10000:
    response = urllib.request.urlopen(req)
    print(cnt)
    cnt += 1
    time.sleep(1.0)
