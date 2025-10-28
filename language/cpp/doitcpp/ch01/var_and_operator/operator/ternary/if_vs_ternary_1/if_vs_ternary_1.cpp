#include <iostream>
using namespace std;

int main() {
    int a = 7;
    int b = 5;
    int result;

    if (a > b)
        result = a;
    else
        result = b;

    cout << "result = " << result << endl;
    return 0;
}