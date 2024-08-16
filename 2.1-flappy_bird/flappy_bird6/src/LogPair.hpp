/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class LogPair.
*/

#pragma once

#include <src/Bird.hpp>
#include <src/Log.hpp>

class LogPair
{
public:
    LogPair(float _x, float _y) noexcept;

    void update(float dt) noexcept;

    void render(sf::RenderTarget& target) const noexcept;

    bool is_out_of_game() const noexcept;

private:
    float x;
    float y;
    Log top;
    Log bottom;
};