/*
    ISPPV1 2024
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
    : BaseState{sm}
{

}

void CountDownState::enter(std::shared_ptr<World> _world, std::shared_ptr<Bird> _bird) noexcept
{
    world = _world;
    world->reset(false);
    bird = _bird;
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
            state_machine->change_state("playing", world, bird);
        }
    }

    world->update(dt);
}

void CountDownState::render(sf::RenderTarget& target) const noexcept
{
    world->render(target);
    render_text(target, Settings::VIRTUAL_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2, std::to_string(counter), Settings::HUGE_TEXT_SIZE, "font", sf::Color::White, true);
}