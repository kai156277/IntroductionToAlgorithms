#include <stdio.h>

#include "../tools.h"
// Descending order
void insertionSort(int *array, int len)
{
    for(int i = len - 2; i >= 0; --i)
    {
        int key = array[i];
        int j = i + 1;
        while(j < len && array[j] > key)
        {
            array[j - 1] = array[j];
            j++;
        }
        array[j - 1] = key;
        printIntArray(array, len);
    }
}

int main(int argc, char const *argv[])
{
    /* code */
    int test[6] = {31, 41, 59, 26, 41, 58};
    insertionSort(test, 6);
    return 0;
}

