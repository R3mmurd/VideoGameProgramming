#include <assert.h>

#include "sounds.h"

void create_sounds(struct Sounds* sounds)
{
    sounds->paddle_hit = al_load_sample("sounds/paddle_hit.wav");
    sounds->wall_hit = al_load_sample("sounds/wall_hit.wav");
    sounds->score = al_load_sample("sounds/score.wav");
    al_reserve_samples(3);

    assert(sounds->paddle_hit != NULL);
    assert(sounds->wall_hit != NULL);
    assert(sounds->score != NULL);
}

void destroy_sounds(struct Sounds* sounds)
{
    al_destroy_sample(sounds->paddle_hit);
    al_destroy_sample(sounds->wall_hit);
    al_destroy_sample(sounds->score);
}
