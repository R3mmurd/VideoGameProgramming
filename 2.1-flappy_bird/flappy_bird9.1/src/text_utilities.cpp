/*
    ISPPV1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of utility functions to build texts.
*/

#include <cmath>

#include <Settings.hpp>
#include <src/text_utilities.hpp>

void center_text(sf::Text& text) noexcept
{
    sf::Vector2f pos = text.getPosition();
    float center_x = text.getGlobalBounds().width / 2.f;
    float center_y = text.getGlobalBounds().height / 2.f;
    float local_center_x = round(center_x + text.getLocalBounds().left);
    float local_center_y = round(center_y + text.getLocalBounds().top);
    text.setOrigin(sf::Vector2f{local_center_x, local_center_y});
    text.setPosition(pos);
}

void render_text(sf::RenderTarget& target, float x, float y, const std::string& text_str, int size, const std::string& font_name, const sf::Color& color, bool center) noexcept
{
    sf::Text text;
    text.setFont(Settings::fonts[font_name]);
    text.setString(text_str);
    text.setCharacterSize(size);
    text.setFillColor(sf::Color::Black);
    text.move(x + 2, y + 2);
    if (center)
    {
        center_text(text);
    }
    target.draw(text);
    text.setFillColor(sf::Color::White);
    text.move(-2, -2);
    target.draw(text);
}
