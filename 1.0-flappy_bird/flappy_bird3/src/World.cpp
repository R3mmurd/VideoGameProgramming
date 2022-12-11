#include <Configuration.hpp>
#include <src/World.hpp>

World::World() noexcept
    : background{Configuration::textures["background"]}, ground{Configuration::textures["ground"]}
{
    ground.setPosition(0, Configuration::VIRTUAL_HEIGHT - Configuration::GROUND_HEIGHT);
}

void World::update(float dt) noexcept
{
    background_x += -Configuration::BACK_SCROLL_SPEED * dt;

    if (background_x <= -Configuration::BACKGROUND_LOOPING_POINT)
    {
        background_x = 0;
    }

    background.setPosition(background_x, 0);

    ground_x += -Configuration::MAIN_SCROLL_SPEED * dt;

    if (ground_x <= -Configuration::VIRTUAL_WIDTH)
    {
        ground_x = 0;
    }

    ground.setPosition(ground_x, Configuration::VIRTUAL_HEIGHT - Configuration::GROUND_HEIGHT);
}

void World::render(sf::RenderTarget& target) const noexcept
{
    target.draw(background);
    target.draw(ground);
}