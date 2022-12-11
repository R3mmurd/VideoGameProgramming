#include <Configuration.hpp>
#include <src/text_utilities.hpp>
#include <src/states/StateMachine.hpp>
#include <src/states/PlayingState.hpp>

PlayingState::PlayingState(StateMachine* sm) noexcept
    : BaseState{sm},
      bird{
          Configuration::VIRTUAL_WIDTH / 2 - Configuration::BIRD_WIDTH / 2, Configuration::VIRTUAL_HEIGHT / 2 - Configuration::BIRD_HEIGHT / 2,
          Configuration::BIRD_WIDTH, Configuration::BIRD_HEIGHT
      },
      world{true}
{

}

void PlayingState::exit() noexcept
{
    world.reset();
}

void PlayingState::handle_inputs(const sf::Event& event) noexcept
{
    if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left)
    {
        bird.jump();
    }
}

void PlayingState::update(float dt) noexcept
{
    bird.update(dt);
    world.update(dt);

    if (world.collides(bird.get_collision_rect()))
    {
        Configuration::sounds["explosion"].play();
        Configuration::sounds["hurt"].play();
        state_machine->change_state("count_down");
    }

    if (world.update_scored(bird.get_collision_rect()))
    {
        ++score;
        Configuration::sounds["score"].play();
    }
}

void PlayingState::render(sf::RenderTarget& target) const noexcept
{
    world.render(target);
    bird.render(target);

    sf::Text score_text = build_text("Score: " + std::to_string(score), Configuration::FLAPPY_TEXT_SIZE, "flappy", sf::Color::White);
    score_text.move(20, 10);
    target.draw(score_text);
}