#include <iostream>
using namespace std;

class character {
public:
    character() {
        cout << "character class constructor" << endl;
    }
};

int main() {
    character my_character;
    return 0;
}