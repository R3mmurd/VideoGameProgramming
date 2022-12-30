/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the Settings methods to load multimedia files.
*/

#include <stdexcept>

#include <Settings.hpp>

std::unordered_map<std::string, sf::Texture> Settings::textures{};

void Settings::init()
{
    Settings::load_textures();
}

void Settings::load_textures()
{
    sf::Texture texture{};

    if (!texture.loadFromFile("graphics/bird.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/bird.png"};
    }

    Settings::textures["bird"] = texture;
}