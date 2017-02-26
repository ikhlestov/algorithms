def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[min_index], data[i] = data[i], data[min_index]
    return data
