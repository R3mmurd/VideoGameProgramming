/*
    ISPPV1 2024
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

    if (!bird_is_dead && world.collides(bird.get_collision_rect()))
    {
        Settings::sounds["explosion"].play();
        Settings::sounds["hurt"].play();
        bird_is_dead = true;
    }

    if (!bird_is_dead && world.update_scored(bird.get_collision_rect()))
    {
        ++score;
        Settings::sounds["score"].play();
    }

}

void Game::render() noexcept
{
    render_texture.clear(sf::Color::Black);
    world.render(render_texture);
    bird.render(render_texture);

    sf::Text score_text;
    score_text.move(22, 12);
    score_text.setFont(Settings::fonts["flappy"]);
    score_text.setString("Score: " + std::to_string(score));
    score_text.setCharacterSize(Settings::FLAPPY_TEXT_SIZE);
    score_text.setFillColor(sf::Color::Black);
    render_texture.draw(score_text);
    score_text.move(-2, -2);
    score_text.setFillColor(sf::Color::White);
    render_texture.draw(score_text);

    render_texture.display();

    render_window.draw(render_sprite);
    render_window.display();
}
