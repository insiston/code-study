#!/usr/bin/env python
# coding=utf-8

#-----------------------------------------
#   程序：get_basic_info.py
#   作者：vforbox
#   日期：2016-1-19
#   语言：python 2.7
#   功能：获取系统基本信息
#-----------------------------------------

import os
import getopt
import datetime
import sys
try:
    import psutil
except ImportError:
    os.system('pip install psutil > /dev/null')
    import psutil


def title():

    print u'''
\t\t┏━━━━━━━━━━━━━━━━━━━┓
\t\t┃Python >= 2.7 < 3.0┃
\t\t┃-------------------┃
\t\t┃Get_basic_info v1.0┃  
\t\t┃-------------------┃
\t\t┃       Linux       ┃  
\t\t┗━━━━━━━━━━━━━━━━━━━┛
'''

#分割线
fg = "-"

#获取CPU信息
def get_cup_info():
    global fg
    print "\033[31m%scpu状态信息%s\033[0m" %(fg*30,fg*30)
    print "cpu 逻辑个数：%s个" % psutil.cpu_count()
    print "cpu 物理个数：%s个" % psutil.cpu_count(logical=False)
    print "cpu 用户空间占用百分比：%s" % (psutil.cpu_times_percent(interval=1).user)+"%"
    print "cpu 内核空间占用百分比：%s" % (psutil.cpu_times_percent(interval=1).system)+"%"
    print "cpu 空闲空间剩余百分比：%s" % (psutil.cpu_times_percent(interval=1).idle)+"%"

#获取内存信息
def get_mem_info():
    global fg
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print "\033[31m%s内存状态信息%s\033[0m" %(fg*30,fg*30)
    print "总共内存：%1.fM" % (int(mem.total/1024/1024))
    print "使用内存：%1.fM" % (int(mem.used/1024/1024))
    print "空闲内存：%1.fM" % (int(mem.free/1024/1024))
    print "Swap分区总共：%1.fM" % (int(swap.total/1024/1024))
    print "Swap分区使用：%1.fM" % (int(swap.used/1024/1024))
    print "Swap分区空闲：%1.fM" % (int(swap.free/1024/1024))

#获取磁盘信息
def get_disk_info():
    global fg
    df = psutil.disk_partitions()
    print "\033[31m%s磁盘状态信息%s\033[0m" %(fg*38,fg*38)
    print "设备名称\t\t\t分区总大小\t已使用\t剩余\t挂载\t权限\t分区类型"
    for i in df:
        disk_usage = psutil.disk_usage(i[1])
        print "%-33s%.1fG\t\t%.1fG\t%.1fG\t%s\t%s\t%s" %(i[0],disk_usage[0]/1024/1024/1024,disk_usage[1]/1024/1024/1024,disk_usage[2]/1024/1024/1024,i[1],i[3],i[2])

#获取网络信息
def get_net_info():
    print "\033[31m%s网络状态信息%s\033[0m" %(fg*30,fg*30)
    net = psutil.net_io_counters()
    print "已发送字节数：%1.f Mib" % (int(net[0]/1024/1024))
    print "已接收字节数：%1.f Mib" % (int(net[1]/1024/1024))
    print "已发送数据包个数：%d" % (int(net[2]))
    print "已接收数据包个数：%d" % (int(net[3]))

#获取用户信息
def get_user_info():
    print "\033[31m%s用户信息%s\033[0m" %(fg*30,fg*30)
    user = psutil.users()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    print "系统开机时间：%s" %(boot_time)
    print "用户名\t\t终端\t\t主机\t\t登陆时间"
    for i in range(0,len(user)):
        login_time = datetime.datetime.fromtimestamp(user[i][3]).strftime("%Y-%m-%d %H:%M:%S")
        print "%s\t\t%s\t\t%s\t%s" %(user[i][0],user[i][1],user[i][2],login_time)



def usage():
    title()
    print "使用："
    print " -a\t--all\t\t所有信息"
    print " -c\t--cpu\t\tcpu信息"
    print " -u\t--user\t\t用户登录信息"
    print " -n\t--network\t网络信息"
    print " -d\t--disk\t\t磁盘信息"
    print " -m\t--mem\t\t内存信息\n"

if __name__ == '__main__':
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    
    if not sys.argv[1:]:
        usage()

    try:
        opts,args = getopt.getopt(sys.argv[1:],'humdnca',['help','user','mem','disk','network','cpu','all'])
    except getopt.GetoptError:
        pass
        usage()
        
    try:
        
        for o,a in opts:
            if o in ("-h","--help"):
                usage()
                sys.exit()
            elif o in ("-u","--user"):
                user = a
                get_user_info()
                sys.exit()
            elif o in ("-m","--mem"):
                mem = a
                get_mem_info()
                sys.exit()
            elif o in ("-d","--disk"):
                disk = a
                get_disk_info()
                sys.exit()
            elif o in ("-n","--network"):
                network = a
                get_net_info()
                sys.exit()
            elif o in ("-c","--cpu"):
                cpu = a
                get_cup_info()
                sys.exit()
            elif o in ("-a","--all"):
                all = a
                get_cup_info()
                get_mem_info()
                get_disk_info()
                get_net_info()
                get_user_info()
            else:
                assert False,"unhandled option"
    except:
        pass
