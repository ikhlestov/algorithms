#include "merge.h"

std::vector<int> merge_lists(std::vector<int> l1, std::vector<int> l2)
{
    int i = 0;
    int j = 0;
    std::vector<int> result;
    while ((i < l1.size()) && (j < l2.size()))
    {
        if (l1[i] < l2[j])
        {
            result.push_back(l1[i]);
            i++;
        }
        else
        {
            result.push_back(l2[j]);
            j++;
        }
    }
    if (i == l1.size())
    {
        for (j; j < l2.size(); j++)
        {
            result.push_back(l2[j]);
        }
    }
    else
    {
        for (i; i < l1.size(); i++)
        {
            result.push_back(l1[i]);
        }
    }
    return result;
}

std::vector<int> merge_sort(std::vector<int> arr)
{
    if (arr.size() <= 1)
    {
        return arr;
    }   
    int split_idx = arr.size() / 2;
    std::vector<int> l1;
    std::vector<int> l2;
    for (int i = 0; i < split_idx; i++)
    {
        l1.push_back(arr[i]);
    }
    for (int i = split_idx; i < arr.size(); i++)
    {
        l2.push_back(arr[i]);
    }
    
    l1 = merge_sort(l1);
    l2 = merge_sort(l2);
    std::vector<int> merged;
    merged = merge_lists(l1, l2);
    return merged;
}
