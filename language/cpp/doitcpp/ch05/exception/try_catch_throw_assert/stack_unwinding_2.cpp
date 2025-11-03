#include <iostream>
using namespace std;

void func_throw() {
    cout << endl;
    cout << "inner func_throw()" << endl;
    cout << "throw -1" << endl;
    throw -1;
    cout << "after throw -1" << endl;
}

void func_2() {
    cout << endl;
    cout << "func_2() inner" << endl;
    cout << "call func_throw()" << endl;
    func_throw();
    cout << "after func_throw()" << endl;
}

void func_1() {
    cout << endl;
    cout << "func_1() inner" << endl;
    cout << "call func_2()" << endl;
    func_2();
    cout << "after func_2()" << endl;
}

int main() {
    cout << "main() inner" << endl;
    try {
        cout << "call func_1()" << endl;
        func_1();
        cout << "after func_1()" << endl;
    } catch (int e) {
        cout << "catch int" << e << endl;
    }

    return 0;
}