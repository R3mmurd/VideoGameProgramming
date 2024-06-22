/*
    ISPPJ1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the Settings methods to load multimedia files.
*/

#include <stdexcept>

#include <Settings.hpp>

const fs::path Settings::ASSETS_PATH{"assets"};

const fs::path Settings::TEXTURES_PATH{Settings::ASSETS_PATH / "textures"};

const fs::path Settings::SOUNDS_PATH{Settings::ASSETS_PATH / "sounds"};

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

    if (!texture.loadFromFile(Settings::TEXTURES_PATH / "bird.png"))
    {
        throw std::runtime_error{"Error loading texture assets/graphics/bird.png"};
    }

    Settings::textures["bird"] = texture;

    if (!texture.loadFromFile(Settings::TEXTURES_PATH / "background.png"))
    {
        throw std::runtime_error{"Error loading texture assets/graphics/background.png"};
    }

    Settings::textures["background"] = texture;

    if (!texture.loadFromFile(Settings::TEXTURES_PATH / "ground.png"))
    {
        throw std::runtime_error{"Error loading texture assets/graphics/ground.png"};
    }

    Settings::textures["ground"] = texture;

    if (!texture.loadFromFile(Settings::TEXTURES_PATH / "log.png"))
    {
        throw std::runtime_error{"Error loading texture assets/graphics/log.png"};
    }

    Settings::textures["Log"] = texture;
}

void Settings::load_sounds()
{
    sf::SoundBuffer buffer;
    sf::Sound sound;
    
    if (!buffer.loadFromFile(Settings::SOUNDS_PATH / "jump.wav"))
    {
        throw std::runtime_error{"Error loading sound assets/sounds/jump.wav"};
    }

    auto result = Settings::sound_buffers.emplace("jump", buffer);

    sound.setBuffer(result.first->second);
    Settings::sounds["jump"] = sound;
}