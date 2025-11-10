cmake_minimum_required(VERSION 4.0)
project(winsock_init)

set(CMAKE_CXX_STANDARD 20)

add_executable(winsock_init main.cpp
        common.h)

target_link_libraries(winsock_init ws2_32)