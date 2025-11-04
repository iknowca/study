#include <iostream>
using namespace std;

class character {
public:
    character() {
        cout << "character class constructor" << endl;
    }
};

class monster {
public:
    monster() {
        cout << "monster class constructor" << endl;
    }
};

class monster_a: public monster, character {
public:
    monster_a() {
        cout << "monster_a class constructor" << endl;
    }

    monster_a(int x, int y): location{x, y} {
        cout << "monster_a class constructor with parameter" << endl;
    }

    void show_location() {
        cout << "location: " << location[0] << ", " << location[1] << endl;
    }

private:
    int location[2];
};

int main() {
    monster_a mon_a;
    mon_a.show_location();

    monster_a mon_a_2(10, 20);
    mon_a_2.show_location();
    return 0;
}