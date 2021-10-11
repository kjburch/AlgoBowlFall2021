#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <sstream>
#include <limits>
#include <set>
#include <algorithm>

using namespace std;

int constrain(int n, int l, int h) {
    if (n < l) {
        return l;
    }
    else if  (n > h) {
        return h;
    }
    else {
        return n;
    }
}

int main_fun(string inputFile, string outputFile) {
    int universal_length = 0;
    int num_subsets = 0;

    ifstream file;
    file.open(inputFile);

        
    file >> universal_length >> num_subsets;
    string advance;
    getline(file, advance);
    vector<int> weights(num_subsets);
    vector<vector<int>> subsets(num_subsets);

    for (int i = 0; i < num_subsets; ++i) {
        string line;
        getline(file, line);
        istringstream ss(line);
        int num;
        while (ss >> num)
        {
            subsets[i].push_back(num);
        }
        getline(file, line);
        istringstream ss2(line);
        ss2 >> weights[i];
    }
    
    for (auto w : weights) {
        cout << w << endl;
    }


        
    int best_weight = numeric_limits<int>::max();
    vector<int> best_sets;
    default_random_engine generator;
    

    int counter = 0;
    while (1) {
        //int k=randint(1, constrain(ub, 1, num_subsets))
        vector<bool> u(universal_length, false);
        set<int> un;
        vector<int> ss;
        int weight = 0;

        while (weight < best_weight && !all_of(u.begin(), u.end(), [](bool b){return b;})) {
            vector<float> rand_weights(num_subsets);
            for (int i = 0; i < num_subsets; ++i) {
                int l = 0;
                for (const int &n : subsets[i]) {
                    if (u[n-1] == false) {
                        ++l;
                    }
                }
                rand_weights[i] = (float) l / (float) weights[i];
            }

            discrete_distribution<int> distribution(rand_weights.begin(), rand_weights.end());

            int s = distribution(generator);
            
            //cout << all_of(u.begin(), u.end(), [](bool b){return b;}) << " ";
            
            ss.push_back(s);
            weight += weights[s];
            for (const int &num : subsets[s]) {
                u[num-1] = true;
                un.insert(num);
            }
        }
        /*
        for (bool b : u) {
            cout << b << " ";
        }
        cout << endl;
        */
        /*
        for (auto x : u) {
            cout << x << " ";
        }
        cout << endl;
        */
        if (weight < best_weight && all_of(u.begin(), u.end(), [](bool b){return b;})) {
            best_weight = weight;
            best_sets = ss;
            cout << best_weight << endl;
            for (int i : best_sets) {
                cout << i << ", ";
            }
            cout << endl;

            counter = 0;
        }
        
    }
            
}
        
    
     
int main() {
    main_fun("InputWithVariations.txt", "rand_output");
}
