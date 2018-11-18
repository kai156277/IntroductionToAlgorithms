#include <stdio.h>
#include <vector>
#include <algorithm>
#include "../tools.h"

using namespace std;

// 使用异或运算符计算当前位的符合
// 通过进位和a,b的值计算进位的初值
// 使用倒序可以从0开始计算, 为了描述方便
vector<int> binarySum(vector<int> a, vector<int> b)
{
    // 产生倒序数列
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    // 初始化结果数列
    vector<int> c(a.size() + 1, 0);

    for(int i = 0; i < a.size(); ++i)
    {
        if((a[i] + b[i] + c[i]) > 1)
            c[i+1] = 1;
        c[i] = c[i] ^ a[i] ^ b[i];
    }

    // 倒序输出
    reverse(c.begin(), c.end());
    return c;
}

int main()
{
    vector<int> a = {1, 0, 1, 1, 0, 1, 0, 1, 1, 1};
    vector<int> b = {0, 1, 1, 1, 0, 0, 1, 1, 0, 1};
    vector<int> c = binarySum(a, b); //100 1010 0100
    printIntVector(c);
    return 0;
}
