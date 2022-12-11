#include <Configuration.hpp>
#include <src/Game.hpp>

Game::Game()
    : render_window{sf::VideoMode{Configuration::WINDOW_WIDTH, Configuration::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close},
      render_texture{},
      render_sprite{},
      bird{
        Configuration::VIRTUAL_WIDTH / 2 - Configuration::BIRD_WIDTH / 2, Configuration::VIRTUAL_HEIGHT / 2 - Configuration::BIRD_HEIGHT / 2,
        Configuration::BIRD_WIDTH, Configuration::BIRD_HEIGHT
      },
      world{}
{
    render_texture.create(Configuration::VIRTUAL_WIDTH, Configuration::VIRTUAL_HEIGHT);

    sf::Vector2f scale_factors{
        float(Configuration::WINDOW_WIDTH) / float(Configuration::VIRTUAL_WIDTH), 
        float(Configuration::WINDOW_HEIGHT) / float(Configuration::VIRTUAL_HEIGHT)
    };

    render_sprite.setTexture(render_texture.getTexture());
    render_sprite.setScale(scale_factors);
}

sf::RenderWindow& Game::get_window() noexcept
{
    return render_window;
}

void Game::update(float dt) noexcept
{
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