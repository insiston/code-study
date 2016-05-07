#coding:utf-8

#-----------------------------------
#   程序：getverify.py
#   作者：vforbox
#   语言：python 2.7
#   操作：直接运行
#   功能：验证码识别处理
#------------------------------------

# 验证码识别，此程序只能识别数据验证码
import os
from pytesser import *  

#变更工程路径
os.chdir('D:\Python27\Lib\site-packages\pytesser')

#二值化(阈值为什么是140呢？试出来的)
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)    

#由于都是数字    
#对于识别成字母的 采用该表进行修正    
rep={'O':'0',    
    'I':'1',
    'L':'1',
    'Z':'2',    
    'S':'8'    
    };    

def getverify(name):          
    #打开图片
    im = Image.open(name)    
    #转化到灰度图(亮度)
    imgry = im.convert('L')  
    #保存上面转换的图像
    imgry.save('gray_'+name)    
    #二值化，采用阈值分割法，threshold为分割点   
    out = imgry.point(table,'1')
    #保存上面分割的二值化
    out.save('binary_'+name)    
    #识别转化为文本
    text = image_to_string(out)    
    #识别是否正确
    text = text.strip()    
    text = text.upper();      
    for i in rep:    
        text = text.replace(i,rep[i])       
    print text    
    return text

#调用函数   
getverify('1.jpg')  #这里的图片保证在pytesser目录下
