/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class BaseState.
*/

#pragma once

#include <SFML/Graphics.hpp>

class StateMachine;

class BaseState
{
public:
    BaseState(StateMachine* sm) : state_machine(sm) {}

    virtual ~BaseState() {}

    virtual void enter() noexcept {}

    virtual void exit() noexcept {}

    virtual void handle_inputs(const sf::Event& event) noexcept {}

    virtual void update(float dt) noexcept {}

    virtual void render(sf::RenderTarget& target) const noexcept {}


protected:
    StateMachine* state_machine;
};
