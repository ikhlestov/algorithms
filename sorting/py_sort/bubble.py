def bubble_sort(data):
    swaps = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swaps += 1
    if swaps > 0:
        return bubble_sort(data)
    else:
        return data
