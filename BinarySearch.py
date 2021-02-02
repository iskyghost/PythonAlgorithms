data = [2,3,4,6,8,10,12,15,16,17,20,23,25,29,31]
target = 25

#linear Search
def Linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


#Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


#recursive binary search
def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return recursive_binary_search(data, target, low, mid-1)
        else:
            return recursive_binary_search(data, target, mid+1, high)



if __name__ == '__main__':
    # print(9 / 3) 浮点除法
    # print(9 // 3) 整数除法
    binary_search_iterative(data, target)