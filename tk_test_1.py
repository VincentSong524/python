import tkinter as tk
root = tk.Tk()
root.title("tk程序")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()


def button_click():
    print("按钮被点击了")

button = tk.Button(root, text="点我", command=button_click)
button.pack()

entry = tk.Entry(root)
entry.pack()


check_var = tk.IntVar()
check = tk.Checkbutton(root, text="同意条款", variable=check_var)
check.pack()


radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="选项1", variable=radio_var, value="1")
radio2 = tk.Radiobutton(root, text="选项2", variable=radio_var, value="2")
radio1.pack()
radio2.pack()


root.mainloop()