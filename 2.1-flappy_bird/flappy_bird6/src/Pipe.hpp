/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class Pipe.
*/

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