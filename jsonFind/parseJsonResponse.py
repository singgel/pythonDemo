# coding:utf8

import urllib
# json解析库,对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath

url = "http://bigdata.yiche.com/testapi/employee/findAll"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}

request = urllib.request.Request(url, headers=header)

response = urllib.request.urlopen(request)
# 取出json文件里的内容，返回的格式是字符串
html = response.read()

# 把json形式的字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)

# python形式的列表
city_list = jsonpath.jsonpath(unicodestr, "$..name")

# 打印每个城市
for i in city_list:
    print
    i

# dumps()默认中文伟ascii编码格式，ensure_ascii默认为Ture
# 禁用ascii编码格式，返回Unicode字符串
array = json.dumps(city_list, ensure_ascii=False)

# 把结果写入到lagouCity.json文件中
with open("lagouCity.json", "wb+") as f:
    f.write(array.encode("utf-8"))
