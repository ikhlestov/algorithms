def insertion_sort(data):
    for i in range(1, len(data)):
        for j in reversed(range(i)):
            if data[i] < data[j]:
                # swap items in an array
                data[i], data[j] = data[j], data[i]
                i -= 1
            else:
                break
    return data


def insertion_sort_while_loop(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
    return data


def insertion_sort_optimized(data):
    """Perform insertion only at the end, previously just
    shift larger elements"""
    for i in range(1, len(data)):
        curr_number = data[i]
        for j in reversed(range(1, i + 1)):
            if data[j - 1] > curr_number:
                data[j] = data[j - 1]
            else:
                break
            data[j - 1] = curr_number
    return data


def insertion_sort_optimized_while_loop(data):
    for i in range(1, len(data)):
        curr_number = data[i]
        j = i
        while j > 0 and data[j - 1] > curr_number:
            data[j] = data[j - 1]
            j -= 1
        data[j] = curr_number
    return data
