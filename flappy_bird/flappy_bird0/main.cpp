#include <SFML/Window.hpp>

int main()
{
    sf::Window window{sf::VideoMode{1280, 720}, "Flappy Bird", sf::Style::Close};

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
    }

    return EXIT_SUCCESS;
}
