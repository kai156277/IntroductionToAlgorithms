#include <stdint.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include "../tools.h"

using namespace std;
// array
void merge(vector<int>& array, int pindex, int qindex, int end)
{
    int plen = qindex - pindex + 1;
    int qlen = end - qindex;

    vector<int> pArray;
    vector<int> qArray;

    for(int i = 0; i < plen; ++i)
        pArray.push_back(array[pindex + i]);

    pArray.push_back(INT_MAX);

    for(int i = 0; i < qlen; ++i)
        qArray.push_back(array[qindex + i + 1]);

    qArray.push_back(INT_MAX);

    int i = 0, j = 0;
    for (; pindex <= end; ++pindex) {
        if(pArray[i] < qArray[j])
        {
            array[pindex] = pArray[i];
            ++i;
        }
        else
        {
            array[pindex] = qArray[j];
            ++j;
        }
    }
}

void mergeSort(vector<int>& array, int pindex, int end)
{
    if(pindex < end)
    {
        int qindex = (pindex + end) / 2;
        mergeSort(array, pindex, qindex);
        mergeSort(array, qindex + 1, end);
        merge(array, pindex, qindex, end);
        printf("p: %d, q:%d, e:%d\n", pindex, qindex, end);
        printIntVector(array);
    }
}

int main(int argc, char *argv[])
{
    vector<int> array = {3, 41, 52, 26, 38, 57, 9, 49};
    mergeSort(array, 0, array.size() - 1);
    return 0;
}
