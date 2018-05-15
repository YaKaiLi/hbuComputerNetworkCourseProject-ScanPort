#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading
from datetime import datetime

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    host = "103.79.76.177"
    setdefaulttimeout(0.5)
    print('Scanning the host:%s......' % (host))
    t1 = datetime.now()
    for p in range(0,65535):
        t = threading.Thread(target=portScanner,args=(host,p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The host:%s scan is complete!' % (host))
    print('[*] A total of %d open port ' % (openNum))
    print('Multiprocess Scanning Completed in  ', datetime.now() - t1)

if __name__ == '__main__':
    main()