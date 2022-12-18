#include <Settings.hpp>
#include <src/Bird.hpp>

Bird::Bird(float _x, float _y, float w, float h) noexcept
    : x{_x}, y{_y}, width{w}, height{h}, vy{0.f}, sprite{Settings::textures["bird"]}
{
    sprite.setPosition(x, y);
}

void Bird::update(float dt) noexcept
{
    vy += Settings::GRAVITY * dt;
    y += vy;
    sprite.setPosition(x, y);
}

void Bird::render(sf::RenderTarget& target) const noexcept
{
    target.draw(sprite);
}