#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    // nomer 1
    cout << "Hello, World!" << std::endl;

    // nomer 2
    double a, b, c;
    //cin >> a >> b;
    a = 3;
    b = 4;
    cout << sqrt(a * a + b * b);

    // nomer 3
    int n;
    //cin >> n;
    n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << '*';
        }
        cout << endl;
    }

    cout << endl << endl;
            
    // nomer 4
    //cin >> n;
    n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << '*';
        }
        cout << endl;
    }

    cout << endl << endl;
    // nomer 5
    //cin >> n;
    n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-i; j++) {
            cout << '*';
        }
        cout << endl;
    }

    cout << endl << endl;
    // nomer 6
    //cin >> n;
    n = 5;
    for (int i = 0; i < n; i+=2) {

        for (int j = 0; j < i/2; j++) {
            cout << ' ';
        }

        for (int k = 0; k < n - i; k++) {
            cout << '*';
        }

        cout << endl;
    }

    cout << endl << endl;

    // fib
    int f1, f2, f3, k, s;
    k = 4e+7;
    f1 = 1;
    f2 = 2;
    s = f2;
    while (f1 + f2 < k) {
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        if (f3 % 2 == 0) s += f3;
    }
    cout << f3;

    return 0;

}