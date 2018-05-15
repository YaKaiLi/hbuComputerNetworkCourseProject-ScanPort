# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import sys

totalnumber = 0
jindu = 0
#103.79.76.177
def scan_port(remote_server_ip,f,port):
    global totalnumber
    global jindu
    s = socket.socket(2, 1)
    res = s.connect_ex((remote_server_ip, port))
    if res == 0:
        #print ('Port {}: OPEN'.format(port))
        print('进度：'+str(100*jindu/65535)+"%")
        f.write("Port "+str(port) + '\n')
        totalnumber = totalnumber + 1
    jindu = jindu + 1
    s.close()

def main():
    ports = []
    remote_server = input("Enter a remote host or ip address to scan:")
    jieshuip = input("jieshu ip:")
    #remote_server = "103.79.76.177"
    remote_server_ip = socket.gethostbyname(remote_server)  # 通过域名来获取IP地址
    f = open('f.txt', 'w')
    print('-' * 60)
    print('the IP : ', remote_server_ip)
    print('-' * 60)

    socket.setdefaulttimeout(5)

    for i in range(0, 65535):
        ports.append(i)
    # Check what time the scan started
    t1 = datetime.now()
    f.write("open port of the IP "+str(remote_server_ip) + '\n')
    pool = ThreadPool(processes=15000)
    zuhe = partial(scan_port, remote_server_ip,f)
    results = pool.map(zuhe, ports)
    pool.close()
    pool.join()
    f.write("totalnumber "+str(totalnumber) + '\n')
    print('time is', datetime.now() - t1)
    print('number is', totalnumber)
if __name__ == '__main__':
    main()