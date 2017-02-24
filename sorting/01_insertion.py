from utils import load_data, check_correctness, measure_time_cons


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


if __name__ == '__main__':
    data_type = 'medium'

    print("Insertion sort, data type %s:" % data_type)
    print("-" * 10, "\n", "for loop:")
    data_to_sort = load_data(data_type)
    measure_time_cons(insertion_sort, 3, data_to_sort)
    data_to_sort = load_data(data_type)
    sorted_data = insertion_sort(data_to_sort)
    check_correctness(sorted_data)

    print("-" * 10, "\n", "while loop:")
    data_to_sort = load_data(data_type)
    measure_time_cons(insertion_sort_while_loop, 3, data_to_sort)
    data_to_sort = load_data(data_type)
    sorted_data = insertion_sort_while_loop(data_to_sort)
    check_correctness(sorted_data)

    print("-" * 10, "\n", "for loop optimized:")
    data_to_sort = load_data(data_type)
    measure_time_cons(insertion_sort_optimized, 3, data_to_sort)
    data_to_sort = load_data(data_type)
    sorted_data = insertion_sort_optimized(data_to_sort)
    check_correctness(sorted_data)

    print("-" * 10, "\n", "while loop optimized:")
    data_to_sort = load_data(data_type)
    measure_time_cons(insertion_sort_optimized_while_loop, 3, data_to_sort)
    data_to_sort = load_data(data_type)
    sorted_data = insertion_sort_optimized_while_loop(data_to_sort)
    check_correctness(sorted_data)
