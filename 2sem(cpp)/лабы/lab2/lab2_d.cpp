#include <iostream>


int main() {

	int a;
	bool is_pow=true;
	std::cin >> a;
	while (is_pow) {
		if (a == 1) break;
		if (a % 2 == 0) a /= 2;
		else is_pow = false;
	}
	is_pow ? std::cout << "YES" : std::cout << "NO";
	return 0;
}