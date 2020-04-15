def binarySearch (list, item):
    low = 0
    hight = len(list) - 1
    i = 0
    while low <= hight:
        mid = (low + hight)//2
        guess = list[mid]
        if guess == item:
            return i
        if guess > item:
            hight = mid - 1
            i += 1
        else:
            low = mid + 1
            i += 1
    return None


numbers = [i for i in range(1, 501)]
print(binarySearch(numbers, 250))