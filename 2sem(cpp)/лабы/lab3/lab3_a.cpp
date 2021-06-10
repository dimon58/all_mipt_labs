#include <iostream>
#include <vector>

int main() {
	int n, t, s=0;
	std::cin >> n;

	std::vector<int> vec(n);
	for (int i = 0; i < n;i++) {
		std::cin >> t;
		vec.push_back(t);
	}

	t = 0;
	for (auto it = vec.begin(); it < vec.end(); it++) t += *it;
	t /= n;
	for (auto it = vec.begin(); it < vec.end(); it++) if (*it > t) s += *it;
	std::cout << s;
	return 0;
}