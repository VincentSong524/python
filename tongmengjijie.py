"""同盟集结"""
import tkinter as tk

# 检查答案是否正确
def check_answer():     # 定义检查答案的函数
    answer = var.get()  # 将选中的答案返回的值放入 answer 中
    if answer =="HTML": # 如果回答正确，那么对应修改结果标签文本内容
        result_label.config(text="恭喜你接受挑战资格，你敢接受挑战吗？")
    else:               # 如果回答错误，对应修改结果标签文本内容
        result_label.config(text="很遗憾下次再见。")
        # 部件.config()
        # 用于配置和修改tkinter部件的属性

root = tk.Tk()
root.title("同盟集结")
root.geometry("400x200")

#问题
question_label = tk.Label(root, text="以下哪个选项不是编程语言？")
question_label.pack()
# tkinter.Label(master, text, font, fg, bg, width, height)
# master-确定父窗口组件
# text-标签上显示的文本
# font-指定文本的字体字号
# fg-文本颜色
# bg-标签颜色
# width-标签宽度
# height-标签高度

var = tk.StringVar()
# StringVar 对象
# 用于存储字符串值的特殊变量类型
# 与 IntVar 类似， 通常与单选框（Radiobutton）或复选框（Checkbutton）等部件一起使用，用于存储用户的选择

# 单选按钮
option_1 = tk.Radiobutton(root, text="Python", variable=var, value="Python")
option_2 = tk.Radiobutton(root, text="HTML", variable=var, value="HTML")
option_1.pack()
option_2.pack()
# tkinter.Radiobutton(master, text, varibale, value)
# master-确定父窗口组件
# text-设置选项内容
# variable-与 Radiobutton 部件关联的 Tkinter 变量（通常是 IntVar 或 StingVar），用于存储用户选择的值。
# value-设置用户选择该单选按钮时 variable 的值。

# 提交按钮
tijiao_button = tk.Button(root, text="提交答案", command=check_answer)
tijiao_button.pack()
# tkinter.Button(master, text, command)
# master-确定父窗口组件
# text-按钮上显示的文本
# command-按钮被点击时执行的函数或方法

# 结果标签
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()

