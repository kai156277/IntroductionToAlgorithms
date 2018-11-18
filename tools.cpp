#include <stdio.h>

#include "tools.h"

void printIntArray(int *array, int len)
{
    printf_s("Array(%d): ", len);
    for(int i = 0; i < len; ++i)
        printf_s("%d ", array[i]);
    
    printf_s("\n");
}
void printIntVector(const std::vector<int> &array)
{
    printf_s("Array(%zd): ", array.size());
    for(int i = 0; i < array.size(); ++i)
        printf_s("%d ", array[i]);

    printf_s("\n");
}
