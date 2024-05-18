/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a pong ball and the declaration
    of the functions to init it, update it, and render it.
*/

#pragma once

#include <src/hitbox.h>

struct Ball
{
    float x;
    float y;
    float width;
    float height;
    float vx;
    float vy;
};

void init_ball(struct Ball* ball, float x, float y, float s);

void build_ball_hitbox(struct Ball ball, struct Hitbox* hitbox);

void update_ball(struct Ball* ball, float dt);

void render_ball(struct Ball ball);
