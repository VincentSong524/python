def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass    #静默失败，发现错误以后什么都不做保持程序运行
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#filename = 'alice.txt'
#count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'fake_file.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)