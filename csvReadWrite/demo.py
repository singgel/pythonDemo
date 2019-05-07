#!/usr/bin/python
# -*- coding:utf-8 -*-
# 昏鸦

import requests
import re
import sys
import time
import random
import csv
import codecs


def get_baidu(s, page=5):
    csvfile = open("result.csv", 'wb')
    csvfile.write(codecs.BOM_UTF8)
    fwcsv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    pattern = "data-tools='{\"title\":\"(.*?)\",\"url\":\"(.*?)\""

    for p in xrange(0, page * 10 + 1, 10):
        time.sleep(random.randint(100, 2000) * 0.001)
        req = "http://www.baidu.com/s?wd={}&pn={}&cl=3".format(s + ' site:xueqiu.com', p)
        res = requests.get(url=req).text
        reg = re.findall(pattern, res)

        for i in xrange(len(reg)):
            title = reg[i][0]
            url = requests.get(url=reg[i][1]).url
            matchObj = re.match('https://xueqiu.com/(\d+)/(\d+).*', url, re.I)
            if matchObj:
                text = [s, matchObj.group(2).encode('utf-8')]
                fwcsv.writerow(text)


#            	print s + ',' + matchObj.group(2).encode('utf-8')
#	    else:
#		print s + ',' + url.encode('utf-8') + '\n\n'

if __name__ == '__main__':
    words = ["宇宙党", "饥荒", "肃反", "18亿亩", "违宪", "集权", "极权", "威权", "熊才大劣", "熊才伟劣", "独裁", "开倒车", "大倒退", "大清洗", "金元外交", "龙脉",
             "昏聩", "一尊", "熊安", "红色权贵", "专权", "好大喜功", "当今CEO", "九长老", "这一届", "某人", "防民之口", "我党", "我裆", "李锐", "李央南",
             "中国专制独裁者", "今上", "长老会", "国子监派", "团派", "宪政", "宪镇", "皿煮", "民猪", "DZY", "WG", "屁民利益极端", "毒菜", "独才", "独材",
             "毒裁", "独菜", "真压学生运动", "学生韵动", "砖制", "王裆", "w当w锅", "含赵量", "含Z量"]
    for word in words:
        get_baidu(word, 10)
