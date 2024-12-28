#include <iostream>
using namespace std;

int main()
{
    cout << "ASCII code [32 ~ 126]:" << endl;
    for (char i=32; i< 126; i++)
    {
        cout << i << ((i%16==15)? "\n" : "\t");
    }

    return 0;
}