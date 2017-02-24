import os
from functools import wraps
from time import time
from copy import deepcopy


def load_data(data_type):
    """
    Args:
        data_type: str, choices from 'small', 'medium', 'large'
    Returns:
        data_to_sort: python list of unsorted int
        data_to_check: python list of sorted int
    """
    data_types = {
        'small': 100,
        'medium': 10000,
        'large': 50000,
    }
    if data_type not in data_types:
        raise NotImplementedError(
            "Available data types are: {}, you've request '{}'.".format(
                list(data_types.keys()), data_type))
    numbers_qtty = data_types[data_type]
    sort_f_name = os.path.join('data', '%d_numbers' % numbers_qtty)

    with open(sort_f_name, 'r') as f:
        data_to_sort = [int(i) for i in f.readlines()]

    return data_to_sort


def check_correctness(sorted_by_algorithm):
    true_sorted = sorted(sorted_by_algorithm)
    assert len(sorted_by_algorithm) == len(true_sorted)
    all_equal = all(i == j for i, j in zip(sorted_by_algorithm, true_sorted))
    if all_equal:
        print("Sorting algorithm work as expected.")
    else:
        print("Algorithm fail to sort data.")
    return all_equal


def timedec(f):
    """Decorator to measure time consumption of the function"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        elapsed = time() - start
        print("Time consumption for {}: {}".format(f.__name__, elapsed))
        return result
    return wrapper


def measure_time_cons(f, repeat, *args):
    """Measure time consumption by repeat times and print mean consumption.
    Args:
        f: function to call
        repeat: int, repeat times
    """
    results = []
    for i in range(repeat):
        copied_args = deepcopy(args)
        start = time()
        f(*copied_args)
        time_consumption = time() - start
        results.append(time_consumption)
    mean_cons = float(sum(results)) / len(results)
    print("Mean time consumption {} for {} iterations.".format(
        mean_cons, repeat))
    return mean_cons
