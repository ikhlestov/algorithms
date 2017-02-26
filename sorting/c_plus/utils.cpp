#include "utils.h"

std::vector<int> load_data(std::string data_type)
{   
    int numbers_total;

    if (data_type == "small")
        numbers_total = 100;
    else if (data_type == "medium")
        numbers_total = 10000;
    else if (data_type == "large")
        numbers_total = 50000;
    else
        throw std::invalid_argument("Only choises 'small', 'medium', 'large' are available.");

    const std::string tmp = "data/" + std::to_string(numbers_total) + "_numbers";
    const char *filename = tmp.c_str();
    std::ifstream myfile;
    myfile.open(filename);

    std::vector<int> arr;

    int number;
    while (myfile >> number)
    {
        arr.push_back(number);
    }

    myfile.close();
    return arr;
}
