#include <iostream>
#include <vector>
#include <functional>

using namespace std;

template <typename T>
ostream& operator<<(ostream& out, vector<T> vec) {
	for (T elem : vec) out << elem << " ";
	return out;
}

template <typename T>
void print2dvec(vector<vector<T>> vec) {
	for (vector<T> elem : vec) cout << elem << endl;
}

template <typename T>
int sign(T x) {
	if (x > 0) return 1;
	if (x < 0) return -1;
	return 0;
}

double find_root(double f(double), double a, double b, double tol) {
	if (f(a) == 0) return a;
	if (f(b) == 0) return b;
	double dx, x;
	while ((b - a) > tol) {
		dx = (b - a) / 2;
		x  = a + dx;
		if (sign(f(a)) != sign(f(x))) b = x;
		else b = x;
	}
	return x;
}


int main() {


	return 0;
}