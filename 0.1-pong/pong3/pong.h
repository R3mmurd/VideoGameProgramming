#include "paddle.h"
#include "ball.h"

enum PongState
{
    START,
    SERVE,
    PLAY,
    DONE
};

struct Pong
{
    struct Paddle player1;
    struct Paddle player2;
    struct Ball ball;

    enum PongState state;
};

void init_pong(struct Pong* pong);

void handle_input_pong(struct Pong* pong, ALLEGRO_KEYBOARD_STATE* state);

void update_pong(struct Pong* pong, double dt);

void render_pong(struct Pong pong, struct Fonts fonts);
