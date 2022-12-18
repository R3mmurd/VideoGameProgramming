#include <cmath>

#include <Settings.hpp>
#include <src/text_utilities.hpp>

void center_text(sf::Text& text) noexcept
{
    float center_x = text.getGlobalBounds().width / 2.f;
    float center_y = text.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + text.getLocalBounds().left);
    float local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(sf::Vector2f{Settings::VIRTUAL_WIDTH / 2, Settings::VIRTUAL_HEIGHT / 2});
}

sf::Text build_text(const std::string& text_str, int size, const std::string& font_name, const sf::Color& color, bool center) noexcept
{
    sf::Text text;
    text.setFont(Settings::fonts[font_name]);
    text.setString(text_str);
    text.setCharacterSize(size);
    text.setFillColor(color);
    if (center)
    {
        center_text(text);
    }
    return text;
}
