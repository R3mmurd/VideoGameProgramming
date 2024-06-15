/*
    ISPPJ1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class CountDownBaseState.
*/

#include <cmath>

#include <Settings.hpp>
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

    sf::Text text;
    text.setFont(Settings::fonts["font"]);
    text.setString(std::to_string(counter));
    text.setCharacterSize(Settings::HUGE_TEXT_SIZE);
    text.setFillColor(sf::Color::White);
    float center_x = text.getGlobalBounds().width / 2.f;
    float center_y = text.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + text.getLocalBounds().left);
    float local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(sf::Vector2f{Settings::VIRTUAL_WIDTH / 2 + 2, Settings::VIRTUAL_HEIGHT / 2 + 2});
    text.setFillColor(sf::Color::Black);
    target.draw(text);
    text.move(-2, -2);
    text.setFillColor(sf::Color::White);
    target.draw(text);
}