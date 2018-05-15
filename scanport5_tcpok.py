# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

remote_server = "103.79.76.177"
remote_server_ip = socket.gethostbyname(remote_server)  # 通过域名来获取IP地址
totalnumber = 0

#103.79.76.177
def scan_port(port):
    global totalnumber
    s = socket.socket(2, 1)
    res = s.connect_ex((remote_server_ip, port))
    if res == 0:  # 如果端口开启 发送 hello 获取banner
        print ('Port {}: OPEN'.format(port))
        totalnumber = totalnumber + 1
    s.close()

def main():
    ports = []

    print('-' * 60)
    print('scanning remote host ', remote_server_ip)
    print('-' * 60)

    socket.setdefaulttimeout(2)

    for i in range(1, 65535):
        ports.append(i)
    # Check what time the scan started
    t1 = datetime.now()

    pool = ThreadPool(processes=15000)
    results = pool.map(scan_port, ports)
    pool.close()
    pool.join()

    print(' Completed in  ', datetime.now() - t1)
    print('number is  ', totalnumber)
if __name__ == '__main__':
  main()

