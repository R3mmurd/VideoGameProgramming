/*
    ISPPJ1 2024
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of some macros with values to set the pong game.
*/

#pragma once

#ifndef MIN
#define MIN(a, b) ((a < b) ? a : b)
#endif

#ifndef MAX
#define MAX(a, b) ((a > b) ? a : b)
#endif

#define WINDOW_WIDTH 1280
#define WINDOW_HEIGHT 720
#define TABLE_WIDTH 432
#define TABLE_HEIGHT 243
#define PADDLE_WIDTH 5
#define PADDLE_HEIGHT 20
#define PADDLE_X_OFFSET 10
#define PADDLE_Y_OFFSET 30
#define PADDLE_SPEED 200
#define BALL_SIZE 4
#define MID_LINE_WIDTH 2
#define FPS 60.0

