/*
    ISPPJ1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class CountDownBaseState.
*/

#pragma once

#include <src/World.hpp>
#include <src/states/BaseState.hpp>

class CountDownState: public BaseState
{
public:
    CountDownState(StateMachine* sm) noexcept;

    void update(float dt) noexcept override;

    void render(sf::RenderTarget& target) const noexcept override;

private:
    World world;
    int counter{3};
    float timer{0.f};
};
