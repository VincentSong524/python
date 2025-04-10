"""入会考验"""
import tkinter as tk
import time


# 创建主窗口
root = tk.Tk()

# 配置标题
root.title("大聪明的时钟")

# 设置窗口大小
root.geometry("400x80+400+400")

# 设置窗口不可调整
root.resizable(width=False, height=False)
# 部件.resizable() 接受两个布尔值参数表示窗口是否可以在水平和垂直方向上调整大小

# 设置时钟标签
label = tk.Label(text="", font=("微软雅黑", 60), fg='blue')
label.pack()

# 更新时间
def update_clock():
    now = time.strftime("%H:%M:%S")             # %H 二十四小时制的小时 %M 分钟 %S 秒
    label.config(text=now)
    root.after(1000, update_clock)              # 用于在制定时间后调用一个函数
update_clock()

# 名言标签
mingyan = tk.Label(text="一寸光阴一寸金， 寸金难买寸光阴", font=('微软雅黑', 20), fg='black')
#修改窗口尺寸
root.geometry("320x100+400+400")
mingyan.pack()

# 循环执行窗口
root.mainloop()