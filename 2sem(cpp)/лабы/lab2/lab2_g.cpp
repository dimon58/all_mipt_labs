#include <iostream>
#include <cmath>


int main() {

	int a;
	bool is_prime = true;
	std::cin >> a;
	
	for (int i = 2; i < sqrt(a);i++) {
		if (a % i == 0) {
			is_prime = false;
			break;
		}
	}

	std::cout << is_prime;
}