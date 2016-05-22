#!/usr/bin/env python
#coding:utf-8

"""
    GITV 1.0 This is a .gitignore file builder
         Author By vforbox, 2016 4
"""
import re
import sys
import urllib2
import time
import os

try:
	from tqdm import *
except ImportError:
	if os.name == 'posix':
		os.system('pip install tqdm > /dev/null')
		from tqdm import *
	else:
		os.system('pip install tqdm')
		from tqdm import *

def get_ignore(url):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
	headers = {'User-Agent':user_agent}
	file = open('.gitignore','w+')
	try:
		request = urllib2.Request(url,headers=headers)
		response = urllib2.urlopen(request)
		content = response.read().decode('utf-8')
		pattern = re.compile(r'<tr>.*?<td id="LC\d+".*?>(.*?)</td>.*?</tr>',re.S)
		items = re.findall(pattern,content)
		for item in items:
			file.writelines(item + "\n")
			file.flush()
	except urllib2.URLError,e:
		pass
	file.close()

def list_eng(url):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
	headers = {'User-Agent':user_agent}
	try:
		request = urllib2.Request(url,headers=headers)
		response = urllib2.urlopen(request)
		content = response.read().decode('utf-8')
		pattern = re.compile(r'<tr class=".*?">.*?<td class="content">.*?<span.*?>.*?<a.*?>(.*?)</a>.*?</td>.*?</tr>',re.S)
		items = re.findall(pattern,content)
		for item in items:
			print item[:-10],
	except urllib2.URLError,e:
		pass

def usage():
	print u'''
        ╭━━╮╭━━╮╭━━╮╭╮╭╮
        ┃╭━╯╰╮╭╯╰╮╭╯┃┃┃┃
        ┃┃╭╮ ┃┃  ┃┃ ┃┃┃┃
        ┃┃┃┃ ┃┃　┃┃ ┃┃┃┃
        ┃╰╯┃╭╯╰╮ ┃┃ ╰╮╭╯
        ╰━━╯╰━━╯ ╰╯  ╰╯　
    GITV 1.0 This is a .gitignore file builder
          Author By vforbox, 4 Arp 2016\n
    Usage:
\tpython gitv.py <list | ls>   - 列出支持的语言
\tpython gitv.py <Name>        - 在当前目录生成指定语言的过滤文件\n
        	'''

if __name__ == '__main__':
	if (sys.version[0:3] <= '2.6' or sys.version[0:3] >= '3.0'):
		print __doc__
		print u"\t当前代码的运行环境应该是 Python 2.7"
		exit(1)

	start=time.clock()
	try:
		if (sys.argv[1] == 'ls' or sys.argv[1] == 'list'):
			list_eng('https://github.com/github/gitignore')
		else:
			get_ignore('https://github.com/github/gitignore/blob/master/%s.gitignore'%sys.argv[1].capitalize())

		if not sys.argv[1:]:
			usage()

	except KeyboardInterrupt:
		print __doc__
		exit(1)

	except:
		usage()
		exit(1)

	for i in tqdm(range(100)):
		time.sleep((time.clock() - start) / 100)
	print "\n(%.2f seconds)" %(time.clock() - start)
