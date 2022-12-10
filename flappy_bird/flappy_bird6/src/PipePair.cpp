#include <Configuration.hpp>
#include <src/PipePair.hpp>

PipePair::PipePair(float _y) noexcept
    : x{Configuration::VIRTUAL_WIDTH}, y{_y},
      top{x, y + Configuration::PIPE_HEIGHT, true},
      bottom{x, y + Configuration::PIPES_GAP + Configuration::PIPE_HEIGHT, false}
{

}

void PipePair::update(float dt) noexcept
{
    x += -Configuration::MAIN_SCROLL_SPEED * dt;

    top.update(x);
    bottom.update(x);
}

void PipePair::render(sf::RenderTarget& target) const noexcept
{
    top.render(target);
    bottom.render(target);
}

bool PipePair::is_out_of_game() const noexcept
{
    return x < -Configuration::PIPE_WIDTH;
}
