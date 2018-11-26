# -*- coding:utf-8 -*-
import math

def merge(array, pindex, qindex, end):
    pArray = array[pindex : qindex]
    qArray = array[qindex : end]

    i, j = 0, 0
    for index in range(end - pindex):
        if i == len(pArray):
            array[pindex + index: end] = qArray[j:]
            break
        
        if j == len(qArray):
            array[pindex + index: end] = pArray[i:]
            break


        if(pArray[i] < qArray[j]):
            array[pindex + index] = pArray[i]
            i += 1
        else:
            array[pindex + index] = qArray[j]
            j += 1
        

def mergeSort(array, pindex, end):
    if pindex < end - 1:
        qindex = math.floor((pindex + end) / 2)
        mergeSort(array, pindex, qindex)
        mergeSort(array, qindex, end)
        merge(array, pindex, qindex, end)
        print(array)


if __name__ == "__main__":
    array = [3, 10, 2, 6, 49, 11, 19, 15]
    mergeSort(array, 0, len(array))