#include <iostream>

using namespace std;

int main()
{
    int *pt_int_value = new int;

    *pt_int_value = 100;
    cout << *pt_int_value << endl;

    delete pt_int_value;

    return 0;
}