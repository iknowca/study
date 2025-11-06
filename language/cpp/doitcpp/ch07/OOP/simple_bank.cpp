#include <iostream>
using namespace std;

class bank {
private:
    int safe;
    string bank_name;
public:
    bank(string name): bank_name(name) { safe = 0;};
    ~bank() {};
    void use_counter(int _in, int _out);
    void transfer(int safe);
};

void bank::use_counter(int _in, int _out) {
    safe += _in;
    safe -= _out;
    cout << bank_name << endl;
    cout << "income: " << _in << endl;
    cout << "outcome: " << _out << endl;
    cout << "Safe: " << safe << endl;
    cout << endl;
}

void bank::transfer(int safe) {
    this->safe = safe;
    cout << "Safe: " << safe << endl;
}

int main() {
    bank rich_bank("Rich Bank");
    bank poor_bank("Poor Bank");

    rich_bank.use_counter(1000, 0);
    poor_bank.use_counter(0, 500);
    poor_bank.use_counter(0, 1000);

    return 0;
}
