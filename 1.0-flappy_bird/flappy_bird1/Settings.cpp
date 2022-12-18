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