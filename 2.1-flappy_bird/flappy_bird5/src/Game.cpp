/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class Game.
*/

#include <Settings.hpp>
#include <src/Game.hpp>

Game::Game()
    : render_window{sf::VideoMode{Settings::WINDOW_WIDTH, Settings::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close},
      render_texture{},
      render_sprite{},
      bird{
        Settings::VIRTUAL_WIDTH / 2 - Settings::BIRD_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2 - Settings::BIRD_HEIGHT / 2,
        Settings::BIRD_WIDTH, Settings::BIRD_HEIGHT
      },
      world{}
{
    render_texture.create(Settings::VIRTUAL_WIDTH, Settings::VIRTUAL_HEIGHT);

    sf::Vector2f scale_factors{
        float(Settings::WINDOW_WIDTH) / float(Settings::VIRTUAL_WIDTH), 
        float(Settings::WINDOW_HEIGHT) / float(Settings::VIRTUAL_HEIGHT)
    };

    render_sprite.setTexture(render_texture.getTexture());
    render_sprite.setScale(scale_factors);
}

sf::RenderWindow& Game::get_window() noexcept
{
    return render_window;
}

void Game::handle_inputs(const sf::Event& event) noexcept
{
    if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left)
    {
        bird.jump();
    }
}

void Game::update(float dt) noexcept
{
    bird.update(dt);
    world.update(dt);
}

void Game::render() noexcept
{
    render_texture.clear(sf::Color::Black);
    world.render(render_texture);
    bird.render(render_texture);
    render_texture.display();

    render_window.draw(render_sprite);
    render_window.display();
}