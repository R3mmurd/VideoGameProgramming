/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the main program to run the game.
*/

#include <SFML/Window.hpp>

#include <Settings.hpp>
#include <src/Game.hpp>

int main()
{
    Settings::init();

    Game game{};

    sf::Clock clock;
    sf::Time dt;

    while (game.get_window().isOpen())
    {
        sf::Event event;

        while (game.get_window().pollEvent(event))
        {
            if (event.type == sf::Event::Closed || (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape))
            {
                game.get_window().close();
            }
        }

        game.update(dt.asSeconds());
        game.render();

        dt = clock.restart();
    }

    return EXIT_SUCCESS;
}
