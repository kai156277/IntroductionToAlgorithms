
# -*- coding:utf-8 -*-
from random import sample
from BinarySearchIterative import lower_bound

def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        index = lower_bound(array, 0, i, key)
        for j in range(i, index, -1):
            array[j] = array[j - 1]
        array[index] = key
        print(array)

if __name__ == "__main__":
    array = sample([x for x in range(100)], 20)
    InsertionSort(array)