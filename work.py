import time
import urllib
import urllib2

url = 'http://www.pctowap.com/air/m.blog.csdn.net/article/details?id=54632384#'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'WHY',
                  'location': 'SDU',
                            'language': 'Python'}

headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
cnt = 1
while cnt <= 10000:
        response = urllib2.urlopen(req)
            print cnt
                cnt += 1
                    time.sleep(1.0)
