#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
from urllib import request, error
from lxml import etree
import re

from tools import get_html

url = 'http://www.en8848.com.cn/kouyu/basic/yuanlai/218414.html'
html = get_html(url, 'utf-8')
# print(html)
key = html
# 表达式
p = '\$\("\.jp-download"\)\.click\(function\(\){\s*window\.open\(\S.*'
# p = 'html'
# 我们在编译这段正则表达式
pattern = re.compile(p)
# 在源文本中搜索符合正则表达式的部分
matcher1 = re.search(pattern, key)
# 打印出来
print(matcher1)


