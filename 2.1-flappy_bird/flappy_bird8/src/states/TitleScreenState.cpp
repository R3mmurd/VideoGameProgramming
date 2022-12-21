#include <cmath>

#include <Settings.hpp>
#include <src/states/StateMachine.hpp>
#include <src/states/TitleScreenState.hpp>

TitleScreenState::TitleScreenState(StateMachine* sm) noexcept
    : BaseState{sm}, world{}
{

}

void TitleScreenState::handle_inputs(const sf::Event& event) noexcept
{
    if (event.key.code == sf::Keyboard::Enter)
    {
        state_machine->change_state("count_down");
    }
}

void TitleScreenState::update(float dt) noexcept
{
    world.update(dt);
}

void TitleScreenState::render(sf::RenderTarget& target) const noexcept 
{
    world.render(target);

    sf::Text text;
    text.setFont(Settings::fonts["font"]);
    text.setString("Press enter to start");
    text.setCharacterSize(Settings::MEDIUM_TEXT_SIZE);
    text.setFillColor(sf::Color::White);
    float center_x = text.getGlobalBounds().width / 2.f;
    float center_y = text.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + text.getLocalBounds().left);
    float local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(sf::Vector2f{Settings::VIRTUAL_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2});
    
    target.draw(text);
}