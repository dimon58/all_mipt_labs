#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int do_some_awesome_work(int* a, int* b) {
    return *a + *b;
}

int main() {
    int a, b;
    cin >> a >> b;
    int* _a = new int(a);
    int* _b = new int(b);
    cout << do_some_awesome_work(_a, _b);
    delete _a;
    delete _b;
    return 0;
}