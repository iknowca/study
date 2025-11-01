#include <iostream>
using namespace std;

int average(int _array[], int _count) {
    int sum = 0;
    for (int i = 0; i< _count; i++) {
        sum += _array[i];
    }
    return sum / _count;
}

int main() {
    int score[5] = {100, 90, 80, 70, 60};
    cout << average(score, 5) << endl;
    return 0;
}