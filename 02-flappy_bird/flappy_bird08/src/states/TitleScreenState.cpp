/*
    ISPPJ1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class TitleScreenState.
*/

#include <cmath>

#include <Settings.hpp>
#include <src/states/StateMachine.hpp>
#include <src/states/TitleScreenState.hpp>

TitleScreenState::TitleScreenState(StateMachine* sm) noexcept
    : BaseState{sm}, world{}
{

}

void TitleScreenState::handle_inputs(const sf::Event& event) noexcept
{
    if (event.key.code == sf::Keyboard::Enter)
    {
        state_machine->change_state("count_down");
    }
}

void TitleScreenState::update(float dt) noexcept
{
    world.update(dt);
}

void TitleScreenState::render(sf::RenderTarget& target) const noexcept 
{
    world.render(target);

    sf::Text title;
    title.setFont(Settings::fonts["flappy"]);
    title.setString("Flappy Bird");
    title.setCharacterSize(Settings::FLAPPY_TEXT_SIZE);
    float center_x = title.getGlobalBounds().width / 2.f;
    float center_y = title.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + title.getLocalBounds().left);
    float local_center_y = round(center_y + title.getLocalBounds().top);
    title.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    title.setPosition(sf::Vector2f{Settings::VIRTUAL_WIDTH / 2 + 2, Settings::VIRTUAL_HEIGHT / 3 + 2});
    title.setFillColor(sf::Color::Black);
    target.draw(title);
    title.move(-2, -2);
    title.setFillColor(sf::Color::White);
    target.draw(title);

    sf::Text text;
    text.setFont(Settings::fonts["font"]);
    text.setString("Press enter to start");
    text.setCharacterSize(Settings::MEDIUM_TEXT_SIZE);
    center_x = text.getGlobalBounds().width / 2.f;
    center_y = text.getGlobalBounds().height / 2.f;
    local_center_x = round(center_x + text.getLocalBounds().left);
    local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(sf::Vector2f{Settings::VIRTUAL_WIDTH / 2 + 2, 2 * Settings::VIRTUAL_HEIGHT / 3 + 2});
    text.setFillColor(sf::Color::Black);
    target.draw(text);
    text.move(-2, -2);
    text.setFillColor(sf::Color::White);
    target.draw(text);
}