import sys

from .insertion import insertion_sort_optimized

sys.setrecursionlimit(10000)


def partition_first_item(data, start_idx, stop_idx):
    pivot = data[start_idx]
    leftmark = start_idx + 1
    rightmark = stop_idx
    while True:
        while leftmark <= rightmark and data[leftmark] <= pivot:
            leftmark += 1
        while rightmark >= leftmark and data[rightmark] >= pivot:
            rightmark -= 1
        if rightmark < leftmark:
            break
        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]
    # replace pivot value with last lower element
    data[start_idx], data[rightmark] = data[rightmark], data[start_idx]
    return rightmark


def quick_sort_first_item_pivot(data, start_idx=None, stop_idx=None):
    if start_idx is None:
        return quick_sort_first_item_pivot(data, 0, len(data) - 1)
    else:
        if start_idx < stop_idx:
            splitpoint = partition_first_item(data, start_idx, stop_idx)
            quick_sort_first_item_pivot(data, splitpoint + 1, stop_idx)
            quick_sort_first_item_pivot(data, start_idx, splitpoint - 1)
        return data


def partition_median_item(data, start_idx, stop_idx):
    mid_idx = (stop_idx - start_idx) // 2
    values_with_indexes = list(zip(
        [data[start_idx], data[mid_idx], data[stop_idx]],
        [start_idx, mid_idx, stop_idx]))
    values_with_indexes.remove(min(values_with_indexes))
    values_with_indexes.remove(max(values_with_indexes))
    pivot, median_idx = values_with_indexes[0]
    if median_idx != start_idx:
        data[start_idx], data[median_idx] = data[median_idx], data[start_idx]

    leftmark = start_idx + 1
    rightmark = stop_idx
    while True:
        while leftmark <= rightmark and data[leftmark] <= pivot:
            leftmark += 1
        while rightmark >= leftmark and data[rightmark] >= pivot:
            rightmark -= 1
        if rightmark < leftmark:
            break
        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]
    data[start_idx], data[rightmark] = data[rightmark], data[start_idx]
    return rightmark


def quick_sort_median_item_pivot(data, start_idx=None, stop_idx=None):
    if start_idx is None:
        return quick_sort_median_item_pivot(data, 0, len(data) - 1)
    else:
        if start_idx < stop_idx:
            if (stop_idx - start_idx) < 10:
                data[start_idx: stop_idx + 1] = insertion_sort_optimized(
                    data[start_idx:stop_idx + 1])
            else:
                splitpoint = partition_median_item(data, start_idx, stop_idx)
                quick_sort_median_item_pivot(data, splitpoint + 1, stop_idx)
                quick_sort_median_item_pivot(data, start_idx, splitpoint - 1)
        return data
