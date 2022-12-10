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
        Configuration::sounds["explosion"].play();
        Configuration::sounds["hurt"].play();
        bird_is_dead = true;
    }

    if (!bird_is_dead && world.update_scored(bird.get_collision_rect()))
    {
        ++score;
        Configuration::sounds["score"].play();
    }

}

void Game::render() noexcept
{
    render_texture.clear(sf::Color::Black);
    world.render(render_texture);
    bird.render(render_texture);

    sf::Text score_text;
    score_text.move(20, 10);
    score_text.setFont(Configuration::fonts["flappy"]);
    score_text.setString("Score: " + std::to_string(score));
    score_text.setCharacterSize(Configuration::FLAPPY_TEXT_SIZE);
    score_text.setFillColor(sf::Color::White);
    render_texture.draw(score_text);

    render_texture.display();

    render_window.draw(render_sprite);
    render_window.display();
}
