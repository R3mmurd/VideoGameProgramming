#pragma once

#include <SFML/Graphics.hpp>

class Pipe
{
public:
    Pipe(float _x, float _y, bool inverted) noexcept;

    void update(float _x) noexcept;

    void render(sf::RenderTarget& target) const noexcept;

private:
    float x;
    float y;
    bool inverted;
    sf::Sprite sprite;
};