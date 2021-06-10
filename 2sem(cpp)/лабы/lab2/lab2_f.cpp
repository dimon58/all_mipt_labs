#include <iostream>


int main() {

	int a, max_num=0, max_num_count=1;
	 do {
		 std::cin >> a;
		 if (a == max_num) max_num_count++;
		 else if (a > max_num) {
			 max_num = a;
			 max_num_count = 1;
		 }
	 } while (a != 0);
	 std::cout << max_num_count;
}