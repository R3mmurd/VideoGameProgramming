#pragma once

#include <src/Bird.hpp>
#include <src/World.hpp>
#include <src/states/BaseState.hpp>

class PlayingState: public BaseState
{

public:
    PlayingState(StateMachine* sm) noexcept;

    void handle_inputs(const sf::Event& event) noexcept override;

    void exit() noexcept override;

    void update(float dt) noexcept override;

    void render(sf::RenderTarget& target) const noexcept override;

private:
    Bird bird;
    World world;
    int score{0};
};
