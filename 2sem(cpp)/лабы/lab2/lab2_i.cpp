#include <iostream>
#include <string>

int calc(std::string s) {
	int a=0;
	// на коленке
	if (s[1] == s[2]) a += 1;
	if (s[1] == s[3]) a += 1;
	if (s[2] == s[3]) a += 1;

	//a < 2 ? return 100 : a == 2 ? return 500 : return 1000;
	if (a == 0) return 100;
	if (a == 1) return 500;
	return 1000;
}


int main() {

	int a, sum = 0;
	std::string s;

	while (s != "A999AA") {
		std::cin >> a >> s;
		if (a <= 60) continue;
		if (s == "A999AA") break;
		sum += calc(s);
	}

	std::cout << sum;

	return 0;
}