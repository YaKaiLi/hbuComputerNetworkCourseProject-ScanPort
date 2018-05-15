# coding: utf-8#
# ! /usr/bin/python3.6
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from tkinter import *
from functools import partial
import time



root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("端口扫描程序")
########################################
totalnumber = 0

#103.79.76.177
def scan_port(remote_server_ip,port):
    global totalnumber
    s = socket.socket(2, 1)
    res = s.connect_ex((remote_server_ip, port))
    if res == 0:
        show(totalnumber)
        totalnumber = totalnumber + 1
    s.close()

def main():
    ports = []
    #remote_server = "103.79.76.177"
    #remote_server_ip = socket.gethostbyname(remote_server)  # 通过域名来获取IP地址
    remote_server = e1.get()
    remote_server_ip = socket.gethostbyname(remote_server)

    socket.setdefaulttimeout(5)

    for i in range(1, 100):
        ports.append(i)
    # Check what time the scan started
    t1 = datetime.now()

    pool = ThreadPool(processes=100)
    zuhe = partial(scan_port, remote_server_ip)
    results = pool.map(zuhe, ports)
    pool.close()
    pool.join()

    print('time is', datetime.now() - t1)
    print('number is', totalnumber)
#########################################

def show(baifenbi):
    '''text.delete(1.0, END)
    text.insert(INSERT, "起始IP：" + e1.get())
    text.insert(INSERT, "\n结束IP：" + e2.get())
    text.delete(1.0, END)
    text.insert(INSERT, "\n起始端口号：" + e3.get())
    text.insert(INSERT, "\n结束端口号：" + e4.get())'''

    text.delete(1.0, END)
    text.insert(INSERT, "\n" + str(baifenbi))
    text.update()

    #text.insert(INSERT, "\n开放数：" + str(opennumber))
    '''
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    '''


frame = Frame(root)
frame.pack(padx=100, pady=60)  # set area
label = Label(frame, text="起始IP：", font=("华康少女字体", 15), fg="black").grid(row=0, column=0, padx=15, pady=5)
label = Label(frame, text="结束IP：", font=("华康少女字体", 15), fg="black").grid(row=1, column=0, padx=15, pady=5)
label = Label(frame, text="起始端口：", font=("华康少女字体", 15), fg="black").grid(row=2, column=0, padx=15, pady=5)
label = Label(frame, text="结束端口：", font=("华康少女字体", 15), fg="black").grid(row=3, column=0, padx=15, pady=5)

e1 = Entry(frame, font=('Helvetica', '12'))
e2 = Entry(frame, font=('Helvetica', '12'))
e3 = Entry(frame, font=('Helvetica', '12'))
e4 = Entry(frame, font=('Helvetica', '12'))
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

hi_there = Button(frame, text=" 开始扫描 ", font=("宋体", 15), width=10, command=main).grid(row=4, column=0, padx=15, pady=20)
hi_there = Button(frame, text=" 退出 ", font=("宋体", 15), width=10, command=root.quit).grid(row=4, column=1, padx=15, pady=20)

# self.hi_there.pack()
label = Label(frame, text="进度：", font=("华康少女字体", 15), fg="black").grid(row=5, column=0, padx=15, pady=5)
text = Text(frame, width=15, height=5, font=("华康少女字体", 15))
text.grid(row=5, column=1, padx=35, pady=10, columnspan=1)
root.mainloop()
