#coding:utf-8
'''
zip压缩暴力破解

'''

import zipfile
import time

#压缩文件的路径
path = raw_input("请输入压缩文件的路径: ")
#破解成功,解压路径
save = raw_input("请输入解压路径：")
#定义破解zip函数
def pojie_zip(path,password):
    if path[-4:]=='.zip':
        #path = dir+'\\'+file
        #print path
        zip = zipfile.ZipFile(path,"r",zipfile.zlib.DEFLATED)
        #print zip.namelist()
        try:
            '''
            如果解压成功，则返回True和密码
            '''
            zip.extractall(path=save,members=zip.namelist(),pwd=password)
            print '\n\033[1;31m-------> success,The password is: \033[1;33m%s\033[0m' %password
            zip.close()
            return True
        except:
            pass   #如果发生异常，不报错
        print 'error'
        print '----------------------------------\n'

#定义密码字典函数
def get_pass():
    #密码字典的路径
    passPath= raw_input("请输入密码文件的路径: ")
    passFile=open(passPath,'r')
    for line in passFile.readlines():
        password = line.strip('\n')
        print 'Try the password %s' %password
        if pojie_zip(path,password):
            break
    passFile.close()

if __name__=='__main__':
    start=time.clock()
    get_pass()
    print "done\n(%.2f seconds)" %(time.clock() - start)
