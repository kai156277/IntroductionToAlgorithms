# -*- coding:utf-8 -*-
# 插入排序 （升序）
# input: {a1, a2, a3, a4, ..., an}
# output: {a1 <= a2 <= a3 <= a4 <= ... <= an}

import random

def AscInsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = key

if __name__ == "__main__":
    array = random.sample([x for x in range(100)], 20)
    print("before: ", array)
    AscInsertionSort(array)
    print("end: ", array)
