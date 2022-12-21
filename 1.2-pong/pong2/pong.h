#include "paddle.h"
#include "ball.h"

struct Pong
{
    struct Paddle player1;
    struct Paddle player2;
    struct Ball ball;
};

void handle_input_pong(struct Pong* pong, ALLEGRO_KEYBOARD_STATE* state);

void init_pong(struct Pong* pong);

void update_pong(struct Pong* pong, double dt);

void render_pong(struct Pong pong);
