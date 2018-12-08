import random

def lower_bound(array, begin, end, key):
    if(begin == end):
        return begin

    mid = (begin + end) // 2
    if(array[mid] < key):
        begin = mid + 1
    else:
        end = mid
    return lower_bound(array, begin, end, key)

def binarySearch(array, begin, end, key):
    first = lower_bound(array, begin, end, key)
    if ((first == end)) or ((key != array[first])):
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