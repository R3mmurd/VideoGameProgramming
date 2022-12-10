#pragma once

#include <list>
#include <random>

#include <SFML/Graphics.hpp>

#include <src/PipePair.hpp>

class World
{
public:
    World();

    World(const World& world) = delete;

    World& operator = (World) = delete;

    bool collides(const sf::FloatRect& rect) const noexcept;

    bool update_scored(const sf::FloatRect& rect) noexcept;

    void update(float dt) noexcept;

    void render(sf::RenderTarget& target) const noexcept;
private:
    sf::Sprite background;
    sf::Sprite ground;

    float background_x;
    float ground_x;

    std::list<PipePair> pipes;

    std::mt19937 rng;

    float pipes_spawn_timer{0.f};
    float last_pipe_y{0.f};
};
