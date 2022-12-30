/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of Settings that contains constants
    to set up the game and methods to load multimedia files.
*/

#pragma once

#include <string>
#include <unordered_map>

#include <SFML/Graphics.hpp>

struct Settings
{
    static constexpr int WINDOW_WIDTH{1280};
    static constexpr int WINDOW_HEIGHT{720};
    static constexpr int VIRTUAL_WIDTH{512};
    static constexpr int VIRTUAL_HEIGHT{288};
    static constexpr float BIRD_WIDTH{38.f};
    static constexpr float BIRD_HEIGHT{24.f};
    static constexpr float GROUND_HEIGHT{16.f};
    static constexpr float BACKGROUND_LOOPING_POINT{413.f};
    static constexpr float MAIN_SCROLL_SPEED{100.f};
    static constexpr float BACK_SCROLL_SPEED{50.f};
    static constexpr float GRAVITY{0.2f};

    static std::unordered_map<std::string, sf::Texture> textures;

    static void init();

    static void load_textures();
};
