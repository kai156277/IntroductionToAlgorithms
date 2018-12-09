# -*- coding:utf-8 -*-
import sys, random
def merge(array, begin, mid, end):
    inversion = 0
    a = array[begin : mid]
    b = array[mid : end]

    aIndex = 0
    bIndex = 0
    for i in range(begin, end):
        if aIndex == len(a):
            array[i: end] = b[bIndex:]
            break

        if bIndex == len(b):
            array[i: end] = a[aIndex:]
            break

        if a[aIndex] <= b[bIndex]:
            array[i] = a[aIndex]
            aIndex += 1
        else:
            inversion += (mid + bIndex - i)
            array[i] = b[bIndex]
            bIndex += 1

    return inversion

def mergeSort(array, begin, end):
    inversion = 0
    if (end - begin) >= 2:
        mid = (begin + end) // 2
        inversion += mergeSort(array, begin, mid)
        inversion += mergeSort(array, mid, end)
        inversion += merge(array, begin, mid, end)
    return inversion

if __name__ == "__main__":
    # array = random.sample([x for x in range(100)], 20)
    array = [3, 41, 52, 26, 38, 57, 9, 49]
    print(array)
    print("inversion: ",mergeSort(array, 0, len(array)))