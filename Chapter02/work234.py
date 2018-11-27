# -*- coding:utf-8 -*-
import math

def binarySearch(array, key):
    begin, end = 0, len(array) - 1
    while(begin <= end):
        mid = math.floor((begin + end) / 2)
        print("[array[{0}]:{1}, array[{2}]:{3}, array[{4}]:{5})".format(begin, array[begin],mid, array[mid], end, array[end]))
        if(key == array[begin]):
            return begin
        if(key == array[end]):
            return end

        if(key < array[mid]):
            end = mid - 1
        elif(key > array[mid]):
            begin = mid + 1
        else:
            return mid

def R_binarySearch(array, begin, key, end):
    if(begin > end):
        return None
    if(array[begin] == key):
        return begin
    if(array[end] == key):
        return end

    mid = math.floor((begin + end) / 2)
    print("[array[{0}]:{1}, array[{2}]:{3}, array[{4}]:{5})".format(begin, array[begin],mid, array[mid], end, array[end]))
    if(key < array[mid]):
        end = mid - 1
    elif(key > array[mid]):
        begin = mid + 1
    else:
        return mid
    return R_binarySearch(array, begin, key, end)
    

if __name__ == "__main__":
    array = [1, 12, 15, 24, 25, 31, 37, 38]#, 42, 100]
    # for i in array:
    #     print("----- serch : {0} ------".format(i))
    #     print(R_binarySearch(array, 0, i, len(array) - 1))

    print(R_binarySearch(array, 0, 101, len(array) - 1))