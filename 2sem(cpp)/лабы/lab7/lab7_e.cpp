#include <iostream>
#include <vector>

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

int main() {
	int N;
	cin >> N;

	vector<vector<int>> mas(N, vector<int>(N));

	for (int row = 0;row < N;row++)
		for (int col = 0;col < N;col++)
			cin >> mas[col][N - row - 1];

	print2dvec(mas);

	return 0;
}