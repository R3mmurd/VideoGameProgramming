#include <stdexcept>

#include <Settings.hpp>

std::unordered_map<std::string, sf::Texture> Settings::textures{};

std::unordered_map<std::string, sf::SoundBuffer> Settings::sound_buffers;

std::unordered_map<std::string, sf::Sound> Settings::sounds{};

void Settings::init()
{
    Settings::load_textures();
    Settings::load_sounds();
}

void Settings::load_textures()
{
    sf::Texture texture{};

    if (!texture.loadFromFile("graphics/bird.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/bird.png"};
    }

    Settings::textures["bird"] = texture;

    if (!texture.loadFromFile("graphics/background.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/background.png"};
    }

    Settings::textures["background"] = texture;

    if (!texture.loadFromFile("graphics/ground.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/ground.png"};
    }

    Settings::textures["ground"] = texture;

    if (!texture.loadFromFile("graphics/pipe.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/pipe.png"};
    }

    Settings::textures["pipe"] = texture;
}

void Settings::load_sounds()
{
    sf::SoundBuffer buffer;
    sf::Sound sound;
    
    if (!buffer.loadFromFile("sounds/jump.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/jump.wav"};
    }

    auto result = Settings::sound_buffers.emplace("jump", buffer);

    sound.setBuffer(result.first->second);
    Settings::sounds["jump"] = sound;
}