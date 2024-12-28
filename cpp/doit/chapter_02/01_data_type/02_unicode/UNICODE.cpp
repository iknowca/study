#include <iostream>
#include <fcntl.h>

using namespace std;

int main()
{
    wchar_t message_korean[] = L"헬로우 월드";
    wcout << message_korean << endl;

    return 0;
}