#include "heap.h"

class MaxHeap{
        void max_heapify_bottom_to_top(int idx);
        void max_heapify_top_to_bottom(int idx);
        int pop_root();
    public:
        vector <int> heap;
        MaxHeap (vector<int>& arr);
        vector<int> sorted();
};

MaxHeap::MaxHeap (vector<int>& arr){
    for (int i = 0; i < arr.size(); i++){
        heap.push_back(arr[i]);
        max_heapify_bottom_to_top(i);
    }
}

void MaxHeap::max_heapify_bottom_to_top(int idx){
    if (idx != 0)
    {
        int root_idx = (idx - 1) / 2;
        if (heap[root_idx] < heap[idx])
        {
            swap(heap[root_idx], heap[idx]);
            max_heapify_bottom_to_top(root_idx);
        }        
    }
}

void MaxHeap::max_heapify_top_to_bottom(int idx){
    int left_idx = 2 * idx + 1;
    int right_idx = 2 * idx + 2;
    int largest = idx;
    if (left_idx < heap.size() and heap[left_idx] > heap[largest])
    {
        largest = left_idx;
    }
    if (right_idx < heap.size() and heap[right_idx] > heap[largest])
    {
        largest = right_idx;
    }
    if (largest != idx)
    {
        swap(heap[largest], heap[idx]);
        max_heapify_top_to_bottom(largest);
    }
}

int MaxHeap::pop_root(){
    int prev_root;
    if (heap.size() == 1)
    {
        prev_root = heap.back();
        heap.pop_back();
    }
    else
    {
        swap(heap[0], heap[heap.size() -1]);
        prev_root = heap.back();
        heap.pop_back();
        max_heapify_top_to_bottom(0);
    }
    return prev_root;
}

vector<int> MaxHeap::sorted(){
    vector<int> result;
    while (!heap.empty())
    {
        result.push_back(pop_root());
    }
    reverse(result.begin(), result.end());
    return result;
}


void heap_sort(vector<int>& arr)
{
    MaxHeap max_heap (arr);
    arr = max_heap.sorted();
}
