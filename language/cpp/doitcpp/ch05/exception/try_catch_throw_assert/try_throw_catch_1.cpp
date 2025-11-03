#include <iostream>
using namespace std;

int main() {
    try {
        int input;
        cout << "Enter a number: ";
        cin >> input;

        if (input < 0) {
            cout << "throw 1" << endl;
            throw 1;
            cout << "after throw 1" << endl;
        }

        if (input > 0) {
            cout << "thow -1.0f" << endl;
            throw -1.0f;
            cout << "after throw -1.0f" << endl;
        }

        if (input == 0) {
            cout << "throw Z" << endl;
            throw 'Z';
            cout << "after throw Z" << endl;
        }
    } catch (int e) {
        cout << "catch int" << e << endl;
    } catch (float e) {
        cout << "catch float" << e << endl;
    } catch (char e) {
        cout << "catch char" << e << endl;
    }
}