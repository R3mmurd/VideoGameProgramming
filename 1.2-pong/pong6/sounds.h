/*
    ISPPV1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a struct to load sounds and the
    declaratrion of functions to create them and destroy them.
*/

#pragma once

#include <allegro5/allegro_audio.h>

struct Sounds
{
    ALLEGRO_SAMPLE* paddle_hit;
    ALLEGRO_SAMPLE* wall_hit;
    ALLEGRO_SAMPLE* score;
};

void create_sounds(struct Sounds* sounds);

void destroy_sounds(struct Sounds* sounds);
