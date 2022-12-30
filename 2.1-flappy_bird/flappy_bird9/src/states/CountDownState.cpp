/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class CountDownBaseState.
*/

#include <Settings.hpp>
#include <src/text_utilities.hpp>
#include <src/states/CountDownState.hpp>
#include <src/states/StateMachine.hpp>

CountDownState::CountDownState(StateMachine* sm) noexcept
    : BaseState{sm}, world{}
{

}

void CountDownState::update(float dt) noexcept
{
    timer += dt;

    if (timer >= 1.f)
    {
        timer = 0.f;
        --counter;

        if (counter == 0)
        {
            state_machine->change_state("playing");
        }
    }

    world.update(dt);
}

void CountDownState::render(sf::RenderTarget& target) const noexcept
{
    world.render(target);
    target.draw(build_text(std::to_string(counter), Settings::HUGE_TEXT_SIZE, "font", sf::Color::White, true));
}