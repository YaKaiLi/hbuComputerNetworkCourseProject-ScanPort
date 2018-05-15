#! /usr/bin/python3.6
from tkinter import *
import time

root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("端口扫描程序")


def test():
    for i in range(1, 5):
        i = i * 1.0
        print(time.time())
        text.insert(i, 'hello--' + str(time.time()) + '\n')
        text.update()
        if i == 4:
            break
        time.sleep(1)
        print(time.time())


def show():
    '''text.delete(1.0, END)
    text.insert(INSERT, "起始IP：" + e1.get())
    text.insert(INSERT, "\n结束IP：" + e2.get())
    text.delete(1.0, END)
    text.insert(INSERT, "\n起始端口号：" + e3.get())
    text.insert(INSERT, "\n结束端口号：" + e4.get())'''
    for i in range(1,100):
        text.delete(1.0, END)
        text.insert(INSERT, "\n" + str(i)+"%")
        text.update()
        #root.update_idletasks()

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


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

hi_there = Button(frame, text=" 开始扫描 ", font=("宋体", 15), width=10, command=show).grid(row=4, column=0, padx=15, pady=20)
hi_there = Button(frame, text=" 退出 ", font=("宋体", 15), width=10, command=root.quit).grid(row=4, column=1, padx=15, pady=20)
b2 = Button(frame, width=10, command=test).grid(row=6, column=1, padx=15, pady=20)
# self.hi_there.pack()
label = Label(frame, text="进度：", font=("华康少女字体", 15), fg="black").grid(row=5, column=0, padx=15, pady=5)
text = Text(frame, width=15, height=5, font=("华康少女字体", 15))
text.grid(row=5, column=1, padx=35, pady=10, columnspan=1)
root.mainloop()

