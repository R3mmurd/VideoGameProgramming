#pragma once

#include <string>

#include <SFML/Graphics.hpp>

void center_text(sf::Text& text) noexcept;

sf::Text build_text(const std::string& text_str, int size, const std::string& font_name, const sf::Color& color, bool center = false) noexcept;
