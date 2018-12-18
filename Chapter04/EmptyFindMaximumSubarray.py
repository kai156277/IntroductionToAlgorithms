import math
import sys
from random import sample

def findMaxCrossingSubarray(array, low, mid, high):
    leftMax, rightMax = 0, 0
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
            if leftSum == 0:
                return high, high, 0
            else:
                return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            if rightSum == 0:
                return high, high, 0
            else:
                return rightLow, rightHigh, rightSum

        if crossSum == 0:
            return high, high, 0
        else:
            return crossLow, crossHigh, crossSum

if __name__ == "__main__":
    array = sample([x for x in range(-12, 12)], 11)
    # array =[12, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(array)
    print(findMaximumSubarray(array, 0, len(array)))