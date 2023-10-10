numbers = [i for i in range(1, 1000001)]
if (max(numbers) == numbers[-1]) and (min(numbers) == numbers[0]): 
    print(sum(numbers))