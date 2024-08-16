/*
    ISPPV1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class Game.
*/

#pragma once

#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>

#include <src/states/StateMachine.hpp>

class Game
{
public:
    Game();

    Game(const Game&) = delete;

    Game& operator = (Game) = delete;

    void handle_inputs(const sf::Event& event) noexcept;

    void update(float dt) noexcept;

    void render() noexcept;

    void exec() noexcept;

private:
    sf::RenderWindow render_window;
    sf::RenderTexture render_texture;
    sf::Sprite render_sprite;

    StateMachine state_machine;
};
