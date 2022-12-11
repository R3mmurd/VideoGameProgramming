#include <Configuration.hpp>
#include <src/Bird.hpp>

Bird::Bird(float _x, float _y, float w, float h) noexcept
    : x{_x}, y{_y}, width{w}, height{h}, sprite{Configuration::textures["bird"]}
{
    sprite.setPosition(x, y);
}

void Bird::render(sf::RenderWindow& window) const noexcept
{
    window.draw(sprite);
}