#include <iostream>
using namespace std;

void swap(int _a, int _b) {
    int temp = _a;
    _a = _b;
    _b = temp;
}

int main() {
    int a = 1, b = 2;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    swap(a, b);

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    return 0;
}