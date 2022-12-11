#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

#include <Configuration.hpp>

#include <src/Bird.hpp>

int main()
{
    Configuration::init();
    
    sf::RenderWindow window{sf::VideoMode{Configuration::WINDOW_WIDTH, Configuration::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close};

    Bird bird{
        Configuration::WINDOW_WIDTH / 2 - Configuration::BIRD_WIDTH / 2, Configuration::WINDOW_HEIGHT / 2 - Configuration::BIRD_HEIGHT / 2,
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

        window.clear(sf::Color::Black);
        
        bird.render(window);

        window.display();
    }

    return EXIT_SUCCESS;
}
