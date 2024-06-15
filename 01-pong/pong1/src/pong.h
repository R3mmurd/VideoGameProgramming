/*
    ISPPJ1 2024
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a pong game and the declaration
    of the functions to init it, update it, and render it.
*/

#include <src/paddle.h>
#include <src/ball.h>

struct Pong
{
    struct Paddle player1;
    struct Paddle player2;
    struct Ball ball;
};

void init_pong(struct Pong* pong);

void update_pong(struct Pong* pong, double dt);

void render_pong(struct Pong pong);
