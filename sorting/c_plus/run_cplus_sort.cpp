#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <map>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include "utils.h"
#include "insertion.h"
using namespace std;

typedef vector<int> (*VectorFunctionPointer)(vector<int>);
typedef map<string, VectorFunctionPointer> string_to_function;
typedef map<string, string_to_function> string_to_function_map;

struct time_and_vector
{
    double time_cons;
    vector<int> res_vector;
};

time_and_vector measure_time_consumption(vector<int> (*sorting_algorithm)(vector<int>),
                                         vector<int> arr_to_sort,
                                         int repeat_iterations)
{
    double total_time_cons = 0;
    time_and_vector sort_results;

    for (int i = 0; i < repeat_iterations; i++)
    {
        clock_t begin = clock();
        sort_results.res_vector = (*sorting_algorithm)(arr_to_sort);

        clock_t end = clock();
        total_time_cons += (double(end - begin) / CLOCKS_PER_SEC);
    }
    
    sort_results.time_cons = total_time_cons / repeat_iterations;
    return sort_results;
}

int main(int argc, char *argv[])
{
    // define some parameters
    string_to_function insertion {
        {"insertion_sort", insertion_sort},
        {"insertion_sort_optimized", insertion_sort_optimized}
    };
    string_to_function_map functions_map = {
        {"insertion", insertion}
    };
    vector<string> functions_names_vec;
    string functions_names_string;
    for (auto const& k: functions_map)
    {
        functions_names_vec.push_back(k.first);
        functions_names_string += k.first + ", ";
    }
    string algorithm_name;
    string data_size = "small";
    vector<string> available_data_sizes = {"small", "medium", "large"};
    int repeat_iterations = 3;
    
    // parse an arguments
    string help_message = "Args:\n"
                          "\t--algorithm_name/-a string, available: " + functions_names_string + "\n"
                          "\t--data_size/-d string, choises from {small, medium, large}, default 'small'\n"
                          "\t--repeat_iterations/-r int, default 3\n"
                          "Example usage:\n"
                          "\t./run_cplus_sort -a insertion -d medium -r 5";
    for (int i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "--algorithm_name") == 0 || strcmp(argv[i], "-a") == 0)
        {
            algorithm_name = argv[i + 1];
            i++;
        }
        else if (strcmp(argv[i], "--data_size") == 0 || strcmp(argv[i], "-d") == 0)
        {
            data_size = argv[i + 1];
            i++;
        }
        else if (strcmp(argv[i], "--repeat_iterations") == 0 || strcmp(argv[i], "-r") == 0)
        {
            repeat_iterations = std::atoi(argv[i + 1]);
            i++;
        }
        else if (strcmp(argv[i], "--help") == 0 || strcmp(argv[i], "-h") == 0)
        {
            cout << help_message << endl;
            exit(0);
        }
    }

    // check that we receive required arguments
    if (algorithm_name.empty())
    {
        cout << "You should provide algorithm name." << endl;
        exit(0);
    }
    if (!(find(functions_names_vec.begin(), functions_names_vec.end(), algorithm_name) != functions_names_vec.end()))
    {
        cout << "You should provide correct algorithm name.\n";
        cout << "Available algorithms are: '" << functions_names_string << "'.\n";
        exit(0);
    }
    if (!(find(available_data_sizes.begin(), available_data_sizes.end(), data_size) != available_data_sizes.end()))
    {
        cout << "You should provide correct data size.\n";
        cout << "Avaibalde choises are: [";
        for (string ds: available_data_sizes)
            cout << ds << " ";
        cout << "]" << endl;
        exit(0);
    }

    // print parsed params
    cout << "Test running time for " << algorithm_name << " algorithms, ";
    cout << "'" << data_size << "' data_size, ";
    cout << repeat_iterations << " repeat_iterations" << endl;

    // load data
    auto functions_map_to_check = functions_map[algorithm_name];
    for (auto const& ifunction: functions_map_to_check)
    {   
        vector<int> data_to_sort = load_data(data_size);
        auto f_name = ifunction.first;
        cout << endl << f_name << endl;
        auto f_to_check = ifunction.second;
        
        time_and_vector sort_results = measure_time_consumption(f_to_check, data_to_sort, repeat_iterations);
        sort(data_to_sort.begin(), data_to_sort.end());

        // check that algorithm works as expected
        if (data_to_sort == sort_results.res_vector)
        {
            cout << "Elapsed time: " << sort_results.time_cons << " seconds." << endl;
            cout << "Sorting algorithm work as expected." << endl;
        }
        else
        {
            cout << "Algorithm fail to sort data." << endl;
        }
        
    }
    return 0;
}


