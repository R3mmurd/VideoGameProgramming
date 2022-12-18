#pragma once

#include <string>
#include <unordered_map>

#include <SFML/Graphics.hpp>

struct Settings
{
    static constexpr int WINDOW_WIDTH{1280};
    static constexpr int WINDOW_HEIGHT{720};
    static constexpr float BIRD_WIDTH{38.f};
    static constexpr float BIRD_HEIGHT{24.f};

    static std::unordered_map<std::string, sf::Texture> textures;

    static void init();

    static void load_textures();
};
 