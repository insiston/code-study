#coding:utf-8

#-------------------------------------------------
#   程序：baidu_tieba.py
#   作者：vforbox
#   日期：2015-12-22
#   语言：python2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数
#   功能：下载对应页码内的所有页面并存储为html文件
#-------------------------------------------------

import string
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('gbk')

#-------------------这里是输入参数-------------------------#
bdurl = raw_input(u'请输入贴吧的地址,去掉?pn=后面的数字： ')
begin_page = int(raw_input(u'请输入开始的页面： '))
end_page = int(raw_input(u'请输入终点的页面： '))
#-------------------这里是输入参数-------------------------#

def baidu_tieba(url,begin_page,end_page):
    for item in range(begin_page,end_page):
        #自动填充文件名#
        strName = string.zfill(item,1) + '.html'
        print u'正在下载第' + str(item) + u'个网页',u'并存储为 ' + strName + ' ......'
        f = open(strName,'w+')
        m = urllib2.urlopen(url=bdurl).read()
        f.write(m)
        f.close()
        
baidu_tieba(bdurl,begin_page,end_page)