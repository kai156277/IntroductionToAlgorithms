# -*- coding:utf-8 -*-
import random
def lower_bound(array, first, last, value):
    while(first < last):
        print("first: {0}, last: {1}".format(first, last))
        mid = (first + last) // 2
        if(array[mid] < value):
            first = mid + 1
        else:
            last = mid
    return first

def binarySearch(array, first, last, value):
    first = lower_bound(array, first, last, value)
    if ((first == last)) or ((value != array[first])):
        return None
    else:
        return first

if __name__ == "__main__":
    array = [1, 4, 6, 7, 11, 16, 27, 34, 35, 47]
    print(array)
    for i in range(len(array)):
        index = binarySearch(array, 0, len(array), array[i])
        print("find: {0} at {1}".format(array[i], index))

    index = binarySearch(array, 0, len(array), 100)
    print("find: {0} at {1}".format(100, index))

    index = binarySearch(array, 0, len(array), 5)
    print("find: {0} at {1}".format(5, index))