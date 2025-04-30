import random

print("这里是二进制部落。来我的地盘，说我的话！")
question = random.randint(1, 100)

answer = input(f'十进制数{question}转换为二进制是多少：')

if answer == bin(question):
    print("亲爱的友人，欢迎来到二进制部落。")
else:
    print('你在胡言乱语什么！来人，把他赶出去！')