step = 0
answer = 2388
for i in range(2400):
    step += 1
    if i > answer:
        print("大了")
    elif i < answer:
        print("小了")
    else:
        break
print(f"一共用了{step}步")