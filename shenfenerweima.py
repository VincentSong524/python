"""身份二维码"""
import tkinter as t
from MyQR import myqr


# 生成二维码
myqr.run(
    words="https://postimg.cc/8JfN7Ycw",
    version=5,
    level='H',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='身份二维码_小米.gif'
    )
# words-指定要编码为二维码的文本内容，或者链接，不支持中文
# version-可选 指定二维码版本。版本决定了二维码的尺寸和容纳的信息量。默认值为1，范围从1到40. vision1 21x21， vision2 25x25， 每增加一个版本增加4的尺寸。
# level-可选 用于制定二维码的纠错等级。L M Q H
# picture-可选 用于自定义二维码背景图，支持 .jpg .png .bmp .gif, 默认为黑白色
# colorized-可选 二维码背景颜色 False 黑白， True 使用颜色对二维码进行美化
# contart-可选 对比度 1.0原对比度， 数字越大对比度越高（参数必须为float类型）
# brightness-可选 亮度
# save_name-可选 指定生成的二维码图片文件的保存名称。
# save_dir-可选 指定生成的二维码图片文件的保存路径，默认当前目录。 要使用斜杠/不要用反斜杠\