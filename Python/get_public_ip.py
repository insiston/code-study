#coding:utf-8

#---------------------------------------
#   程序：get_public_ip.py
#   版本：v0.1
#   作者：vforbox
#   日期：2016-1-4
#   语言：Python 2.7
#   操作：直接运行
#   功能：获取公网地址
#---------------------------------------

import re
import urllib2

class Get_public_ip:
    def get_ip(self):
        try:
            myip = self.visit("http://www.whereismyip.com/")
        except:
            myip = "So sorry!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
            match = re.search(r'\d+.\d+.\d+.\d+',str).group(0)
            return match
            
if __name__ == "__main__":
    getmyip = Get_public_ip()
    print getmyip.get_ip()