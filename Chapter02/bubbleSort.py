from random import sample

def bubbleSort(array):
    for i in range(len(array) - 2):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


if __name__ == "__main__":
    array = sample([x for x in range(100)], 20)
    bubbleSort(array)