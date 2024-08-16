/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class World.
*/

#include <Settings.hpp>
#include <src/World.hpp>

World::World() noexcept
    : background{Settings::textures["background"]}, ground{Settings::textures["ground"]},
      logs{}, rng{std::default_random_engine{}()}
{
    ground.setPosition(0, Settings::VIRTUAL_HEIGHT - Settings::GROUND_HEIGHT);
    std::uniform_int_distribution<int> dist(0, 80);
    last_log_y = -Settings::LOG_HEIGHT + dist(rng) + 20;
}

void World::update(float dt) noexcept
{
    logs_spawn_timer += dt;

    if (logs_spawn_timer >= Settings::TIME_TO_SPAWN_LOGS)
    {
        logs_spawn_timer = 0.f;

        std::uniform_int_distribution<int> dist{-20, 20};
        float y = std::max(-Settings::LOG_HEIGHT + 10, std::min(last_log_y + dist(rng), Settings::VIRTUAL_HEIGHT + 90 - Settings::LOG_HEIGHT));

        last_log_y = y;

        logs.push_back(log_factory.create(Settings::VIRTUAL_WIDTH, y));
    }

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

    for (auto it = logs.begin(); it != logs.end(); )
    {
        if (it->is_out_of_game())
        {
            it = logs.erase(it);
        }
        else
        {
            it->update(dt);
            ++it;
        }
    }
}

void World::render(sf::RenderTarget& target) const noexcept
{
    target.draw(background);

    for (const auto& log_pair: logs)
    {
        log_pair.render(target);
    }

    target.draw(ground);
}