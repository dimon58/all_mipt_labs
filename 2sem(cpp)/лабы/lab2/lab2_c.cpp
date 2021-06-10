#include <iostream>


int main() {

	int a, n=0;

	std::cin >> a;

	while (a != 0) {

		if (a % 2 == 0) n += 1;
		std::cin >> a;
	}

	std::cout << n;

}