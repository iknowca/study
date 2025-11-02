#include <iostream>
using namespace std;

int main() {
    int input_number;
    cout << "1~5 Enter the number:";
    cin >> input_number;

    switch (input_number) {
        case 1:
            cout << "One" << endl;
        case 2:
            cout << "Two" << endl;
        case 3:
            cout << "Three" << endl;
        case 4:
            cout << "Four" << endl;
        case 5:
            cout << "Five" << endl;
        default:
            cout << "Invalid number" << endl;
    }
    return 0;
}