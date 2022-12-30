/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of utility functions to build texts.
*/

#pragma once

#include <string>

#include <SFML/Graphics.hpp>

void center_text(sf::Text& text) noexcept;

sf::Text build_text(const std::string& text_str, int size, const std::string& font_name, const sf::Color& color, bool center = false) noexcept;
