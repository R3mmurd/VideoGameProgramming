#pragma once

#include <SFML/Graphics/Sprite.hpp>

class RenderTarget;

class World
{
public:
    World();

    World(const World& world) = delete;

    World& operator = (World) = delete;

    void update(float dt) noexcept;

    void render(sf::RenderTarget& target) const noexcept;
private:
    sf::Sprite background;
    sf::Sprite ground;

    float background_x;
    float ground_x;
};
