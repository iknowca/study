#include <iostream>
using namespace std;

int main() {
    unsigned int value = 0x00000000;

    value = ~value;
    cout << hex << value << endl;
}