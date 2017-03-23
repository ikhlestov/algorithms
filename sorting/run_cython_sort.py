import argparse
from array import array

from cython_sort.insertion import insertion_sort, insertion_sort_optimized
from run_python_sort import Checker


class CythonChecker(Checker):
    available_algorithms = {
        'insertion': [insertion_sort, insertion_sort_optimized],
    }

    def measure_sorting_time_cons(self, alg_to_check):
        """Measure time consumption method only for sorting algorithms.
        """
        unsorted_arr = array('i', self.unsorted_data)
        arr_size = len(self.unsorted_data)
        mean_time_cons, sorted_arr = self._measure_time_cons(
            alg_to_check, self.repeat_iterations, unsorted_arr, arr_size)
        sorted_list = list(sorted_arr)
        return mean_time_cons, sorted_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--algorithm_name", "-a",
        choices=list(CythonChecker.available_algorithms.keys()),
        required=True)
    parser.add_argument(
        "--data_size", "-d",
        choices=list(CythonChecker.data_size_to_f_name.keys()),
        default="small")
    parser.add_argument(
        "--repeat_iterations", "-r", type=int, default=3)
    args = parser.parse_args()

    checker = CythonChecker(args.data_size, args.repeat_iterations)
    checker.check_algorithm(args.algorithm_name)
