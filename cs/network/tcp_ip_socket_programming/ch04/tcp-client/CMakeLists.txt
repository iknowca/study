cmake_minimum_required(VERSION 4.0)
project(tcp_client)

set(CMAKE_CXX_STANDARD 20)

add_executable(tcp_client main.cpp)
target_link_libraries(tcp_client ws2_32)