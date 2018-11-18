#include <stdio.h>

#include "tools.h"

void printIntArray(int *array, int len)
{
    printf_s("Array(%d): ");
    for(int i = 0; i < len; ++i)
        printf_s("%d ", array[i]);
    
    printf_s("\n");
}