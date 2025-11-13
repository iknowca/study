#include "common.h"

char *SERVERIP = (char *) "127.0.0.1";
#define SERVERPORT 9000
#define BUFFERSIZE 512

int main() {
    int retval;

    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        return 1;
    }

    //socket creation
    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == INVALID_SOCKET) {err_quit("socket()");}

    // connect()
    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    inet_pton(AF_INET, SERVERIP, &server_addr.sin_addr);
    server_addr.sin_port = htons(SERVERPORT);
    retval = connect(sock, (struct sockaddr *) &server_addr, sizeof(server_addr));
    if (retval == SOCKET_ERROR) {err_quit("connect()");}

    //data
    char buf[BUFFERSIZE + 1];
    int len;

    while (1) {
        // data input
        printf("\n[output data]");
        if (fgets(buf, BUFFERSIZE + 1, stdin) == nullptr) {break;}

        len = (int)strlen(buf);
        if (buf[len-1] == '\n')
            buf[len-1] = '\0';
        if (strlen(buf) ==0)
            break;

        // send data
        retval = send(sock, buf, (int)strlen(buf), 0);
        if (retval == SOCKET_ERROR) {err_display("send()"); break;}

        printf("\n[TCP] %d bytes sended\n", retval);

        // recv data
        retval = recv(sock, buf, retval, MSG_WAITALL);
        if (retval == SOCKET_ERROR) {
            err_display("recv()");
            break;
        } else if (retval == 0 ) {
            break;
        }

        buf[retval] = '\0';
        printf("[TCP] &d bytes received", retval);
        printf("data: %s\n", buf);
    }

    closesocket(sock);
    WSACleanup();
    return 0;
}