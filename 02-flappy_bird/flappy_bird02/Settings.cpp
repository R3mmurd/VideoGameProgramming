/*
    ISPPV1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the Settings methods to load multimedia files.
*/

#include <stdexcept>

#include <Settings.hpp>

const fs::path Settings::ASSETS_PATH{"assets"};

const fs::path Settings::TEXTURES_PATH{Settings::ASSETS_PATH / "textures"};

std::unordered_map<std::string, sf::Texture> Settings::textures{};

void Settings::init()
{
    Settings::load_textures();
}

void Settings::load_textures()
{
    sf::Texture texture{};

    if (!texture.loadFromFile(Settings::TEXTURES_PATH / "bird.png"))
    {
        throw std::runtime_error{"Error loading texture assets/graphics/bird.png"};
    }

    Settings::textures["bird"] = texture;
}