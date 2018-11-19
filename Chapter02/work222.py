# -*- coding:utf-8 -*-
import sys

def selectSort(array):
    
    for i in range(0, len(array) - 1):
        min, index = sys.maxsize, 0
        for j in range(i, len(array)):
            if min > array[j]:
                min, index = array[j], j

        array[index], array[i] = array[i], array[index]

if __name__ == "__main__":
    array = [1, 5, 6, 6, 9, 8, 11, 2, 16, 15]
    selectSort(array)
    print(array)