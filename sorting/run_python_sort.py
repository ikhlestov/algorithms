from __future__ import print_function
from time import time
from copy import deepcopy
import argparse
import os

from py_sort.insertion import insertion_sort, insertion_sort_while_loop, \
    insertion_sort_optimized, insertion_sort_optimized_while_loop
from py_sort.selection import selection_sort
from py_sort.merge import merge_sort
from py_sort.heap import heap_sort
from py_sort.quick import quick_sort_first_item_pivot, \
    quick_sort_median_item_pivot


class Checker:
    data_size_to_f_name = {
        'small': "100_numbers",
        'medium': "10000_numbers",
        'large': "50000_numbers",
        'almost_sorted': 'almost_sorted',
        'same_values': 'same_values',
        'same_almost_sorted': 'same_almost_sorted'
    }

    available_algorithms = {
        'insertion': [insertion_sort, insertion_sort_while_loop,
                      insertion_sort_optimized,
                      insertion_sort_optimized_while_loop],
        'selection': [selection_sort],
        'merge': [merge_sort],
        'heap': [heap_sort],
        'quick': [quick_sort_first_item_pivot, quick_sort_median_item_pivot]
        # 'quick': [quick_sort_median_item_pivot]
    }

    def __init__(self, data_size, repeat_iterations):
        self.data_size = data_size
        self.repeat_iterations = repeat_iterations

    def check_algorithm(self, algorithm_name):
        algorithms_to_check = self.available_algorithms[algorithm_name]
        print("Test running time for {} algorithms, '{}' data size, "
              "{} repeated iterations.".format(
                  algorithm_name, self.data_size, self.repeat_iterations))
        for alg_to_check in algorithms_to_check:
            print("\n", alg_to_check.__name__)
            mean_time_cons, sorted_list = self.measure_time_cons(
                alg_to_check, self.repeat_iterations, self.unsorted_data)
            print("Mean time consumption: {}.".format(mean_time_cons))
            self.check_list_was_sorted(sorted_list)

    @property
    def unsorted_data(self):
        if not hasattr(self, '_unsorted_data'):
            self._unsorted_data = self.load_data()
        # make a copy of unsorted data because some algorithms perform
        # sorting in place
        return list(self._unsorted_data)

    @property
    def sorted_data(self):
        if not hasattr(self, '_sorted_data'):
            self._sorted_data = sorted(self.unsorted_data)
        return self._sorted_data

    def load_data(self):
        f_name = self.data_size_to_f_name[self.data_size]
        f_path = os.path.join('data', f_name)
        with open(f_path, 'r') as f:
            data_to_sort = [int(i) for i in f.readlines()]
        return data_to_sort

    @staticmethod
    def measure_time_cons(f, repeat, *args):
        """Measure time consumption by calling function N repeat times.
        Args:
            f: function to call
            repeat: int, repeat times
        Return:
            mean_cons: float, mean time consumption in seconds
            f_result: result of function call
        """
        results = []
        for i in range(repeat):
            copied_args = deepcopy(args)
            start = time()
            f_result = f(*copied_args)
            time_consumption = time() - start
            results.append(time_consumption)
        mean_cons = float(sum(results)) / len(results)
        return mean_cons, f_result

    def check_list_was_sorted(self, sorted_by_algorithm):
        if len(sorted_by_algorithm) != len(self.sorted_data):
            print("Sorting algorithms miss some data.")
            return
        all_equal = all(i == j for i, j in zip(
            sorted_by_algorithm, self.sorted_data))
        if all_equal:
            print("Sorting algorithm work as expected.")
        else:
            print("Algorithm fail to sort data.")
        return all_equal


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--algorithm_name", "-a",
        choices=list(Checker.available_algorithms.keys()),
        required=True)
    parser.add_argument(
        "--data_size", "-d", choices=list(Checker.data_size_to_f_name.keys()),
        default="small")
    parser.add_argument(
        "--repeat_iterations", "-r", type=int, default=3)
    args = parser.parse_args()

    checker = Checker(args.data_size, args.repeat_iterations)
    checker.check_algorithm(args.algorithm_name)
