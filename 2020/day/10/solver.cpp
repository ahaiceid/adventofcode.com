#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int solve_part_one(vector<int> const& inputs) {

    int jolts(0);
    uint one_steps(0);
    uint two_steps(0);
    uint three_steps(0);

    for (auto it(inputs.cbegin()); it != inputs.cend(); ++it) {
        if (*it - jolts == 3) {
            ++three_steps;
        } else if (*it - jolts == 1) {
            ++one_steps;
        }
        jolts = *it;
    }
    return three_steps * one_steps;
}

long solve_part_two(vector<int> const& inputs) {
    map<int,int> run_counts{{1,0},{2,0},{3,0},{4,0},{5,0}};
    int run_length = 1;
    for (auto it(inputs.cbegin()+1); it != inputs.cend(); ++it) {
        if (*it - *(it-1)== 3) {
            ++run_counts[run_length];
            run_length = 1;
        } else {
            ++run_length;
        }
    }
    map<int,int> const run_combinations {{1,1},{2,1},{3,2},{4,4},{5,7}};
    long possible_combinations = 1;
    for (auto it(run_counts.cbegin()); it != run_counts.cend(); ++it) {
        possible_combinations *= pow(run_combinations.at(it->first),it->second);
    }
    return possible_combinations;
}

int main() {
    ifstream infile("input");

    int input;
    vector<int> inputs;
    string line;
    while(getline(infile, line)) {
        inputs.push_back(atoi(line.data()));
    }

    inputs.push_back(0);
    std::sort(inputs.begin(), inputs.end());
    inputs.push_back(*(inputs.cend()-1)+3);

    cout << "part 1: " << solve_part_one(inputs) << endl;

    cout << "part 2: " << solve_part_two(inputs) << endl;

    return EXIT_SUCCESS;
}