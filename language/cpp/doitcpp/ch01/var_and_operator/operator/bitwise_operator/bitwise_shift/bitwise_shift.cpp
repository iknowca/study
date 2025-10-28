#include <iostream>
#include <bitset>

using namespace std;

int main() {
    int a = 13;
    int b = a >> 1;
    int c = a << 1;
    int d = a >> -1;
    int e = a << 32;

    cout << "a = " << bitset<8>(a) << ": " << a << endl;
    cout << "b = " << bitset<8>(b) << ": " << b << endl;
    cout << "c = " << bitset<8>(c) << ": " << c << endl;
    cout << "d = " << bitset<8>(d) << ": " << d << endl;
    cout << "e = " << bitset<8>(e) << ": " << e << endl;
}