from random import choice

#记录猜测次数
guess = 0

#设置彩票号码表
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

#中奖号码存储列表
bingo =[]

#随机抽取四个字符为中奖号码
while True:
    bingo.append(choice(nums))
    if len(bingo) == 4:
        break

#展示中奖号码
print(f"The winning number are ")
for i in bingo:
    print(i, end=' ')
print()

#我的答案
my_ticket= []

while True:
    guess += 1
    #存储中奖号码
    while True:
        my_ticket.append(choice(nums))
        if len(my_ticket) == 4:
            break

    #判断是否中奖
    if bingo == my_ticket:
        print(f"You guessed it after only {guess} tries.")
        break
    
    #重置中奖号码
    my_ticket = []