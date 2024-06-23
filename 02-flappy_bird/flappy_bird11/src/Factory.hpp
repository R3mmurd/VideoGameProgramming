#pragma once

#include <list>
#include <memory>
#include <type_traits>

#include <iostream>

template <class T>
class Factory
{
public:
    template <typename N1, typename N2, typename ...Args>
    std::shared_ptr<T> create(N1 x, N2 y, Args... args)
    {
        static_assert(std::is_convertible<N1, float>::value, "Template argument N1 should be convertible to float.");
        static_assert(std::is_convertible<N2, float>::value, "Template argument N2 should be convertible to float.");
        static_assert(std::is_constructible<T, float, float, Args...>::value);

        if (!buffer.empty())
        {
            auto object = buffer.back();
            object->reset(float(x), float(y));
            buffer.pop_back();
            return object;
        }
        return std::make_shared<T>(float(x), float(y), args...);
    }

    void remove(std::shared_ptr<T> object)
    {
        buffer.push_back(object);
    }

private:
    std::list<std::shared_ptr<T>> buffer;
};
