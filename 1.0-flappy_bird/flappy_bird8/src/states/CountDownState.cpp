#include <cmath>

#include <Configuration.hpp>
#include <src/states/CountDownState.hpp>
#include <src/states/StateMachine.hpp>

CountDownState::CountDownState(StateMachine* sm) noexcept
    : BaseState{sm}, world{}
{

}

void CountDownState::update(float dt) noexcept
{
    timer += dt;

    if (timer >= 1.f)
    {
        timer = 0.f;
        --counter;

        if (counter == 0)
        {
            state_machine->change_state("playing");
        }
    }

    world.update(dt);
}

void CountDownState::render(sf::RenderTarget& target) const noexcept
{
    world.render(target);

    sf::Text text;
    text.setFont(Configuration::fonts["font"]);
    text.setString(std::to_string(counter));
    text.setCharacterSize(Configuration::HUGE_TEXT_SIZE);
    text.setFillColor(sf::Color::White);
    float center_x = text.getGlobalBounds().width / 2.f;
    float center_y = text.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + text.getLocalBounds().left);
    float local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(sf::Vector2f{Configuration::VIRTUAL_WIDTH / 2, Configuration::VIRTUAL_HEIGHT / 2});
    
    target.draw(text);
}