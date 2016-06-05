#coding:utf-8

#-------------------------------------------------
#   程序：qsbk_dz.py
#   作者：vforbox
#   日期：2016-1-7
#   语言：python 2.7
#   操作：输入页数
#   功能：爬取糗事百科的段子,不包括图片
#-------------------------------------------------

import urllib2,urllib,re,time,datetime

page = int(raw_input(u'请输入页数：'))
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author.*?">.*?<a.*?<img.*?>(.*?)</a>.*?<a.*?<img.*?title=".*?">(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    
    for item in items:
        haveImg = re.search("img",item[4])
        if not haveImg:
            rep = re.compile('<h2>|</h2>')
            rep_1 = re.compile('</br>')
            text = re.sub(rep,"",item[1])
            text_1 = re.sub(rep_1,"\n",item[2])
            t = time.localtime(int(item[3]))
            timestr = time.strftime("%Y-%m-%d %H:%M:%S")
            print item[0],"发布者：".decode('utf-8').encode('gbk'),text,"内容  ：".decode('utf-8'),text_1,"时间  ：".decode('utf-8'),timestr,"点赞数：".decode('utf-8'),item[5]

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reas