/*
    ISPPV1 2024
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
    game.exec();

    return EXIT_SUCCESS;
}
