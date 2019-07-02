# 1、英语口语-》集合（创建文件夹）-》遍历-》
# 2、入门口语-》集合（创建文件夹）-》遍历-》
# 3、实用英语口语1000句-》集合（创建文件夹）-》遍历-》
# 4、获取连接，下载.mp3、.lrc到本地
import os

from tools import get_html, url_final, get_url04, get_url03, get_url02
from concurrent.futures import ThreadPoolExecutor
import tools
from lxml import etree
import urllib


# 第一级
url01 = 'http://www.en8848.com.cn/kouyu/'

url02map = get_url02(url01)

# filename = ''
# for key02 in url02map.keys():
#     url02Tmp = url02map.get(key02)


def threadTmp(url02Tmp, key02):
    # 第二层的第一个url
    # url0201 = 'http://www.en8848.com.cn/kouyu/basic/'
    url03map = get_url03(url02Tmp)
    for key03 in url03map.keys():
        url03Tmp = url03map.get(key03)
        # 第3层的第一个url
        # url0301 = 'http://www.en8848.com.cn/kouyu/basic/useful1000/'
        url04map = get_url04(url03Tmp)
        if url04map == None:
            continue
        # 遍历第4层的链接，并下载
        filename = 'H://englishListen/' + key02 + '/' + key03 + '/'
        # 新建文件夹
        if not os.path.exists(filename):
            os.makedirs(filename)
        for key04 in url04map.keys():
            if key04 == '':
                continue
            url04Tmp = url04map.get(key04)
            if url04Tmp == None:
                continue
            url_final(url04Tmp, key04, filename)


def main():
    with ThreadPoolExecutor(10) as executor:
        for key02 in url02map.keys():
            executor.submit(threadTmp, url02map.get(key02), key02)


if __name__ == '__main__':
    main()













# # 第一级
# url01 = 'http://www.en8848.com.cn/kouyu/'
# # 获取网页源码
# html01 = get_html(url01, 'utf-8')
# # print(html)
# # 转为dom树
# content = etree.ElementTree(etree.HTML(html01))
# # xpath解析，获取第二层的链接
# url02s = content.xpath(r'//div[contains(@class,"warp") and contains(@class,"ch_subnav_news")]/h2/a/@href')
# url02names = content.xpath(r'//div[contains(@class,"warp") and contains(@class,"ch_subnav_news")]/h2/a/text()')
#
# # 定义一个map, 用来存第2层的键值对
# url02map = {}
# i2 = 0
# for url02 in url02s:
#     url02temp = url01 + url02.split('/')[2] + '/'
#     # print(url02temp)
#     url02map[url02names[i2]] = url02temp
#     i2 += 1
# # print(url02map)
#
# # 遍历map
# for key in url02map.keys():
#     # print(key)
#     k = url02map.get(key)
#     # print(k)





#
# # 第二层的第一个url
# url0201 = 'http://www.en8848.com.cn/kouyu/basic/'
# # 获取网页源码
# html02 = get_html(url0201, 'utf-8')
# # print(html)
# # 转为dom树
# content = etree.ElementTree(etree.HTML(html02))
# # xpath解析，获取第三层的链接
# url03s = content.xpath(r'//div[@class="ch_warp_left"]/ul[@class="ch_list_nav"]/li/a/@href')
# url03names = content.xpath(r'//div[@class="ch_warp_left"]/ul[@class="ch_list_nav"]/li/a/text()')
#
# # 定义一个map, 用来存第3层的键值对
# url03map = {}
# i3 = 0
# for url03 in url03s:
#     url03temp = url0201 + url03.split('/')[3] + '/'
#     url03map[url03names[i3]] = url03temp
#     i3 += 1
# # print(len(url03map))
# # print(url03map)
#
# # 遍历map
# for key in url03map.keys():
#     # print(key)
#     k = url03map.get(key)
#     # print(k)



#
# # 第3层的第一个url
# url0301 = 'http://www.en8848.com.cn/kouyu/basic/useful1000/'
# # 获取网页源码
# html03 = get_html(url0301, 'utf-8')
# # print(html)
# # 转为dom树
# content = etree.ElementTree(etree.HTML(html03))
# # xpath解析，获取第4层的链接
# url04s = content.xpath(r'//div[@class="ch_content"]/div[@class="ch_lii"]/div[@class="ch_lii_left"]/a/@href')
# url04names = content.xpath(r'//div[@class="ch_content"]/div[@class="ch_lii"]/div[@class="ch_lii_left"]/a/text()')
# # 定义一个map, 用来存第3层的键值对
# url04map = {}
# i4 = 0
# j4 = 1
# # 对url进行拼接处理
# for url04 in url04s:
#     # http://www.en8848.com.cn/kouyu/basic/useful1000/325707.html
#     # 获取最后的数字，用来拼接
#     split0401 = url04.split('/')[-1].split('.')[0]
#     if j4 < 10:
#         # http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3
#         url0401Tmp = 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=' + split0401 + \
#                      '&mp3=http://mp3.en8848.com/kouyu/useful1000/0' + str(j4) + '.mp3'
#     else:
#         url0401Tmp = 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=' + split0401 + \
#                      '&mp3=http://mp3.en8848.com/kouyu/useful1000/' + str(j4) + '.mp3'
#     j4 = int(j4)
#     j4 += 1
#     url04map[url04names[i4]] = url0401Tmp
#     i4 += 1
# # print(len(url04map))
# # print(url04map)

# # 遍历第4层的链接，并下载
# for key in url04map.keys():
#     url04Tmp = url04map.get(key)
#     url_final(url04Tmp, key)


# # 进行最后的目标url获取
# # '实用英语口语1000句 001-025':
# # 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3'
# url0401 = 'http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3'
# # 获取网页源码
# html04 = get_html(url0401, 'utf-8')
# # print(html)
# # 转为dom树
# content = etree.ElementTree(etree.HTML(html04))
# # xpath解析，获取第4层的链接 //*[@id="dload"]
# url04MP3s = content.xpath(r'//*[@id="dload"]/@href')
# url04LRCs = content.xpath(r'//*[@id="dloadword"]/@href')
#
# i5 = 1
# for url04MP3 in url04MP3s:
#     print(url04MP3)
#     write(url04MP3, str(i5) + '.mp3')
#     i5 = int(i5)
#     i5 += 1
# i5 = 1
# for url04LRC in url04LRCs:
#     print(url04LRC)
#     write(url04LRC, str(i5) + '.lrc')
#     i5 = int(i5)
#     i5 += 1
#
