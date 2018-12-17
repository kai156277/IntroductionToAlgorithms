import math
import sys
from random import sample

def findMaxCrossingSubarray(array, low, mid, high):
    leftMax, rightMax = -sys.maxsize, -sys.maxsize
    leftIndex, rightIndex = mid, mid
    leftSum, rightSum = 0, 0

    for i in range(mid - 1, low - 1, -1):
        leftSum += array[i]
        if leftSum >= leftMax:
            leftMax = leftSum
            leftIndex = i

    for i in range(mid, len(array)):
        rightSum += array[i]
        if rightSum >= rightMax:
            rightMax = rightSum
            rightIndex = i

    return leftIndex, rightIndex + 1, leftMax + rightMax

def findMaximumSubarray(array, low, high):
    if (high - low) == 1:
        return (low, high, array[low])
    else:
        mid = (low + high) // 2
        (leftLow, leftHigh, leftSum) = findMaximumSubarray(array, low, mid)
        (rightLow, rightHigh, rightSum) = findMaximumSubarray(array, mid, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(array, low, mid, high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum

        return crossLow, crossHigh, crossSum

if __name__ == "__main__":
    # array = sample([x for x in range(-50, 50)], 11)
    array =[12, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(array)
    print(findMaximumSubarray(array, 0, len(array)))