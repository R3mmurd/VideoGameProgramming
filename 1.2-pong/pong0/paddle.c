#include <allegro5/allegro_primitives.h>

#include "paddle.h"

void init_paddle(struct Paddle* paddle, int x, int y, int w, int h)
{
    paddle->x = x;
    paddle->y = y;
    paddle->width = w;
    paddle->height = h;
    paddle->vy = 0;
}

void update_paddle(struct Paddle* paddle, double dt)
{

}

void render_paddle(struct Paddle paddle)
{
    al_draw_filled_rectangle(
        paddle.x, paddle.y, paddle.x + paddle.width, paddle.y + paddle.height,
        al_map_rgb(255, 255, 255)
    );
}
