/*
    ISPPV1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class PlayingBaseState.
*/

#include <Settings.hpp>
#include <src/states/StateMachine.hpp>
#include <src/states/PlayingState.hpp>

PlayingState::PlayingState(StateMachine* sm) noexcept
    : BaseState{sm},
      bird{
          Settings::VIRTUAL_WIDTH / 2 - Settings::BIRD_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2 - Settings::BIRD_HEIGHT / 2,
          Settings::BIRD_WIDTH, Settings::BIRD_HEIGHT
      },
      world{true}
{

}

void PlayingState::exit() noexcept
{
    world.reset();
}

void PlayingState::handle_inputs(const sf::Event& event) noexcept
{
    if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left)
    {
        bird.jump();
    }
}

void PlayingState::update(float dt) noexcept
{
    bird.update(dt);
    world.update(dt);

    if (world.collides(bird.get_collision_rect()))
    {
        Settings::sounds["explosion"].play();
        Settings::sounds["hurt"].play();
        state_machine->change_state("count_down");
        return;
    }

    if (world.update_scored(bird.get_collision_rect()))
    {
        ++score;
        Settings::sounds["score"].play();
    }
}

void PlayingState::render(sf::RenderTarget& target) const noexcept
{
    world.render(target);
    bird.render(target);

    sf::Text score_text;
    score_text.move(22, 12);
    score_text.setFont(Settings::fonts["flappy"]);
    score_text.setString("Score: " + std::to_string(score));
    score_text.setCharacterSize(Settings::FLAPPY_TEXT_SIZE);
    score_text.setFillColor(sf::Color::Black);
    target.draw(score_text);
    score_text.move(-2, -2);
    score_text.setFillColor(sf::Color::White);
    target.draw(score_text);
}