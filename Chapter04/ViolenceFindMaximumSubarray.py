import sys
from random import sample
from FindMaximumSubarray import findMaximumSubarray

def violenceFindMaximumSubarray(array, low, high):

    maxSum = array[:]
    jIndex = [x for x in range(len(array))]
    for i in range(low, high):
        tmp = array[i]
        for j in range(i + 1, high):
            tmp += array[j]
            if maxSum[i] < tmp:
                maxSum[i] = tmp
                jIndex[i] = j

    maxSub = -sys.maxsize
    low = 0
    for i in range(low, high):
        if maxSum[i] > maxSub:
            maxSub = maxSum[i]
            low = i

    return low, jIndex[low] + 1, maxSum[low]

if __name__ == "__main__":
    array = sample([x for x in range(-50, 50)], 11)
    # array = [22, -29, -44, -27, -30, -34, -38, 15, -35, -37, 13]
    print(array)
    print(violenceFindMaximumSubarray(array, 0, len(array)))
    print(findMaximumSubarray(array, 0, len(array)))