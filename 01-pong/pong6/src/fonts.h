/*
    ISPPV1 2024
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a struct to load fonts and the
    declaratrion of functions to create them and destroy them.
*/

#pragma once

#include <allegro5/allegro_ttf.h>

struct Fonts
{
    ALLEGRO_FONT* large_font;
    ALLEGRO_FONT* score_font;
};

void create_fonts(struct Fonts* fonts);

void destroy_fonts(struct Fonts* fonts);
