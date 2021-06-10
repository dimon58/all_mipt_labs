#include <iostream>


int main() {

	int a, b;

	std::cin >> a >> b;

	while (a > 0 && b > 0) {
		a %= b;
		if (a > 0)	b %= a;
	}


	std::cout << a + b;

	return 0;
}