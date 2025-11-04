#include <iostream>
using namespace std;

class character {
public:
    character(): hp(100), power(100) {};

protected:
    int hp;
    int power;
};

class player: public character {
public:
    player(){};
};

class monster {
public:
    monster(){};
    void get_damage(int _damage){};
    void attack(player target_paleyr){};
    virtual void attack_special(player target_player);
};

void monster::attack_special(player target_player) {
    cout << "default attack: damage - 10 hp" << endl;
}

class monster_a: public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_a::attack_special(player target_player) {
    cout << "intangle attack: damage - 15hp" << endl;
}

class monster_b: public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_b::attack_special(player target_player) {
    cout << "virtual attack: damage - 0hp" << endl;
}

class monster_c: public monster, character {
public:
    virtual void attack_special(player target_player) override;
};

void monster_c::attack_special(player target_player) {
    cout << "thunder attack: damage - 100 hp" << endl;
}

int main() {
    player player_1;

    monster_a monster_1;

    monster &mon = monster_1;
    monster_a &mon_a = monster_1;

    cout << endl << "parent class attack" << endl;
    mon.attack_special(player_1);

    cout << endl << "child class attack" << endl;
    mon_a.attack_special(player_1);

    cout << endl << "namespace attack" << endl;
    mon_a.monster::attack_special(player_1);

    return 0;
}

