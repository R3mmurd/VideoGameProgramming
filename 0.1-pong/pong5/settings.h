#pragma once

#ifndef MIN
#define MIN(a, b) ((a < b) ? a : b)
#endif

#ifndef MAX
#define MAX(a, b) ((a > b) ? a : b)
#endif

#define SCALE 3
#define TABLE_WIDTH 432 * SCALE
#define TABLE_HEIGHT 243 * SCALE
#define PADDLE_WIDTH 5 * SCALE
#define PADDLE_HEIGHT 30 * SCALE
#define PADDLE_X_OFFSET 10 * SCALE
#define PADDLE_Y_OFFSET 30 * SCALE
#define PADDLE_SPEED 200 * SCALE
#define BALL_SIZE 4 * SCALE
#define MID_LINE_WIDTH 2 * SCALE
#define FPS 60.0
#define MAX_POINTS 5

