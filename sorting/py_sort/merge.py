def merge_lists(l1, l2):
    i = 0
    j = 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1.pop(i))
        else:
            result.append(l2.pop(j))
    # because some list can be fetched not till the end
    result.extend(l1)
    result.extend(l2)
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    split_idx = len(data) // 2
    l1 = merge_sort(data[:split_idx])
    l2 = merge_sort(data[split_idx:])
    sorted_res = merge_lists(l1, l2)
    return sorted_res
