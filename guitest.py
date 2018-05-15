# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
from tkinter import *

totalnumber = 0
jindu = 0
#103.79.76.177
def scan_port(remote_server_ip,port):
    global totalnumber
    global jindu
    s = socket.socket(2, 1)
    res = s.connect_ex((remote_server_ip, port))
    jindu = jindu + 1
    if res == 0:
        print('进度：'+str(100*jindu/65535)+"%")
        totalnumber = totalnumber + 1
        text.insert(INSERT, 'hello--' + '\n')
        text.update()
    s.close()


#text.delete(1.0, END)


def proc():
    ports = []
    remote_server = e1.get()
    remote_server_ip = socket.gethostbyname(remote_server)  # 通过域名来获取IP地址

    socket.setdefaulttimeout(5)

    for i in range(1, 65535):
        ports.append(i)
    # Check what time the scan started
    t1 = datetime.now()
    pool = ThreadPool(processes=15000)
    zuhe = partial(scan_port, remote_server_ip)
    results = pool.map(zuhe, ports)
    pool.close()
    pool.join()


root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("端口扫描程序")
frame = Frame(root)
frame.pack(padx=100, pady=60)  # set area
label = Label(frame, text="IP：", font=("华康少女字体", 15), fg="black").grid(row=0, column=0, padx=15, pady=5)
e1 = Entry(frame, font=('Helvetica', '12'))
e1.grid(row=0, column=1)

# self.hi_there.pack()
label = Label(frame, text="进度：", font=("华康少女字体", 15), fg="black").grid(row=5, column=0, padx=15, pady=5)
text = Text(frame, width=15, height=5, font=("华康少女字体", 15))
text.grid(row=5, column=1, padx=35, pady=10, columnspan=1)

hi_there = Button(frame, text=" 开始扫描 ", font=("宋体", 15), width=10, command=proc).grid(row=4, column=0, padx=15, pady=20)
hi_there = Button(frame, text=" 退出 ", font=("宋体", 15), width=10, command=root.quit).grid(row=4, column=1, padx=15, pady=20)

root.mainloop()


