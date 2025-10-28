#include <iostream>

using namespace std;

int main() {
    cout << "print ASCII [32 ~ 126]" << endl;

    for (char i = 32; i <= 126; i++) {
        cout << i << ((i%16==15) ? '\n': ' ');
    }

    return 0;
}