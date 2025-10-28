#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 2, c = 8;

    int result_1 = a + b * c;
    cout << "Result 1: " << result_1 << endl;

    int result_2 = (a + b) * c;
    cout << "Result 2: " << result_2 << endl;

    a += b * c;
    cout << "Result 3: " << a << endl;

    bool condition = true;
    int result_4 = (condition && a > b) ? a : b;
    cout << "Result 4: " << result_4 << endl;
}