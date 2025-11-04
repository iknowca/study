#include <iostream>

using namespace std;

class bank {
private:
    int safe;
public:
    bank();
    void use_counter(int _in, int _out);
};

bank::bank() {
    safe = 1000;
    cout << "Bank created" << endl;
    cout << "Safe: " << safe << endl;
    cout << endl;
}

void bank::use_counter(int _in, int _out) {
    safe += _in;
    safe -= _out;

    cout << "income: " << _in << endl;
    cout << "outcome: " << _out << endl;
    cout << "Safe: " << safe << endl;
    cout << endl;
}

int main() {
    bank my_bank;

    my_bank.use_counter(1000, 0);
    // my_bank.safe -= 100;

    return 0;
}