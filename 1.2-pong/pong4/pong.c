/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the functions to init a pong game,
    update it, and render it.
*/

#include <allegro5/allegro_primitives.h>

#include "settings.h"
#include "fonts.h"
#include "pong.h"

void init_pong(struct Pong* pong)
{
    init_paddle(&pong->player1, PADDLE_X_OFFSET, PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT);
    init_paddle(&pong->player2, TABLE_WIDTH - PADDLE_WIDTH - PADDLE_X_OFFSET, TABLE_HEIGHT - PADDLE_HEIGHT - PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT);
    init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);
    pong->state = START;
    srand(time(NULL));
}

void handle_input_pong(struct Pong* pong, ALLEGRO_KEYBOARD_STATE* state)
{
    if (pong->state == START)
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            pong->state = SERVE;
        }
    }
    else if (pong->state == SERVE)
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            pong->state = PLAY;

            pong->ball.vx = rand() % 120 + 480;

            if (rand() % 2 == 0)
            {
                pong->ball.vx *= -1;
            }

            pong->ball.vy = rand() % 400 - 200;
        }
    }
    else if (pong->state == PLAY)
    {
        if (al_key_down(state, ALLEGRO_KEY_S))
        {
            pong->player1.vy = PADDLE_SPEED;
        }
        else if (al_key_down(state, ALLEGRO_KEY_W))
        {
            pong->player1.vy = -PADDLE_SPEED;
        }
        else
        {
            pong->player1.vy = 0;
        }

        if (al_key_down(state, ALLEGRO_KEY_DOWN))
        {
            pong->player2.vy = PADDLE_SPEED;
        }
        else if (al_key_down(state, ALLEGRO_KEY_UP))
        {
            pong->player2.vy = -PADDLE_SPEED;
        }
        else
        {
            pong->player2.vy = 0;
        }
    }
    else
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            init_pong(pong);
            pong->state = SERVE;
        }
    }
}

void update_pong(struct Pong* pong, double dt)
{
    if (pong->state == PLAY)
    {
        update_paddle(&pong->player1, dt);
        update_paddle(&pong->player2, dt);
        update_ball(&pong->ball, dt);

        struct Hitbox ball_hitbox;
        build_ball_hitbox(pong->ball, &ball_hitbox);

        struct Hitbox player1_hitbox;
        build_paddle_hitbox(pong->player1, &player1_hitbox);

        struct Hitbox player2_hitbox;
        build_paddle_hitbox(pong->player2, &player2_hitbox);

        if (ball_hitbox.y1 <= 0)
        {
            pong->ball.y = 0;
            pong->ball.vy *= -1;
        }
        else if (ball_hitbox.y2 >= TABLE_HEIGHT)
        {
            pong->ball.y = TABLE_HEIGHT - pong->ball.height;
            pong->ball.vy *= -1;
        }
        
        if (collides(ball_hitbox, player1_hitbox))
        {
            pong->ball.x = player1_hitbox.x2;
            pong->ball.vx *= -1.03;

            if (pong->ball.vy < 0)
            {
                pong->ball.vy = -(rand() % 200 + 200);
            }
            else
            {
                pong->ball.vy = rand() % 200 + 200;
            }
        }
        else if (collides(ball_hitbox, player2_hitbox))
        {
            pong->ball.x = player2_hitbox.x1 - pong->ball.width;
            pong->ball.vx *= -1.03;

            if (pong->ball.vy < 0)
            {
                pong->ball.vy = -(rand() % 140 + 50);
            }
            else
            {
                pong->ball.vy = rand() % 140 + 50;
            }
        }
    }
}

void render_pong(struct Pong pong, struct Fonts fonts)
{
    al_draw_filled_rectangle(
        TABLE_WIDTH / 2 - MID_LINE_WIDTH / 2, 0,
        TABLE_WIDTH / 2 + MID_LINE_WIDTH / 2, TABLE_HEIGHT,
        al_map_rgb(255, 255, 255)
    );
    render_paddle(pong.player1);
    render_paddle(pong.player2);
    render_ball(pong.ball);

    if (pong.state == START)
    {
        al_draw_text(fonts.large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 3, ALLEGRO_ALIGN_CENTER, "Press enter to start");
    }
    else if (pong.state == SERVE)
    {
        al_draw_text(fonts.large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 3, ALLEGRO_ALIGN_CENTER, "Press enter to serve");
    }
}
