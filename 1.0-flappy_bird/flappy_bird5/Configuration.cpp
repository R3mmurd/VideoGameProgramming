#include <stdexcept>

#include <Configuration.hpp>

std::unordered_map<std::string, sf::Texture> Configuration::textures{};

std::unordered_map<std::string, sf::SoundBuffer> Configuration::sound_buffers;

std::unordered_map<std::string, sf::Sound> Configuration::sounds{};

void Configuration::init()
{
    Configuration::load_textures();
    Configuration::load_sounds();
}

void Configuration::load_textures()
{
    sf::Texture texture{};

    if (!texture.loadFromFile("graphics/bird.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/bird.png"};
    }

    Configuration::textures["bird"] = texture;

    if (!texture.loadFromFile("graphics/background.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/background.png"};
    }

    Configuration::textures["background"] = texture;

    if (!texture.loadFromFile("graphics/ground.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/ground.png"};
    }

    Configuration::textures["ground"] = texture;
}

void Configuration::load_sounds()
{
    sf::SoundBuffer buffer;
    sf::Sound sound;
    
    if (!buffer.loadFromFile("sounds/jump.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/jump.wav"};
    }

    auto result = Configuration::sound_buffers.emplace("jump", buffer);

    sound.setBuffer(result.first->second);
    Configuration::sounds["jump"] = sound;
}