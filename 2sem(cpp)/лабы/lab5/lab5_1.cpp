#include <iostream>
#include <cmath>
#include <stack>

using std::cin;
using std::cout;
using std::endl;


int main() {
	std::stack<int> st;
	int temp;
	for (;;) {
		cin >> temp;
		if (temp == 0) break;
		else if (temp > 0) st.push(temp);
		else if (st.size() != 0) {
			if (abs(temp) < st.top()) st.top() += temp;
			else st.pop();
		}
	}
	if (st.size()==0) cout << st.size() << " " << -1;
	else cout << st.size() << " " << st.top();
	return 0;
}