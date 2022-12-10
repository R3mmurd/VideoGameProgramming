#include <stdexcept>

#include <Configuration.hpp>

std::unordered_map<std::string, sf::Texture> Configuration::textures{};

std::unordered_map<std::string, sf::SoundBuffer> Configuration::sound_buffers;

std::unordered_map<std::string, sf::Sound> Configuration::sounds{};

std::unordered_map<std::string, sf::Font> Configuration::fonts{};

void Configuration::init()
{
    Configuration::load_textures();
    Configuration::load_sounds();
    Configuration::load_fonts();
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

    if (!texture.loadFromFile("graphics/pipe.png"))
    {
        throw std::runtime_error{"Error loading texture graphics/pipe.png"};
    }

    Configuration::textures["pipe"] = texture;
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

    if (!buffer.loadFromFile("sounds/explosion.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/explosion.wav"};
    }

    result = Configuration::sound_buffers.emplace("explosion", buffer);

    sound.setBuffer(result.first->second);
    Configuration::sounds["explosion"] = sound;

    if (!buffer.loadFromFile("sounds/hurt.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/hurt.wav"};
    }

    result = Configuration::sound_buffers.emplace("hurt", buffer);

    sound.setBuffer(result.first->second);
    Configuration::sounds["hurt"] = sound;

    if (!buffer.loadFromFile("sounds/score.wav"))
    {
        throw std::runtime_error{"Error loading sound sounds/score.wav"};
    }

    result = Configuration::sound_buffers.emplace("score", buffer);

    sound.setBuffer(result.first->second);
    Configuration::sounds["score"] = sound;
}

void Configuration::load_fonts()
{
    sf::Font font;

    if (!font.loadFromFile("fonts/font.ttf"))
    {
        throw std::runtime_error{"Error loading font fonts/font.ttf"};
    }

    Configuration::fonts["font"] = font;

    if (!font.loadFromFile("fonts/flappy.ttf"))
    {
        throw std::runtime_error{"Error loading font fonts/flappy.ttf"};
    }

    Configuration::fonts["flappy"] = font;
}
