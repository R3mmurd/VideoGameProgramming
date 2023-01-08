/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the functions to init a pong paddle,
    update it, and render it.
*/

#include <allegro5/allegro_primitives.h>

#include "paddle.h"

void init_paddle(struct Paddle* paddle, float x, float y, float w, float h)
{
    paddle->x = x;
    paddle->y = y;
    paddle->width = w;
    paddle->height = h;
    paddle->vy = 0;
}

void update_paddle(struct Paddle* paddle, float dt)
{
    paddle->y += paddle->vy * dt;
}

void render_paddle(struct Paddle paddle)
{
    al_draw_filled_rectangle(
        paddle.x, paddle.y, paddle.x + paddle.width, paddle.y + paddle.height,
        al_map_rgb(255, 255, 255)
    );
}
