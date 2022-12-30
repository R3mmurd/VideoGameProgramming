/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class Pipe.
*/

#include <Settings.hpp>
#include <src/Pipe.hpp>

Pipe::Pipe(float _x, float _y, bool _inverted) noexcept
    : x{_x}, y{_y}, inverted{_inverted}, sprite{Settings::textures["pipe"]}
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
        return sf::FloatRect{x, y, Settings::PIPE_WIDTH, Settings::PIPE_HEIGHT};
    }

    return sf::FloatRect{x - Settings::PIPE_WIDTH, y - Settings::PIPE_HEIGHT, Settings::PIPE_WIDTH, Settings::PIPE_HEIGHT};
}

void Pipe::update(float _x) noexcept
{
    x = _x;

    if (inverted)
    {
        x += Settings::PIPE_WIDTH;
    }

    sprite.setPosition(x, y);
}

void Pipe::render(sf::RenderTarget& target) const noexcept
{
    target.draw(sprite);
}
