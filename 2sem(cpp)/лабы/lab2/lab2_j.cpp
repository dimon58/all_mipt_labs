#include <iostream>
#include <string>


int main() {

	int a;
	std::string s = "";

	std::cin >> a;

	while (a > 0) {
		s += std::string(a % 10, 'v');
		s += std::string((a % 60) / 10, '<');
		a /= 60;
		if (a != 0)	s += '.';
	}
	for (auto it = s.rbegin(); it < s.rend();it++) { std::cout << *it; }
	//for (int i = s.size() - 1;i > -1;i--) std::cout << s[i];
	return 0;
}