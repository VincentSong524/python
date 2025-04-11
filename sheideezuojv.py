import tkinter as tk
import threading
import time
import random

def tanchuang():
    # 创建主窗口对象，并起名为root
    root = tk.Tk()
    # 窗口标题
    root.title("恶作剧")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = random.randint(0, width)
    y = random.randint(0, height)
    # 设置窗口大小
    root.geometry(f'400x100+{x}+{y}')
    # 设置标签
    tk.Label(root,
            text='抓不到我吧',
            bg='yellow',
            font=('楷体', 17),
            width=40, height=4
            ).pack()
    #循环窗口
    root.mainloop()

for _ in range(5):
    t = threading.Thread(target=tanchuang)
    # threading.Thread()用于表示一个线程的执行
    # target=tanchuang 制定了线程开始执行时调用的函数
    # t = 将新创建的Thread对象赋值给变量t，通过变量t来引用和控制这个线程

    # 暂停 0.1 秒
    time.sleep(0.1)
    # 启动线程
    t.start()