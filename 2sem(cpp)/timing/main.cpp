#include<vector>
#include<chrono>
#include<random>
#include<iostream>
#include<algorithm>
#include<cassert>
#include<fstream>
#include<string>

using namespace std;
using namespace std::chrono;

const int max_value = 100000;

enum benchmark_type {
    best = 0,
    average = 1,
    worst = 2
};


template<typename T>
T sum(T best, T benchmark) {
    return best + benchmark;
}

void bubble_sort(vector<int> &v) {
    for (int i = 0; i < v.size() - 1; i++)
        for (int j = 0; j < v.size() - i - 1; j++)
            if (v[j] > v[j + 1])
                swap(v[j], v[j + 1]);
}

void merge_sort(vector<int> &v) {
    if (1 < v.size()) {
        vector<int> array1(v.begin(), v.begin() + v.size() / 2);
        merge_sort(array1);
        vector<int> array2(v.begin() + v.size() / 2, v.end());
        merge_sort(array2);
        merge(array1.begin(), array1.end(), array2.begin(), array2.end(), v.begin());
    }
}

void heap_sort(vector<int> &v) {
    make_heap(v.begin(), v.end());
    for (auto i = v.end(); i != v.begin(); --i) {
        pop_heap(v.begin(), i);
    }
}

void std_sort(vector<int> &v) {
    sort(v.begin(), v.end());
}


vector<int> generate_random_vector(uint64_t n) {

    vector<int> ret(n);

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, max_value);

    for (int i = 0; i < n; ++i) {
        ret[i] = dist(gen);
    }

    return ret;
}


template<typename SortFunction>
uint64_t benchmark(SortFunction f, uint64_t n, benchmark_type type) {

    vector<int> v = generate_random_vector(n);

    switch (type) {
        case benchmark_type::best:
            f(v);
            break;
        case benchmark_type::average:
            break;
        case benchmark_type::worst:
            sort(v.begin(), v.end(), greater<>());
            break;
    }

    auto start = steady_clock::now();
    f(v);
    auto finish = steady_clock::now();


    //возвращаем время работы в мс
    return duration_cast<nanoseconds>(finish - start).count();
}

template<typename SortFunction>
void fileoutput(const string &name, SortFunction f, int max_number, int points, int iterations) {
    int step = static_cast<int>(max(max_number / (points * 1.0), 1.0));

    ofstream fout;
    string path = R"(C:\Users\Dmitry\CLionProjects\timing\)" + name + "_sort.csv";
    fout.open(path, ios_base::out);

    fout << "number";
    fout << ",time_" << name << "\n";

    for (int i = step; i <= max_number; i += step) {
        fout << i;
        uint64_t best = 0, average = 0, worst = 0;
        cout << name << " " << i << " ";

        // Лучший случай
        for (int j = 1; j <= iterations; j++) best += benchmark(f, i, benchmark_type::best);
        best /= iterations;

        // Средний случай
        for (int j = 1; j <= iterations; j++) average += benchmark(f, i, benchmark_type::average);
        average /= iterations;

        // Худший случай
        for (int j = 1; j <= iterations; j++) worst += benchmark(f, i, benchmark_type::worst);
        worst /= iterations;

        fout << "," << best<< "," << average<< "," << worst<< "\n";
        cout << best << " " << average << " " << worst << endl;
    }

    fout.close();
}


int main() {
    int a = 100, points = 20, iterations = 10000;

    fileoutput("bubble", bubble_sort, a, points, iterations);
    fileoutput("heap", heap_sort, a, points, iterations);
    fileoutput("merge", merge_sort, a, points, iterations);
    fileoutput("quick", std_sort, a, points, iterations);
    return 0;
}