import sys
from random import sample
from FindMaximumSubarray import findMaximumSubarray

class MaximumSubarray(object):
    def __init__(self, lowIndex = 0, highIndex = 1, maxSum = -sys.maxsize):
        self.lowIndex = lowIndex
        self.highIndex = highIndex
        self.maxSum = maxSum

    def __str__(self):
        return "(%d, %d, %d)" % (self.lowIndex, self.highIndex, self.maxSum)


def LinearFindMaximumSubarray(array, low, high):
    current = MaximumSubarray(low, low + 1, low)
    result = MaximumSubarray(low, low + 1, low)
    for i in range(low, high):
        if current.maxSum >= 0:
            current.highIndex = i + 1
            current.maxSum += array[i]
        else:
            current.lowIndex = i
            current.highIndex = i + 1
            current.maxSum = array[i]

        if current.maxSum > result.maxSum:
            result.lowIndex = current.lowIndex
            result.highIndex = current.highIndex
            result.maxSum = current.maxSum

    return result

if __name__ == "__main__":
    array = sample([x for x in range(-50, 50)], 11)
    print(array)
    print(LinearFindMaximumSubarray(array, 0, len(array)))
    print(findMaximumSubarray(array, 0, len(array)))