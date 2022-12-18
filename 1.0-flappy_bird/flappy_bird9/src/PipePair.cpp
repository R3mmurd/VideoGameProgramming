#include <Settings.hpp>
#include <src/PipePair.hpp>

PipePair::PipePair(float _y) noexcept
    : x{Settings::VIRTUAL_WIDTH}, y{_y},
      top{x, y + Settings::PIPE_HEIGHT, true},
      bottom{x, y + Settings::PIPES_GAP + Settings::PIPE_HEIGHT, false}
{

}

bool PipePair::collides(const sf::FloatRect& rect) const noexcept
{
    return top.get_collision_rect().intersects(rect) || bottom.get_collision_rect().intersects(rect);
}

void PipePair::update(float dt) noexcept
{
    x += -Settings::MAIN_SCROLL_SPEED * dt;

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
    return x < -Settings::PIPE_WIDTH;
}

bool PipePair::update_scored(const sf::FloatRect& rect) noexcept
{
    if (scored)
    {
        return false;
    }

    if (rect.left > x + Settings::PIPE_WIDTH)
    {
        scored = true;
        return true;
    }

    return false;
}
