#-*- coding:utf-8 -*-
#2105-03-25
Port = [80,21,23,22,25,110,443,1080,3306,3389,1521,1433]
Server = ['HTTP','FTP','TELNET','SSH','SMTP','POP3','HTTPS','SOCKS','MYSQL','Misrosoft RDP','Oracle','Sql Server']
result = []

import socket 
import sys
import threading
import time


def get_remote_machine_info(Domain):
    try:
        return socket.gethostbyname(Domain)
    except socket.error,e:
        print '%s: %s'%(Domain,e)
        return 0

def scan(Domain,port,server):
    temp = []
    try:
        s = socket.socket()
        print "Attempting to connect to "+Domain+': '+str(port)
        s.connect((Domain,port))
        temp.append(port)
        temp.append(server)
        result.append(temp)
        s.close()
    except:
        pass
        

def output(Domain,IP):
    if result:
        print '\n'+Domain+': --> '+IP
        print '\nThe Open Port:'
        for i in result:
            print Domain+': %4d -->%s'%(i[0],i[1])
    else:
        print 'None Port!'

def main():
    print '''\nX-man Port Scan 2.0
payload:./Scan.py www.xxx.zzz'''
    payload = sys.argv
    IP = get_remote_machine_info(payload[1])
    print '\n'
    for port,server in zip(Port,Server):
        t = threading.Thread(target=scan,args=(payload[1],port,server,)) #for循环创建线程，每个端口开一个线程
        t.setDaemon(True) #将线程声明为守护线程,使其可快速退出
        t.start()
        time.sleep(0.1) #每个线程之间设置时间间隔，避免输出混乱
    output(payload[1],IP)

if __name__=='__main__':
    main()

