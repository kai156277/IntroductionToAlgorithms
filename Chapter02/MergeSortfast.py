# -*- coding:utf-8 -*-
import sys, random
def merge(array, begin, mid, end):
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
            array[i] = b[bIndex]
            bIndex += 1

def mergeSort(array, begin, end):
    if (end - begin) >= 2:
        mid = (begin + end) // 2
        mergeSort(array, begin, mid)
        mergeSort(array, mid, end)
        merge(array, begin, mid, end)
        print(array)

if __name__ == "__main__":
    array = random.sample([x for x in range(100)], 20)
    mergeSort(array, 0, len(array))