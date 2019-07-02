#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
import urllib
from urllib import request, error
from lxml import etree
import random
import pymysql

'''
爬取招聘网站的工具类
'''


# 根据传入的网址进行获取网页源码，默认编码是utf-8，
def get_html(url, encoding='utf-8'):
    print(url)
    # 模拟请求头，防止反爬封ip
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    ]
    try:
        req = request.Request(url)
        req.add_header("User-Agent", random.choice(user_agents))
        response = request.urlopen(req)
        content = response.read().decode(encoding)
        return content
    except error.URLError as e:
        # URLError
        # 产生的原因主要有：
        # 1.没有网络连接
        # 2.服务器连接失败
        # 3.找不到指定的服务
        print("URL 异常 {}".format(e.reason))
    except error.HTTPError as e:
        # HTTPError 获取响应状态码来判断响应失败的原因
        print("HTTP 异常{}".format(e.reason))
        return None
    except BaseException as e:
        print('有异常{}'.format(e.reason))
    return None



#  将爬虫的数据写入到文件中
def write(url, filname):
    try:
        urllib.request.urlretrieve(url, filname)
        print('...【下载成功】')
    except:
        print('...【下载失败】')



# 获取第2层链接集合
def get_url02(url01):
    # 第一级
    # url01 = 'http://www.en8848.com.cn/kouyu/'
    # 获取网页源码
    html01 = get_html(url01, 'utf-8')
    if html01 == None:
        return None
    # print(html)
    # 转为dom树
    content = etree.ElementTree(etree.HTML(html01))
    # xpath解析，获取第二层的链接
    url02s = content.xpath(r'//div[contains(@class,"warp") and contains(@class,"ch_subnav_news")]/h2/a/@href')
    url02names = content.xpath(r'//div[contains(@class,"warp") and contains(@class,"ch_subnav_news")]/h2/a/text()')
    # 定义一个map, 用来存第2层的键值对
    url02map = {}
    i2 = 0
    for url02 in url02s:
        url02temp = url01 + url02.split('/')[2] + '/'
        # print(url02temp)
        url02map[url02names[i2]] = url02temp
        i2 += 1
    # print(len(url03map))
    # print(url03map)
    return url02map


# 获取第3层链接集合
def get_url03(url02):
    # 第二层的第一个url
    # url0201 = 'http://www.en8848.com.cn/kouyu/basic/'
    # 获取网页源码
    html02 = get_html(url02, 'utf-8')
    if html02 == None:
        return None
    # print(html)
    # 转为dom树
    content = etree.ElementTree(etree.HTML(html02))
    # xpath解析，获取第三层的链接
    url03s = content.xpath(r'//div[@class="ch_warp_left"]/ul[@class="ch_list_nav"]/li/a/@href')
    url03names = content.xpath(r'//div[@class="ch_warp_left"]/ul[@class="ch_list_nav"]/li/a/text()')

    # 定义一个map, 用来存第3层的键值对
    url03map = {}
    i3 = 0
    for url03 in url03s:
        url03temp = url02 + url03.split('/')[3] + '/'
        url03map[url03names[i3]] = url03temp
        i3 += 1
    # print(len(url03map))
    # print(url03map)
    return url03map



# 获取第4层链接集合
def get_url04(url03):
    # 第3层的第一个url
    # url0301 = 'http://www.en8848.com.cn/kouyu/basic/useful1000/'
    # 获取网页源码
    html03 = get_html(url03, 'utf-8')
    if html03 == None:
        return None
    # print(html)
    # 转为dom树
    content = etree.ElementTree(etree.HTML(html03))
    # xpath解析，获取第4层的链接
    url04s = content.xpath(r'//div[@class="ch_content"]/div[@class="ch_lii"]/div[@class="ch_lii_left"]/a/@href')
    url04names = content.xpath(r'//div[@class="ch_content"]/div[@class="ch_lii"]/div[@class="ch_lii_left"]/a/text()')

    # 定义一个map, 用来存第3层的键值对
    url04map = {}
    i4 = 0
    # 对url进行拼接处理
    for url04 in url04s:
        key = get_html(url04)
        if key == None:
            return None

        # 表达式
        # \$\("\.jp-download"\)\.click\(function\(\){\s*window\.open\('\S*
        p = '\$\("\.jp-download"\)\.click\(function\(\){\s*window\.open\(\S*'
        # 我们在编译这段正则表达式
        pattern = re.compile(p)
        # 在源文本中搜索符合正则表达式的部分
        matcher = re.search(pattern, key)
        # print(matcher)
        urlTmp = ''
        if not matcher == None:
            split = matcher[0].split('\'')[1]
            urlTmp = 'http://www.en8848.com.cn' + split
            print(urlTmp)
        else:
            print('正则表达式出问题了')
        url04map[url04names[i4]] = urlTmp
        i4 += 1
    # print(len(url04map))
    # print(url04map)
    return url04map








# 进行最后的目标url获取,并下载
def url_final(url, urlname, filename):
    # '实用英语口语1000句 001-025':
    # 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3'
    # 获取网页源码
    html04 = get_html(url, 'utf-8')
    if html04 == None:
        return None
    # print(html)
    # 转为dom树
    content = etree.ElementTree(etree.HTML(html04))
    # xpath解析，获取第4层的链接 //*[@id="dload"]
    url04MP3s = content.xpath(r'//*[@id="dload"]/@href')
    url04LRCs = content.xpath(r'//*[@id="dloadword"]/@href')

    # 遍历下载
    for url04MP3 in url04MP3s:
        print(url04MP3)
        write(url04MP3, filename + urlname + '.mp3')
    for url04LRC in url04LRCs:
        print(url04LRC)
        write(url04LRC, filename + urlname + '.lrc')






















def connect_DB(row, province_name):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "1234", "mypython")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行插入操作
    sql = "INSERT INTO company_51job_cloudcom (province, job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number) " \
          " VALUES " \
          "(\"" + province_name + "\",\"" + row[0] + "\",\"" + row[1] + "\",\"" + row[2] + "\",\"" + row[3] + "\",\"" + \
          row[4] + "\",\"" + row[5] + "\",\"" + row[6] + "\",\"" + row[7] + "\",\"" + row[8] + "\");"
    print('数据库执行： ', sql)
    cursor.execute(sql)
    db.commit()
    db.close()

# # http://www.en8848.com.cn/kouyu/basic/useful1000/325707.html
# # 获取最后的数字，用来拼接
# id = url04.split('/')[-1].split('.')[0]
# url04.split('/')
# if j4 < 10:
#     # http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3
#     url0401Tmp = 'http://www.en8848.com.cn/e/action/down.php?classid=' + classid +'&id=' + id + \
#                  '&mp3=http://mp3.en8848.com/kouyu/useful1000/0' + str(j4) + '.mp3'
# else:
#     url0401Tmp = 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=' + id + \
#                  '&mp3=http://mp3.en8848.com/kouyu/useful1000/' + str(j4) + '.mp3'
# j4 = int(j4)
# j4 += 1