#include <iostream>


int main() {

	int a, max_num=0;
	 do {
		 std::cin >> a;
		 if (a % 2 == 0 and a > max_num) max_num = a;
	 } while (a != 0);
	 std::cout << max_num;
}