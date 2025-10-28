#include <iostream>
using namespace std;

int value = 1;

int main() {
    int value = -1;

    cout <<value << endl;
    cout << ::value << endl;

    return 0;
}