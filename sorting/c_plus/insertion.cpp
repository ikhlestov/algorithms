#include "insertion.h"

std::vector<int> insertion_sort(std::vector<int> arr)
{
    for (int i=1; i < arr.size(); i++)
    {
        for (int j=i; j> 0; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                std::swap(arr[j], arr[j - 1]);
            }
            else
                break;
        }
    }
    return arr;
}

std::vector<int> insertion_sort_optimized(std::vector<int> arr)
{
    for (int i=1; i < arr.size(); i ++)
    {
        int tmp = arr[i];
        int j = i;
        for (j; j > 0; j--)
        {
            if (tmp < arr[j - 1])
            {
                arr[j] = arr[j - 1];
            }
            else
                break;
        }
        arr[j] = tmp;
    }
    return arr;
}
