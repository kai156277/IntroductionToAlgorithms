import sys
def merge(array, begin, mid, end):
    a = array[begin : mid]
    b = array[mid : end]

    a.append(sys.maxsize)
    b.append(sys.maxsize)

    aIndex = 0
    bIndex = 0
    for i in range(begin, end):
        if a[aIndex] <= b[bIndex]:
            array[i] = a[aIndex]
            aIndex += 1
        else:
            array[i] = b[bIndex]
            bIndex += 1

def mergeSort(array, begin, end):
    if (end - begin) >= 2:
        mid = (begin + end) // 2
        mergeSort(array, begin, mid)
        mergeSort(array, mid, end)
        merge(array, begin, mid, end)
        print(array)

if __name__ == "__main__":
    array = [3, 41, 52, 26, 38, 57, 9, 49, 11, 7]
    mergeSort(array, 0, len(array))