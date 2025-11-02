#include <iostream>
using namespace std;

int main() {
    int input_number;
    cout << "Enter a number: ";
    cin >> input_number;

    if ( input_number > 0) cout << "Positive number" << endl;
    else if ( input_number < 0) cout << "Negative number" << endl;
    else cout << "Zero" << endl;

    return 0;
}