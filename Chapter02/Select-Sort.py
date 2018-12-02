# -*- coding:utf-8 -*-
import sys
import random

def findMin(array):
    _min, index = sys.maxsize, 0
    for j in range(len(array)):
        if _min > array[j]:
            _min, index = array[j], j

    return _min, index

def selectSort(array):
    for i in range(0, len(array) - 1):
        _min, index = findMin(array[i:])
        array[index + i], array[i] = array[i], array[index + i]

if __name__ == "__main__":
    array = random.sample([x for x in range(100)], 20)
    print("Before Select Sort:",array)
    selectSort(array)
    print("End Select Sort:",array)