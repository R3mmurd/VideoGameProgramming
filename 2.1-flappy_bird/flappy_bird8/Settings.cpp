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

std::unordered_map<std::string, sf::SoundBuffer> Settings::sound_buffers;

std::unordered_map<std::string, sf::Sound> Settings::sounds{};

std::unordered_map<std::string, sf::Font> Settings::fonts{};

void Settings::init()
{
    Settings::load_textures();
    Settings::load_sounds();
    Settings::load_fonts();
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

    if (!buffer.loadFromFile("sounds/explosion.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/explosion.wav"};
    }

    result = Settings::sound_buffers.emplace("explosion", buffer);

    sound.setBuffer(result.first->second);
    Settings::sounds["explosion"] = sound;

    if (!buffer.loadFromFile("sounds/hurt.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/hurt.wav"};
    }

    result = Settings::sound_buffers.emplace("hurt", buffer);

    sound.setBuffer(result.first->second);
    Settings::sounds["hurt"] = sound;

    if (!buffer.loadFromFile("sounds/score.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/score.wav"};
    }

    result = Settings::sound_buffers.emplace("score", buffer);

    sound.setBuffer(result.first->second);
    Settings::sounds["score"] = sound;
}

void Settings::load_fonts()
{
    sf::Font font;

    if (!font.loadFromFile("fonts/font.ttf"))
    {
        throw std::runtime_error{"Error loading font fonts/font.ttf"};
    }

    Settings::fonts["font"] = font;

    if (!font.loadFromFile("fonts/flappy.ttf"))
    {
        throw std::runtime_error{"Error loading font fonts/flappy.ttf"};
    }

    Settings::fonts["flappy"] = font;
}
