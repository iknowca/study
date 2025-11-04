#include <iostream>
#include <string>
using namespace std;

class character {
public:
    character() {
        cout << "character class constructor" << endl;
    }
};

class player: public character {
public:
    player(){};
};

class monster {
public:
    monster() {
        cout << "monster class constructor" << endl;
    }
};

class monster_a: public monster, character {
public:
    monster_a(): monster_a(10, 10) {
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

class monster_b: public monster, character {
public:
    monster_b(player &attack_target)
        :monster_type("일반"),
        location{0, 0},
        unique_id(++total_count),
        target(attack_target) {
        difficult_level = 10;
        quiz = new char[1024];
    };
    ~monster_b() {
        delete[] quiz;
        total_count--;
    }

    monster_b(const monster_b &other);

    void set_quiz(const char *new_quiz) {
        strlcpy(quiz, new_quiz, 1024);
    };
    void set_type(string type) { monster_type = type;};
    void set_difficult_level(int level) {difficult_level = level;};
    void set_location(int x, int y) {location[0] = x; location[1] = y;};
    char *get_quiz() {return quiz;};
    string get_type() { return monster_type;};
    int get_difficult_level() {return difficult_level;};
    int get_x_location() { return location[0];};
    int get_y_location() { return location[1];};
private:
    string monster_type;
    int location[2];
    static int total_count;
    const int unique_id;
    player &target;
    int difficult_level;
    char *quiz;
};

int monster_b::total_count = 0;

int main() {
    player first_player;
    monster_b first_monster(first_player);

    first_monster.set_quiz("at moring 4, at afternoon 2, at night 3");
    first_monster.set_difficult_level(100);
    first_monster.set_type("quiz monster");
    first_monster.set_location(10, 20);

    monster_b second_monster(first_player);
    second_monster.set_quiz("what is the meaning of life?");
    second_monster.set_difficult_level(1);
    second_monster.set_type("quiz monster");
    second_monster.set_location(45, 50);

    cout << "[" << first_monster.get_x_location() << ", " << first_monster.get_y_location() << "]";
    cout << " first monster: " << first_monster.get_type() << " - " << first_monster.get_difficult_level() << endl;
    cout << "quiz: " << first_monster.get_quiz() << endl;

    cout << "[" << second_monster.get_x_location() << ", " << second_monster.get_y_location() << "]";
    cout << " second monster: " << second_monster.get_type() << " - " << second_monster.get_difficult_level() << endl;
    cout << "quiz: " << second_monster.get_quiz() << endl;

    return 0;
}
