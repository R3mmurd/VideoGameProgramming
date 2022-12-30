/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class Bird.
*/

#pragma once

#include <SFML/Graphics.hpp>

class Bird
{
public:
    Bird(float _x, float _y, float w, float h) noexcept;

    Bird(const Bird&) = delete;

    Bird& operator = (Bird&) = delete;

    void render(sf::RenderWindow& window) const noexcept;

private:
    float x;
    float y;
    float width;
    float height;
    sf::Sprite sprite;
};
