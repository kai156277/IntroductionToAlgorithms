# -*- coding:utf-8 -*-

def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = key
        print(array)

if __name__ == "__main__":
    array = [31, 41, 59, 26, 41, 58]
    InsertionSort(array)