#include "utils.h"

string join(string joining, vector<string> vec_to_join);

vector<int> load_data(string data_type)
{   
    map <string, string> data_type_to_f_name = {
        {"small", "100_numbers"},
        {"medium", "10000_numbers"},
        {"large", "50000_numbers"},
        {"almost_sorted", "almost_sorted"},
        {"same_values", "same_values"},
        {"same_almost_sorted", "same_almost_sorted"}
    };

    if (data_type_to_f_name.find(data_type) == data_type_to_f_name.end())
    {
        vector<string> avail_data_types;
        for (auto const& imap: data_type_to_f_name)
        {
            avail_data_types.push_back(imap.first);
        }
        throw std::invalid_argument("Only choises {" + join(", ", avail_data_types) + "} are available.");
    }

    string f_name = data_type_to_f_name[data_type];

    const string tmp = "data/" + f_name;
    const char *filename = tmp.c_str();
    std::ifstream myfile;
    myfile.open(filename);

    vector<int> arr;

    int number;
    while (myfile >> number)
    {
        arr.push_back(number);
    }

    myfile.close();
    return arr;
}

string join(string joining, vector<string> vec_to_join)
{
    string joined_vector;
    for (int i = 0; i < vec_to_join.size() - 1; i++)
    {
        joined_vector += vec_to_join[i] + joining;
    }
    joined_vector += vec_to_join[vec_to_join.size() - 1];
    return joined_vector;
}
