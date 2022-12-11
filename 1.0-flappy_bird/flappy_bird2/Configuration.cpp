#include <stdexcept>

#include <Configuration.hpp>

std::unordered_map<std::string, sf::Texture> Configuration::textures{};

void Configuration::init()
{
    Configuration::load_textures();
}

void Configuration::load_textures()
{
    sf::Texture texture{};

    if (!texture.loadFromFile("graphics/bird.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/bird.png"};
    }

    Configuration::textures["bird"] = texture;
}