def line():
    for i in range(80):
        print('-',end='')
    print()

def binary_search(list, item):
    low, high = 0, len(list) - 1

    while low <= high:
        mid = (low + high) // 2 #计算中间索引
        #mid = int(mid)
        #guess = list[mid]
        if list[mid] == item:
            return mid  #找到目标返回索引
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
    

if __name__ == "__main__":
    line()
    
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, 5))