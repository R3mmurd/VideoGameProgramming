/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of functions to create fonts and destroy them.
*/

#include <settings.h>
#include <src/fonts.h>

void create_fonts(struct Fonts* fonts)
{
    fonts->large_font = al_load_ttf_font("assets/fonts/font.ttf", 16, ALLEGRO_TTF_MONOCHROME);
    fonts->score_font = al_load_ttf_font("assets/fonts/font.ttf", 32, ALLEGRO_TTF_MONOCHROME);
}

void destroy_fonts(struct Fonts* fonts)
{
    al_destroy_font(fonts->large_font);
    al_destroy_font(fonts->score_font);
}
