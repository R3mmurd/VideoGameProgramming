#include <Configuration.hpp>
#include <src/Pipe.hpp>

Pipe::Pipe(float _x, float _y, bool _inverted) noexcept
    : x{_x}, y{_y}, inverted{_inverted}, sprite{Configuration::textures["pipe"]}
{
    if (inverted)
    {
        sprite.rotate(180.f);
    }
}

sf::FloatRect Pipe::get_collision_rect() const noexcept
{
    if (!inverted)
    {
        return sf::FloatRect{x, y, Configuration::PIPE_WIDTH, Configuration::PIPE_HEIGHT};
    }

    return sf::FloatRect{x - Configuration::PIPE_WIDTH, y - Configuration::PIPE_HEIGHT, Configuration::PIPE_WIDTH, Configuration::PIPE_HEIGHT};
}

void Pipe::update(float _x) noexcept
{
    x = _x;

    if (inverted)
    {
        x += Configuration::PIPE_WIDTH;
    }

    sprite.setPosition(x, y);
}

void Pipe::render(sf::RenderTarget& target) const noexcept
{
    target.draw(sprite);
}
