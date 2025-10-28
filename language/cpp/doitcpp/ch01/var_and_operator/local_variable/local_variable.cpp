#include <iostream>
using namespace std;

void print() {
    int value = 10;
    cout << "print() print value: " << value << endl;
}

int main() {
    int value = 5;
    cout << "main() print value: " << value << endl;

    print();
    cout << "main() print value: " << value << endl;
    return 0;
}