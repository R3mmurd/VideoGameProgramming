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
    sf::RenderTexture render_texture{};
    render_texture.create(Settings::VIRTUAL_WIDTH, Settings::VIRTUAL_HEIGHT);

    sf::Vector2f scale_factors{
        float(Settings::WINDOW_WIDTH) / float(Settings::VIRTUAL_WIDTH), 
        float(Settings::WINDOW_HEIGHT) / float(Settings::VIRTUAL_HEIGHT)
    };

    sf::Sprite render_sprite{render_texture.getTexture()};
    render_sprite.setScale(scale_factors);

    Bird bird{
        Settings::VIRTUAL_WIDTH / 2 - Settings::BIRD_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2 - Settings::BIRD_HEIGHT / 2,
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

        render_texture.clear(sf::Color::Black);
        bird.render(render_texture);
        render_texture.display();

        window.draw(render_sprite);
        window.display();
    }

    return EXIT_SUCCESS;
}
