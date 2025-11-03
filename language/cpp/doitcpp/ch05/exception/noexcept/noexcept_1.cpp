#include <iostream>
using namespace std;

void real_noexcept() noexcept{
    cout << "real_noexcept" << endl;
}

void fake_noexcept() noexcept{
    cout << "fake_noexcept" << endl;
    throw 1;
}

int main() {
    real_noexcept();
    try {
        fake_noexcept();
    } catch (int e) {
        cout << "catch int" << e << endl;
    }

    return 0;
}