#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

template< typename T>
void print_vector(vector<T> vec) {
	for (auto elem : vec) cout << elem << endl;
}

template< typename T>
double mid(vector<T> vec) {
	if (vec.size() == 0) return 0;
	double s = 0;
	for (T elem : vec) s += elem;
	return round(1000 * s / vec.size()) / 1000;
}


template< typename T>
double disp(vector<T> vec) {
	if (vec.size() == 0) return 0;
	double a = 0, b = 0;
	for (T elem : vec) a += elem * elem;
	for (T elem : vec) b += elem;

	double res = (a - b * b / vec.size()) / vec.size();

	return round(1000 * res) / 1000;;
}


int main() {
	double temp;
	vector<double> seq;

	for (;;) {
		cin >> temp;
		if (temp == 0) break;
		seq.push_back(temp);
	}

	cout << fixed << setprecision(3) << mid(seq) << " " << disp(seq);

	return 0;
}