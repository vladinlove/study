import random

def quickSort(array):
    '''Function for quick int list sort'''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

#Testing data
numbers = [i for i in range(1,50)]
random.shuffle(numbers)
print('Before sort: ' , numbers)
print('After sort: ', quickSort(numbers))