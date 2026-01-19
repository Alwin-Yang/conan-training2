cmake_minimum_required(VERSION 3.15)
project(formatter CXX)

add_executable(formatter src/main.cpp)

if (USE_STD_FORMAT) # If the USE_STD_FORMAT is true, then use the std::format library, the variable can be found in conanfile.py.
    target_compile_definitions(formatter PRIVATE USE_STD_FORMAT)
else()
    find_package(fmt REQUIRED)
    target_link_libraries(formatter fmt::fmt)
endif()
