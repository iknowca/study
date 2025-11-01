#include <iostream>
using namespace std;

int main() {
    char char_value = 'A';
    int int_vlaue = 123;
    double double_value = 123.456;

    char *char_pointer_value = &char_value;
    int *int_pointer_value = &int_vlaue;
    double *double_pointer_value = &double_value;

    cout << char_value << endl;
    cout << int_vlaue << endl;
    cout << double_value << endl;

    cout << *char_pointer_value << endl;
    cout << *int_pointer_value << endl;
    cout << *double_pointer_value << endl;

    *char_pointer_value = 'B';
    *int_pointer_value = 234;
    *double_pointer_value = 234.567;

    cout << char_value << endl;
    cout << int_vlaue << endl;
    cout << double_value << endl;

    return 0;
}