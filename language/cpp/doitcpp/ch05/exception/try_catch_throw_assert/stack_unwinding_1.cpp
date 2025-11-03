#include <iostream>
using namespace std;

void func_throw() {
    cout << "func_throw" << endl;
    cout << "throw -1" << endl;
    throw -1;
}

int main() {
    try {
        func_throw();
    } catch (int e) {
        cout << "catch int" << e << endl;
    }
}