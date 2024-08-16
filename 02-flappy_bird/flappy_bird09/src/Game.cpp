/*
    ISPPV1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class Game.
*/

#include <Settings.hpp>
#include <src/Game.hpp>
#include <src/states/CountDownState.hpp>
#include <src/states/TitleScreenState.hpp>
#include <src/states/PlayingState.hpp>

Game::Game()
    : render_window{sf::VideoMode{Settings::WINDOW_WIDTH, Settings::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close},
      render_texture{},
      render_sprite{},
      state_machine{
        {"title", [](StateMachine* sm) { return std::make_shared<TitleScreenState>(sm); }},
        {"count_down", [](StateMachine* sm) { return std::make_shared<CountDownState>(sm); }},
        {"playing", [](StateMachine* sm) { return std::make_shared<PlayingState>(sm); }}
      }
{
    render_texture.create(Settings::VIRTUAL_WIDTH, Settings::VIRTUAL_HEIGHT);

    sf::Vector2f scale_factors{
        float(Settings::WINDOW_WIDTH) / float(Settings::VIRTUAL_WIDTH), 
        float(Settings::WINDOW_HEIGHT) / float(Settings::VIRTUAL_HEIGHT)
    };

    render_sprite.setTexture(render_texture.getTexture());
    render_sprite.setScale(scale_factors);

    state_machine.change_state("title");

    Settings::music.setLoop(true);
    Settings::music.play();
}

sf::RenderWindow& Game::get_window() noexcept
{
    return render_window;
}

void Game::handle_inputs(const sf::Event& event) noexcept
{
    state_machine.handle_inputs(event);
}

void Game::update(float dt) noexcept
{
    state_machine.update(dt);
}

void Game::render() noexcept
{
    render_texture.clear(sf::Color::Black);
    
    state_machine.render(render_texture);

    render_texture.display();

    render_window.draw(render_sprite);
    render_window.display();
}
