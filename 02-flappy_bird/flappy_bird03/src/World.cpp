/*
    ISPPJ1 2024
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class World.
*/

#include <Settings.hpp>
#include <src/World.hpp>

World::World() noexcept
    : background{Settings::textures["background"]}, ground{Settings::textures["ground"]}
{
    ground.setPosition(0, Settings::VIRTUAL_HEIGHT - Settings::GROUND_HEIGHT);
}

void World::update(float dt) noexcept
{
    background_x += -Settings::BACK_SCROLL_SPEED * dt;

    if (background_x <= -Settings::BACKGROUND_LOOPING_POINT)
    {
        background_x = 0;
    }

    background.setPosition(background_x, 0);

    ground_x += -Settings::MAIN_SCROLL_SPEED * dt;

    if (ground_x <= -Settings::VIRTUAL_WIDTH)
    {
        ground_x = 0;
    }

    ground.setPosition(ground_x, Settings::VIRTUAL_HEIGHT - Settings::GROUND_HEIGHT);
}

void World::render(sf::RenderTarget& target) const noexcept
{
    target.draw(background);
    target.draw(ground);
}