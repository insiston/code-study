#coding:utf-8
import urllib2  
import urllib  
import cookielib  
import re  
  
# 需要提交post的url   
target_url = "http://ctf.idf.cn/game/pro/37/"  
# 请求url
req = urllib2.Request(target_url) 
# 声明一个CookieJar对象实例来保存cookie 
cj = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
# 通过handler来构建opener
res = opener.open(req)
# 通过正则匹配抓到需要统计的字符串  
content = res.read()
check_text = re.findall(r'<hr />(.*)<hr />',content,re.S)[0]  
  
# 统计  
char_count = [0,0,0,0,0]  
for txt in check_text:  
        if txt == 'w':  
            char_count[0] += 1  
        elif txt == 'o':  
            char_count[1] += 1  
        elif txt == 'l':  
            char_count[2] += 1  
        elif txt == 'd':  
            char_count[3] += 1  
        elif txt == 'y':  
            char_count[4] += 1  
  
# 将数字转换成字符串   
result = ''
for nIndex in char_count:  
    result += str(nIndex)  
print "result = %s" %(result)  
  
# 提交  
value = {'anwser': result}
# 把key-value 的键值对转换成anwser=result
data = urllib.urlencode(value)
# 请求url
request = urllib2.Request(target_url,data)  
# 此处的Oepn方法同urllib2的urlopen方法，也可以传入request
response = opener.open(request)
# response对象有一个read方法，可以返回获取到的网页内容
html = response.read()  
complete = re.findall(r'<body>(.*?)<hr />',html,re.S)[0]
print complete

