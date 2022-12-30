/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class PipePair.
*/

#pragma once

#include <src/Bird.hpp>
#include <src/Pipe.hpp>

class PipePair
{
public:
    PipePair(float _y) noexcept;

    bool collides(const sf::FloatRect& rect) const noexcept;

    void update(float dt) noexcept;

    void render(sf::RenderTarget& target) const noexcept;

    bool is_out_of_game() const noexcept;

    bool update_scored(const sf::FloatRect& rect) noexcept;

private:
    float x;
    float y;
    Pipe top;
    Pipe bottom;

    bool scored{false};
};