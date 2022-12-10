#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

#include <Configuration.hpp>

#include <src/Bird.hpp>

int main()
{
    Configuration::init();
    
    sf::RenderWindow window{sf::VideoMode{Configuration::WINDOW_WIDTH, Configuration::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close};
    sf::RenderTexture render_texture{};
    render_texture.create(Configuration::VIRTUAL_WIDTH, Configuration::VIRTUAL_HEIGHT);

    sf::Vector2f scale_factors{
        float(Configuration::WINDOW_WIDTH) / float(Configuration::VIRTUAL_WIDTH), 
        float(Configuration::WINDOW_HEIGHT) / float(Configuration::VIRTUAL_HEIGHT)
    };

    sf::Sprite render_sprite{render_texture.getTexture()};
    render_sprite.setScale(scale_factors);

    Bird bird{
        Configuration::VIRTUAL_WIDTH / 2 - Configuration::BIRD_WIDTH / 2, Configuration::VIRTUAL_HEIGHT / 2 - Configuration::BIRD_HEIGHT / 2,
        Configuration::BIRD_WIDTH, Configuration::BIRD_HEIGHT
    };

    sf::Texture texture{};

    while (window.isOpen())
    {
        sf::Event event;

        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed || (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape))
            {
                window.close();
            }
        }

        render_texture.clear(sf::Color::Black);
        bird.render(render_texture);
        render_texture.display();

        window.draw(render_sprite);
        window.display();
    }

    return EXIT_SUCCESS;
}
