#include <iostream>
using namespace std;

int main() {
    int input_number;
    cout << "Enter a number in 1~5: ";
    cin >> input_number;

    switch (input_number) {
        case 1:
            cout << "One" << endl;
            break;
        case 2:
            cout << "Two" << endl;
            break;
        case 3:
            cout << "Three" << endl;
            break;
        case 4:
            cout << "Four" << endl;
            break;
        case 5:
            cout << "Five" << endl;
            break;
        default:
            cout << "Invalid number" << endl;
            break;
    }

    return 0;
}