#pragma once

#include <type_traits>

template <class T>
class Factory
{
public:
    template <typename N1, typename N2, typename ...Args>
    T create(N1 x, N2 y, Args... args)
    {
        static_assert(std::is_convertible<N1, float>::value, "Template argument N1 should be convertible to float.");
        static_assert(std::is_convertible<N2, float>::value, "Template argument N2 should be convertible to float.");
        static_assert(std::is_constructible<T, float, float, Args...>::value);
        return T{float(x), float(y), args...};
    }
};
