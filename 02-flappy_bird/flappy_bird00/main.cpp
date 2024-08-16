/*
    ISPPV1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains an example of using SFML to setup a window
    and close it by pressing the key Escape.
*/

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
