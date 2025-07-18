import re
import requests
from requests import RequestException
import time
import random
from bs4 import BeautifulSoup


# 获取网页的response文件
def get_response(url):
    try:
        headers = {
            'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
            # 伪装成浏览器
        }
        # 设置代理ip
        porxy_list = [
            {"http": "http://218.60.8.99:3129"},
            {"http": "http://114.226.244.78:9999"},
            {"http": "http://39.137.95.71:80"},
            {"http": "http://115.159.31.195:8080"},
            {"http": "http://39.137.69.7:8080"},
            {"http": "http://39.106.66.178:80"},
            {"http": "http://101.4.136.34:81"},
            # 最新添加
            {"http": "http://1.197.10.199:9999"},
            {"http": "http://115.216.79.93:9999"},
            {"http": "http://123.149.136.215:999"},
            {"http": "http://39.108.92.182:8888"},
            {"http": "http://221.1.200.242:43399"},
            {"http": "http://175.42.123.88:9999"},
            {"http": "http://223.241.119.0:9999"},
            {"http": "http://59.44.78.30:54069"},
            {"http": "http://114.104.185.114:9999"},
            {"http": "http://163.204.247.84:9999"},
            {"http": "http://123.149.141.128:9999"},
            {"http": "http://223.215.6.181:9999"},
            {"http": "http://106.85.143.27:9999"},
            {"http": "http://123.163.27.131:9999"},
            {"http": "http://61.145.4.204:9999"},
            {"http": "http://183.166.162.198:9999"},
            {"http": "http://110.243.2.57:9999"},
        ]
        proxy = random.choice(porxy_list)
        response = requests.get(url, headers=headers, proxies=proxy)
        if response.status_code == requests.codes.ok:  # 响应状态码是200 或者Requests还附带了一个内置的状态码查询对象
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None


# 获取博客中所有的文章链接,在下面soup对象创建过程中，如果网页编码为其他应该，加一个from_encoding='UTF-8'
def get_url(html, u_name):
    url_list = []
    num = re.findall(r'<div.*?article-item-box csdn-tracking-statistics.*?data-articleid.*?(\d+).*?>', html)
    for x in range(len(num)):
        url = f'https://blog.csdn.net/{u_name}/article/details/{num[x]}'
        url_list.append(url)
    return url_list


# 查询博客有多少页(暂时没想到更好的方法，以后会完善的)
def get_page(u_name):
    var = 1
    while True:
        url = f'https://blog.csdn.net/{u_name}/article/list/{var}'
        list1 = get_url(get_response(url), u_name)
        if len(list1):
            var += 1
        else:
            break
    return var - 1


# 获取文章总阅读量
def get_all(html):
    if html is None:
        print("get_all: 网页内容为空，无法解析阅读量")
        return 0
    match = re.compile(r'<dl.*?text-center.*?title.*?(\d[0-9][0-9][0-9]*).*?>').search(html)
    if match:
        read_num = int(match.group(1))
        return read_num
    else:
        print("get_all: 正则未匹配到阅读量，可能网页结构已变")
        return 0


def parse_page(html):
    try:
        read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
        return read_num
    except Exception:
        print('解析出错')
        return None


# 获取每篇文章标题
def get_name(url):
    html = get_response(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.title.string


# 入口
def main():
    url_old = []        # 用于存储用户每一页的文章链接
    url_new = []        # 用于存储用户的每一篇文章的链接
    var_all = 0         # var_all 用于存储每一轮新增的访问总量总和
    user_name = input("请输入你的CSDN用户名:")
    page_num = get_page(user_name)
    print(f'你的博客一共有{page_num}页')
    # 获取所有文章列表
    for num in range(1):
        temp = num + 1
        url_old.append(f'https://blog.csdn.net/{user_name}/article/list/{temp}')
        url_new += get_url(get_response(url_old[num]), user_name)
    art_num = len(url_new)
    print(f'你的博客目前文章数{art_num}')
    var1 = get_all(get_response(url_new[0]))        # var1 用于存储刷取前的访问总量
    print('当前总阅读量:', var1)
    while True:
        for x in range(len(url_new)):
            html = get_response(url_new[x])
            read_num = parse_page(html)
            print('当前阅读量：', read_num)
            if art_num < 40:
                sleep_time = random.randint(60, 65)
            else:
                sleep_time = 1
            print('please wait', sleep_time, 's')
            time.sleep(sleep_time)  # 设置访问频率，过于频繁的访问会触发反爬虫
            print(f'文章 {x + 1}/{art_num}：')
            print(get_name(url_new[x]), '已成功访问')
        var2 = get_all(get_response(url_new[0]))  # var2 用于存储刷取后的访问总量
        print('当前循环增加的阅读量为：', var2 - var1)
        var_all += (var2 - var1)
        print(f'程序运行期间增加的总阅读量为{var_all}')


if __name__ == '__main__':
    main()