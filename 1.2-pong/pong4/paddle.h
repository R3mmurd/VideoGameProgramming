/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a pong paddle and the declaration
    of the functions to init it, update it, and render it.
*/

#pragma once

#include "hitbox.h"

struct Paddle
{
    int x;
    int y;
    int width;
    int height;
    int vy;
};

void init_paddle(struct Paddle* paddle, int x, int y, int w, int h);

void build_paddle_hitbox(struct Paddle paddle, struct Hitbox* hitbox);

void update_paddle(struct Paddle* paddle, double dt);

void render_paddle(struct Paddle paddle);
