#pragma once

#include <string>
#include <unordered_map>

#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>

struct Settings
{
    static constexpr int WINDOW_WIDTH{1280};
    static constexpr int WINDOW_HEIGHT{720};
    static constexpr int VIRTUAL_WIDTH{512};
    static constexpr int VIRTUAL_HEIGHT{288};
    static constexpr float BIRD_WIDTH{38.f};
    static constexpr float BIRD_HEIGHT{24.f};
    static constexpr float PIPE_WIDTH{70.f};
    static constexpr float PIPE_HEIGHT{288.f};
    static constexpr float PIPES_GAP{90.f};
    static constexpr float GROUND_HEIGHT{16.f};
    static constexpr float BACKGROUND_LOOPING_POINT{413.f};
    static constexpr float MAIN_SCROLL_SPEED{100.f};
    static constexpr float BACK_SCROLL_SPEED{50.f}; // MAIN_SCROLL_SPEED / 2
    static constexpr float GRAVITY{0.2f};
    static constexpr float JUMP_TAKEOFF_SPEED{GRAVITY / 6.f};
    static constexpr float TIME_TO_SPAWN_PIPES{1.5f};
    static constexpr int MEDIUM_TEXT_SIZE{14};
    static constexpr int HUGE_TEXT_SIZE{56};
    static constexpr int FLAPPY_TEXT_SIZE{28};

    static std::unordered_map<std::string, sf::Texture> textures;
    static std::unordered_map<std::string, sf::SoundBuffer> sound_buffers;
    static std::unordered_map<std::string, sf::Sound> sounds;
    static std::unordered_map<std::string, sf::Font> fonts;

    static sf::Music music;

    static void init();

    static void load_textures();

    static void load_sounds();

    static void load_fonts();
};
