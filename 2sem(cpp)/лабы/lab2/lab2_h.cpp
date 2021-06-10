#include <iostream>
#include <cmath>


int first_prime(int num, int start = 2) {
	//возращает минимальный просто делитель
	for (int i = 2; i < sqrt(num);i++)	if (num % i == 0) return i;

	return num;
}


int main() {

	int a, b;
	std::cin >> a;

	if (a == 1) return 0;

	while (a != 1) {
		b = first_prime(a);
		std::cout << b << std::endl;
		a /= b;
	}

	return 0;
}