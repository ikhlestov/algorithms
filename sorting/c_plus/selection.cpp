#include "selection.h"
#include <iostream>

void selection_sort(std::vector<int>& arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        int min_index = i;
        for (int j = i + 1; j < arr.size(); j++)
        {
            if (arr[j] < arr[min_index])
            {
                min_index = j;
            }
        }
        if (min_index != i)
        {
            std::swap(arr[min_index], arr[i]);
        }
    }
}
