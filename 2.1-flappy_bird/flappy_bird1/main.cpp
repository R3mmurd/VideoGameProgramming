/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the main program to run the game.
*/

#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

#include <Settings.hpp>

#include <src/Bird.hpp>

int main()
{
    Settings::init();
    
    sf::RenderWindow window{sf::VideoMode{Settings::WINDOW_WIDTH, Settings::WINDOW_HEIGHT}, "Flappy Bird", sf::Style::Close};

    Bird bird{
        Settings::WINDOW_WIDTH / 2 - Settings::BIRD_WIDTH / 2, Settings::WINDOW_HEIGHT / 2 - Settings::BIRD_HEIGHT / 2,
        Settings::BIRD_WIDTH, Settings::BIRD_HEIGHT
    };

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
