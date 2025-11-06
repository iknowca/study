#include <iostream>
using namespace std;

class character {
public:
    character() {
        cout << "character class constructor" << endl;
    }

    ~character() {
        cout << "character class destructor" << endl;
    }
};

class monster {
public:
    monster() {
        cout << "monster class constructor" << endl;
    }
    ~monster() {
        cout << "monster class destructor" << endl;
    }
};

class monster_a: public monster, character {
public:
    monster_a() {
        cout << "monster_a class constructor" << endl;
    }
    ~monster_a() {
        cout << "monster_a class destructor" << endl;
    }
};

int main() {
    monster_a mon_a;
    return 0;
}