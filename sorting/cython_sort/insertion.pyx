cpdef int[:] insertion_sort(int[:] data, int data_size):
    cdef int i, j
    for i in range(1, data_size):
        for j in reversed(range(i)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                i -= 1
            else:
                break
    return data

cpdef int[:] insertion_sort_optimized(int[:] data, int data_size):
    cdef int i, j, curr_number
    for i in range(1, data_size):
        curr_number = data[i]
        for j in reversed(range(1, i + 1)):
            if data[j - 1] > curr_number:
                data[j] = data[j - 1]
            else:
                break
            data[j - 1] = curr_number
    return data
