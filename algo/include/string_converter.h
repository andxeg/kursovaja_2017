#pragma once

#include <sstream>
#include <iostream>

template <typename T>
T convertFromStringTo(std::string str) {
    T val;
    std::stringstream stream(str);
    stream >> val;
    return val;
}


template <typename T>
std::string ToString(T val)
{
    std::stringstream stream;
    stream << val;
    return stream.str();
}
