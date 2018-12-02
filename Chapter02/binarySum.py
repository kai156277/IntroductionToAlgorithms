# -*- coding:utf-8 -*-

def binarySum(aArray, bArray):
    c = [0]* (len(aArray) + 1)

    for i in range(len(aArray) - 1, -1, -1):
        if((a[i] + b[i] + c[i + 1]) > 1):
            c[i] = 1
        c[i + 1] = c[i + 1] ^ a[i] ^ b[i]

    return c

if __name__ == "__main__":
    a = [1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    b = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
    #100 1010 0100
    c = binarySum(a, b)
    print(c)