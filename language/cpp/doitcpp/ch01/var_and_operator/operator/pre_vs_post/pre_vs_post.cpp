#include <iostream>
using namespace std;

int main() {
    int a = 0;
    int b = 0;
    int a_prefix;
    int b_postfix;

    a_prefix = ++a;
    b_postfix = b++;
    cout << "a= " << a << ", a_prefix= " << a_prefix<< endl;
    cout << "b = " << b << ", b_postfix=" << b_postfix << endl;
}