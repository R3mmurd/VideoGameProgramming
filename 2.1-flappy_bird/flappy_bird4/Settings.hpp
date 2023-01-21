/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of Settings that contains constants
    to set up the game and methods to load multimedia files.
*/

#pragma once

#include <filesystem>
#include <string>
#include <unordered_map>

namespace fs = std::filesystem;

#include <SFML/Graphics.hpp>

struct Settings
{
    static const fs::path GRAPHICS_PATH;
    
    static constexpr int WINDOW_WIDTH{1280};
    static constexpr int WINDOW_HEIGHT{720};
    static constexpr int VIRTUAL_WIDTH{512};
    static constexpr int VIRTUAL_HEIGHT{288};
    static constexpr float BIRD_WIDTH{39.f};
    static constexpr float BIRD_HEIGHT{28.f};
    static constexpr float GROUND_HEIGHT{16.f};
    static constexpr float BACKGROUND_LOOPING_POINT{1157.f};
    static constexpr float MAIN_SCROLL_SPEED{100.f};
    static constexpr float BACK_SCROLL_SPEED{50.f};
    static constexpr float GRAVITY{980.f};

    static std::unordered_map<std::string, sf::Texture> textures;

    static void init();

    static void load_textures();
};
