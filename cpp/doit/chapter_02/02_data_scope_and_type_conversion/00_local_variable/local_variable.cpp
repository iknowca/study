#include <iostream>

using namespace std;

void print()
{
    int value = 10;
    cout << "local variable's value of print function inside: " << value << endl;
}

int main()
{
    int value = 5;
    cout << "local variable's value of main function inside: " << value << endl;
    print();
    cout << "local variable's value of main function inside again: " << value << endl;

    return 0;
}