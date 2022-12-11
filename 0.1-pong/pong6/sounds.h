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
