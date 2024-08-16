/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class Log.
*/

#include <Settings.hpp>
#include <src/Log.hpp>

Log::Log(float _x, float _y, bool _inverted) noexcept
    : x{_x}, y{_y}, inverted{_inverted}, sprite{Settings::textures["Log"]}
{
    if (inverted)
    {
        sprite.rotate(180.f);
    }
}

void Log::update(float _x) noexcept
{
    x = _x;

    if (inverted)
    {
        x += Settings::LOG_WIDTH;
    }

    sprite.setPosition(x, y);
}

void Log::render(sf::RenderTarget& target) const noexcept
{
    target.draw(sprite);
}
