/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a pong ball and the declaration
    of the functions to init it, update it, and render it.
*/

#pragma once

struct Ball
{
    int x;
    int y;
    int width;
    int height;
    int vx;
    int vy;
};

void init_ball(struct Ball* ball, int x, int y, int s);

void update_ball(struct Ball* ball, double dt);

void render_ball(struct Ball ball);
