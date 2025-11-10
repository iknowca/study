#include <iostream>
#include "common.h"

// TIP 코드를 <b>Run</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나 여백에서 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
int main(int argc, char *argv[]) {
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) return 1;
    printf("winsock_init\n");

    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == INVALID_SOCKET) err_quit("socket()");
    printf("socket created");

    WSACleanup();
    return 0;
}