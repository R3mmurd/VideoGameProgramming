/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the functions to init a pong ball,
    update it, and render it.
*/

#include <allegro5/allegro_primitives.h>

#include "ball.h"

void init_ball(struct Ball* ball, float x, float y, float s)
{
    ball->x = x;
    ball->y = y;
    ball->width = s;
    ball->height = s;
    ball->vx = 0;
    ball->vy = 0;
}

void update_ball(struct Ball* ball, float dt)
{
    ball->x += ball->vx * dt;
    ball->y += ball->vy * dt;
}

void render_ball(struct Ball ball)
{
    al_draw_filled_rectangle(
        ball.x, ball.y, ball.x + ball.width, ball.y + ball.height, al_map_rgb(255, 255, 255)
    );
}
