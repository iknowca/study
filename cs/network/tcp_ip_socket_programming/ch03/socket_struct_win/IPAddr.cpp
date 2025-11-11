 // g++.exe IPAddr.cpp -lws2_32
#include "common.h"

int main() {
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0 ) {
        return 1;
    }

    const char *ipv4test = "147.46.114.70";
    printf("IPv4 addr (before convert) = %s\n", ipv4test);

    struct in_addr ipv4num;
    inet_pton(AF_INET, ipv4test, &ipv4num);
    printf("IPv4 addr (after convert) =%#x\n", ipv4num.s_addr);

    char ipv4str[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &ipv4num, ipv4str, sizeof(ipv4str));
    printf("IPv4 addr (after convert) = %s\n", ipv4str);

}