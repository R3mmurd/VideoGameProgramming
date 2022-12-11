#include <allegro5/allegro_primitives.h>

#include "configuration.h"
#include "pong.h"

void init_pong(struct Pong* pong)
{
    init_paddle(&pong->player1, PADDLE_X_OFFSET, PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT);
    init_paddle(&pong->player2, TABLE_WIDTH - PADDLE_WIDTH - PADDLE_X_OFFSET, TABLE_HEIGHT - PADDLE_HEIGHT - PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT);
    init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);
}

void update_pong(struct Pong* pong, double dt)
{

}

void render_pong(struct Pong pong)
{
    al_draw_filled_rectangle(
        TABLE_WIDTH / 2 - MID_LINE_WIDTH / 2, 0,
        TABLE_WIDTH / 2 + MID_LINE_WIDTH / 2, TABLE_HEIGHT,
        al_map_rgb(255, 255, 255)
    );
    render_paddle(pong.player1);
    render_paddle(pong.player2);
    render_ball(pong.ball);
}
