def line():
    """打印横线"""
    for i in range(80):
        print('-',end='')
    print()


def binary_search(list, item):
    """二分查找"""
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


def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")
    

if __name__ == "__main__":
    greet_user('jesse')