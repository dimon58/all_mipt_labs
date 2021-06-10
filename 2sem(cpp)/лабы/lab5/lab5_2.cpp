#include <iostream>
#include <cmath>
#include <stack>
#include <string>	
#include <sstream>

using std::cin;
using std::cout;
using std::endl;

bool is_sign(const std::string& s) {
	return s == "+" || s == "-" || s == "*" || s == "/";
}


int find_term(std::stack<std::string> st) {
	return 0;
}

int polish_magic(std::stack<std::string>& st) {
	if (is_sign(st.top())) {
		std::string sign = st.top();
		st.pop();
		int b = polish_magic(st);
		int a = polish_magic(st);
		if (sign == "+") return a + b;
		if (sign == "-") return a - b;
		if (sign == "*") return a * b;
		if (sign == "/") return a / b;
	}
	else {
		int t = std::stoi(st.top());
		st.pop();
		return t;
	}
	return 0;
}


int main() {
	std::stack<std::string> st;
	std::string temp;
	std::getline(cin, temp);
	std::stringstream ss;
	ss.str(temp);
	
	while (!ss.eof()) {
		ss >> temp;
		st.push(temp);
	}
	cout << polish_magic(st);
	return 0;
}
