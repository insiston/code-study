#coding:utf-8

#---------------------------------------
#   程序：get_ip_location.py
#   版本：v0.1
#   作者：vforbox
#   日期：2016-1-4
#   语言：Python 2.7
#   操作：预览帮助信息 ./get_ip_location.py
#   功能：根据IP获取物理位置
#---------------------------------------

import sys
import urllib2
import json

def get_ip_location():
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s"%sys.argv[1]
        content = urllib2.urlopen(apiurl).read()
        code = json.loads(content)["code"]
        data = json.loads(content)["data"]
        if code == 0:
            print u"您查询的IP: %s"%data["ip"]
            print u"国家: %s"%data["country_id"]
            print u"城市: %s"%data["city"]
            print u"运营商: %s"%data["isp"]
        else:
            print data
    except:
        print "Usage: \033[;33m./%s IP\033[0m"%sys.argv[0]

if __name__ == "__main__":
    get_ip_location()