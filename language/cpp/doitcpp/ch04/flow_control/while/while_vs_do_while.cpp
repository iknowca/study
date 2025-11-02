#include <iostream>
using namespace std;

int main() {
    int i = 0;
    while ( i< 0) {
        cout << "i is less than 0" << endl;
        i++;
    }

    int j = 0;
    do {
        cout << "j is less than 0" << endl;
        j++;
    } while (j < 0);

    return 0;
}