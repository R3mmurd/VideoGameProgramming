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
