#!/usr/bin/python27
# coding=utf-8
# authon: vforbox   <vforbox@gmail.com>
# date: 2016 07

import re
import os
import sys
from collections import defaultdict,OrderedDict

# 字符类型转换
def input_str(s):
    if str.isdigit(s):      # 对输入是否是数字进行判断
        s = int(s)          # 如果输入的数字,则转换为整数类型
    return s                # 返回输入字符


# 名称或变量名输入判断
def name_decide():
    (name,name_flag) = ('',True)    # 初始化返回的名称和判断标志位

    while name_flag:
        name_input = raw_input("\033[32m请输入 新服务名 \033[0m\033[31m[退出输入q]\033[0m: ")
        if len(name_input) == 0:    # 如果输入为空则直接下一次循环
            continue
        elif name_input == 'q' or name_input == 'Q':     # 输入q,退出本次输入
            name_flag = False
        elif re.match('[0-9a-zA-Z\_]+',name_input):      # 匹配输入是否以字符,数字或下划线开头
            name = name_input
            name_flag = False       # 输入成功后退出循环
        else:
            print "\033[31m名称输入错误，请重新输入!\033[0m"
    return name


# IP地址及端口输入判断
def ip_decide():
    (address,address_flag) = ('',True)    # 初始化返回的IP地址和判断标志位

    while address_flag:
        address_input = raw_input("\033[32m请输入 IP \033[0m\033[31m[退出输入q]\033[0m: ")
        if len(address_input) == 0:    # 如果输入为空则直接下一次循环
            continue
        elif address_input == 'q' or address_input == 'Q':     # 输入q,退出本次输入
            address_flag = False

        # 匹配输入是否是ip:port的格式
        elif re.match('(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}(\:\d{1,5})?$',address_input):
            address = address_input
            address_flag = False       # 输入成功后退出循环
        else:
            print "\033[31mIP输入错误，请重新输入!\033[0m"
    return address


# 输入的数字判断
def number_decide(name):
    (number,number_flag) = ('',True)    # 初始化返回的数字和判断标志位

    while number_flag:
        number_inptu = raw_input("\033[32m请输入 %s \033[0m\033[31m[退出输入q]\033[0m: " %name)
        if len(number_inptu) == 0:    # 如果输入为空则直接下一次循环
            continue
        elif number_inptu == 'q' or number_inptu == 'Q':     # 输入q,退出本次输入
            number_flag = False
        else:
            try:
                int(number_inptu)     # 匹配输入是否是数字
            except:
                print "\033[31m%s 输入错误，请重新输入!\033[0m" %name
            else:
                number = number_inptu
                number_flag = False
    return number


# backend 输入判断
def backend_input(input_index,input_dict):
    (input_name,input_flag) = ('',True)    # 初始化返回的名称和判断标志位

    if len(input_index) !=0:    # 如果输入非空,对输入进行判断并转化类型
        input_index = input_str(input_index)
    if input_index == 'b' or input_index == 'B':    #  输入b,退出程序
        input_flag = False
    elif input_index in input_dict.keys():      # 如果输入为数字编号,则从字典中获取具体backend名称
        input_name = input_dict[input_index]
    elif input_index in input_dict.values():    # 如果输入为backend名称,则直接获取
        input_name = input_index
    else:
        input_name = ''         # 输入其他字符,赋值变量为空
    return (input_name,input_flag)              # 返回输入的结果和循环标志位


# backend 列表展示
def backend_read(file):
    backend_list = []       # 初始化backend的列表
    show_dict = {}          # 初始化要返回的显示字典
    backend_name_dict = defaultdict(list)       # 定义一个value为列表的字典,用来存放server

    server_flag = False     # 初始化server判断标志位

    with open(file,'r') as haproxy:              # 打开haproxy配置文件
        for line in haproxy:
            server_dict = OrderedDict()         # 定义一个有序字典
            line = line.strip('\n')

            if re.match('backend',line):        # 匹配配置文件以backend开头的行
                backend_name = re.split('\s+',line)[1]
                backend_list.append(backend_name)   # 将配置到的backend的名称插入到列表
                server_flag = True                  # 赋值标志位为真,用来与server关联

            elif server_flag and re.match('\s+server',line):     # 匹配配置文件以server开头的行
                server_info = re.split('\s+',line)  # 对server进行分隔

                server_dict['name'] = server_info[2]
                server_dict['address'] = server_info[3]
                server_dict['weight'] = server_info[5]
                server_dict['maxconn'] = server_info[7]

                backend_name_dict[backend_name].append(server_dict)     # 将server字典与backend的名称进行关联
            else:
                server_flag = False             # 当server没匹配到,赋值标志位为假，结束关联

    for k,v in enumerate(backend_list,1):
        show_dict[k] = v                        # 对backend名称进行新字典赋值,方便查询和展示
        print "\t┣------------------------------┨"
        print "\t| %d. %s " %(k,v)                   # 输出backend列表
    print "\t┗------------------------------┛"
    return (show_dict,backend_name_dict)        # 返回显示的字典和backend-server字典


# 显示backend后端服务器
def show_backend_server(show_backend_value,show_server_dict):

    # 对backend名称进行遍历并加上数字编号
    print "┏-----------------------------------------------------------------------------┓"
    print "|\t\t\t\033[35m后端服务器 %s 信息 \033[0m" %show_backend_value
    print "┣-----------------------------------------------------------------------------┨"
    print "| %-5s %-20s %-20s %-20s %-20s" %('id','name','address','weight','maxconn')
    print "┣-----------------------------------------------------------------------------┨"
    server_list = show_server_dict[show_backend_value]
    for k,v in enumerate(server_list,1):        # 用enumerate进行server展示
        print "| %-5s" %k + '',
        for kk,vv in v.items():
            print "%-20s" %vv + '',
        print ""
    print "┗-----------------------------------------------------------------------------┛"


# backend后端服务操作并回写配置文件
def backend_server_handle(file,handle_dict):
    newfile = "new_%s.cfg" %file        # 定义回写的新文件
    server_flag = False                 # 初始化server判断标志位

    # 同时打开二文件,一个读,一个写
    with open(file,'r') as read_file,open(newfile,'w') as write_file:
        for line in read_file:
            if re.match('backend',line): # 匹配到backend行时进行server信息插入
                write_file.write(line)

                backend_name = re.split('\s+',line)[1]
                for server_dict in handle_dict[backend_name]:   # 对backend-server字典进行遍历
                    server_line = "\tserver {name} {address} weight {weight} maxconn {maxconn}\n"
                    write_file.write(server_line.format(**server_dict)) # 将指定的backend下的server条目插入文件

                server_flag = True      # 指定标志位为真,方便server判断
            elif server_flag and re.match('\s+server',line):    # 匹配server开头的行,跳过不做任何操作
                pass
            else:
                write_file.write(line)  # 其他的行,直接插入新文件
                server_flag = False

    print "\t\t\033[33m→ server 更新成功 ←\033[0m"
    os.system('mv %s %s.bak' %(file,file))      # 对源配置文件进行备份
    os.system('mv %s %s' %(newfile,file))       # 对新生成的配置文件进行改名


# 主程序开始
if __name__ == '__main__':

    # 运行环境
    if (sys.version[0:3] <= '2.6' or sys.version[0:3] >= '3.0'):
        print "\033[36m\t\t当前代码的运行环境应该是 Python 2.7\033[0m"
        exit(1)

    # 确定是一个Python版本2
    if sys.version_info.major > 2:
        raw_input = input

    (backend_name,flag) = ('',True) # 初始化返回的名称和判断标志位

    haproxy_file = "haproxy.cfg"           # 指定haproxy配置文件
    show_haproxy_name_dict = {}     # 初始化backend显示字典
    show_haproxy_server_dict = {}   # 初始化server显示字典

    while flag:
        # if os.name == 'posix':      # 清屏
        #     os.system('clear')
        # else:
        #     os.system('cls')

        print "     ┏--------------------------------------┓"
        print "\033[35m\t 欢迎访问 haproxy 配置文件管理平台\033[0m\n"
        print "\t┏------------------------------┓"
        print "\t|\t\033[35mbackend 列表信息\033[0m"
        (show_haproxy_name_dict,show_haproxy_server_dict) = backend_read(haproxy_file)

        print '''
        ┏------------------------------┓
        |\t\033[35m    功能菜单\033[0m
        ┠------------------------------┨
        |\t\033[31m 1. 查询后端服务\033[0m
        ┠------------------------------┨
        |\t\033[32m 2. 添加后端服务\033[0m
        ┠------------------------------┨
        |\t\033[33m 3. 修改后端服务\033[0m
        ┠------------------------------┨
        |\t\033[34m 4. 删除后端服务\033[0m
        ┠------------------------------┨
        |\t\033[36m 5. 退出\033[0m
        ┗------------------------------┛'''
        print "\n     ┗--------------------------------------┛"
        select_num = raw_input("\033[33m请选择操作的菜单条目\033[0m：")

        # 查询后端服务
        if select_num == '1':
            query_flag = True       # 初始化查询循环标志

            while query_flag:
                backend_index = raw_input("\033[32;1m请输入查询的 backend 编号或名称\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m：")

                # 对输入的值进行判断
                (backend_name,query_flag) = backend_input(backend_index,show_haproxy_name_dict)
                if backend_name:    # 显示对应backend下的server列表
                    show_backend_server(backend_name,show_haproxy_server_dict)

        # 添加后端服务
        if select_num == '2':
            add_flag = True         # 初始化添加循环标志

            while add_flag:
                backend_index = raw_input("\033[32;1m请输入添加的 backend 的编号或名称\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m: ")

                # 对输入的值进行判断
                (backend_name,add_flag) = backend_input(backend_index,show_haproxy_name_dict)
                if backend_name:    # 显示对应backend下的server列表
                    show_backend_server(backend_name,show_haproxy_server_dict)

                    add_server_dict = OrderedDict()         # 定义一个有序字典
                    print "\t\t\033[34;1m请依次输入后端服务信息\033[0m[\033[36;1mname   address   weight    maxconn\033[0m]"

                    add_server_dict['name'] = name_decide()     # 对输入的name有效性进行判断
                    add_server_dict['address'] = ip_decide()    # 对输入的IP有效性进行判断
                    add_server_dict['weight'] = number_decide("权重值")      # 对输入的权重值有效性进行判断
                    add_server_dict['maxconn'] = number_decide("最大连接数")  # 对输入的最大连接数有效性进行判断

                    print "┏-----------------------------------------------------------------------┓"
                    print "| %-20s %-20s %-20s %-20s" % ('name', 'address', 'weight', 'maxconn')
                    print "┠-----------------------------------------------------------------------┨"
                    print "| %-20s %-20s %-20s %-20s" %(add_server_dict['name'],
                                                        add_server_dict['address'],
                                                        add_server_dict['weight'],
                                                        add_server_dict['maxconn'])
                    print "┗-----------------------------------------------------------------------┛"

                    # 对输入的四个服务信息判断是否成功
                    if add_server_dict['name'] and add_server_dict['address'] and add_server_dict['weight'] and add_server_dict['maxconn']:
                        add_commit = raw_input("确认是否添加此条目[y|n]: ")
                        if add_commit == 'y' or add_commit == 'Y':      # 确认添加服务条目,并回写配置文件
                            show_haproxy_server_dict[backend_name].append(add_server_dict)
                            backend_server_handle(haproxy_file,show_haproxy_server_dict)
                        else:
                            add_flag = False        # 否则退出本次循环
                    else:
                        print "\033[31mserver 输入信息有误,请重新输入!\033[0m"

        # 修改后端服务
        if select_num == '3':
            backend_modify_flag = True         # 初始化修改循环标志

            while backend_modify_flag:
                backend_index = raw_input('\033[32;1m请输入修改的 backend 的编号或名称\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m: ')

                # 对输入的值进行判断
                (backend_name,backend_modify_flag) = backend_input(backend_index,show_haproxy_name_dict)
                if backend_name:       # 显示对应backend下的server列表
                    show_backend_server(backend_name,show_haproxy_server_dict)

                    server_modify_flag = True  # 初始化server条目修改标志位
                    while server_modify_flag:
                        server_index = raw_input('\033[32;1m请输入修改的 server 的编号\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m: ')
                        if len(server_index) != 0:
                            server_index = input_str(server_index)
                        if server_index == 'b' or server_index == 'B':      # 输入b,返回上一层
                            server_modify_flag = False

                        # 指定具体的server编号进行判断
                        elif server_index >= 1 and server_index <= len(show_haproxy_server_dict[backend_name]):
                            modify_server_dict = OrderedDict()         # 定义一个有序字典
                            print "\t\t\033[34;1m请依次输入后端服务信息\033[0m[\033[36;1mname   address   weight    maxconn\033[0m]"

                            modify_server_dict['name'] = name_decide()                # 对输入的name有效性进行判断
                            modify_server_dict['address'] = ip_decide()               # 对输入的IP有效性进行判断
                            modify_server_dict['weight'] = number_decide("权重值")     # 对输入的权重值有效性进行判断
                            modify_server_dict['maxconn'] = number_decide("最大连接数") # 对输入的最大连接数有效性进行判断

                            print "┏-----------------------------------------------------------------------┓"
                            print "| %-20s %-20s %-20s %-20s" % ('name', 'address', 'weight', 'maxconn')
                            print "┠-----------------------------------------------------------------------┨"
                            print "| %-20s %-20s %-20s %-20s" % (modify_server_dict['name'],
                                                                 modify_server_dict['address'],
                                                                 modify_server_dict['weight'],
                                                                 modify_server_dict['maxconn'])
                            print "┗-----------------------------------------------------------------------┛"

                            # 对输入的四个服务信息判断是否成功
                            if modify_server_dict['name'] and modify_server_dict['address'] and modify_server_dict['weight'] and modify_server_dict['maxconn']:
                                modify_commit = raw_input("确认是否添加此条目[y|n]: ")
                                if modify_commit == 'y' or modify_commit == 'Y':      # 确认修改服务条目,并回写配置文件
                                    show_haproxy_server_dict[backend_name][server_index - 1] = modify_server_dict
                                    backend_server_handle(haproxy_file,show_haproxy_server_dict)
                                    modify_server_dict = False
                                else:           # 否则退出本次循环
                                    modify_server_dict = False
                            else:
                                print "\033[31mserver 输入信息有误,请重新输入!\033[0m"
                        else:
                            print "\033[31mserver 编号输入有误,请重新输入!\033[0m"

        # 删除后端服务
        if select_num == '4':
            backend_del_flag = True         # 初始化删除循环标志

            while backend_del_flag:
                backend_index = raw_input('\033[32;1m请输入删除的 server 的编号\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m: ')

                # 对输入的值进行判断
                (backend_name,backend_del_flag) = backend_input(backend_index,show_haproxy_name_dict)

                if backend_name:       # 显示对应backend下的server列表
                    show_backend_server(backend_name,show_haproxy_server_dict)

                    server_del_flag = True
                    while server_del_flag:
                        server_index = raw_input('\033[32;1m请输入删除的 server 的编号\033[0m\033[31;1m[返回上层菜单,请输入b]\033[0m: ')
                        if len(backend_index) != 0:
                            server_index = input_str(server_index)
                        if server_index == 'b' or server_index == 'B':      # 输入b,返回上一层
                            server_del_flag = False

                        # 指定具体的server编号进行判断
                        elif server_index >= 1 and server_index <= len(show_haproxy_server_dict[backend_name]):
                            del_server_dict = OrderedDict()  # 定义一个有序字典

                            server_list_dict = show_haproxy_server_dict[backend_name][server_index - 1]
                            del_server_dict['name'] = server_list_dict.values()[0]
                            del_server_dict['address'] = server_list_dict.values()[1]
                            del_server_dict['weight'] = server_list_dict.values()[2]
                            del_server_dict['maxconn'] = server_list_dict.values()[3]

                            print "┏-----------------------------------------------------------------------┓"
                            print "| %-20s %-20s %-20s %-20s" % ('name', 'address', 'weight', 'maxconn')
                            print "┠-----------------------------------------------------------------------┨"
                            print "| %-20s %-20s %-20s %-20s" % (del_server_dict['name'],
                                                                 del_server_dict['address'],
                                                                 del_server_dict['weight'],
                                                                 del_server_dict['maxconn'])
                            print "┗-----------------------------------------------------------------------┛"

                            del_commit = raw_input("确认是否删除此条目[y|n]: ")
                            if del_commit == 'y' or del_commit == 'Y':      # 确认修改服务条目,并回写配置文件
                                del show_haproxy_server_dict[backend_name][server_index - 1]
                                backend_server_handle(haproxy_file,show_haproxy_server_dict)
                                server_del_flag = False
                            else:           # 否则退出本次循环
                                server_del_flag = False
                        else:
                            print "\033[31mserver 编号输入有误,请重新输入!\033[0m"

        # 退出程序
        if select_num == '5':
            sys.exit("\033[36m\t\t→ 退出程序 ←\033[0m")
