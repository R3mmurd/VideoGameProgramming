#include <allegro5/allegro5.h>
#include <allegro5/allegro_primitives.h>

#include "settings.h"
#include "pong.h"

int main()
{
    al_init();

    al_install_keyboard();
    al_init_primitives_addon();

    ALLEGRO_TIMER* timer = al_create_timer(1.0 / FPS);

    ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();

    ALLEGRO_DISPLAY* display = al_create_display(TABLE_WIDTH, TABLE_HEIGHT);

    al_register_event_source(queue, al_get_keyboard_event_source());
    al_register_event_source(queue, al_get_display_event_source(display));
    al_register_event_source(queue, al_get_timer_event_source(timer));

    bool redraw = true;
    ALLEGRO_EVENT event;

    al_start_timer(timer);

    struct Pong pong;
    init_pong(&pong);

    double last_frame_time = al_get_time();

    while (true)
    {
        al_wait_for_event(queue, &event);

        if (event.type == ALLEGRO_EVENT_TIMER)
        {
            redraw = true;
        }
        else if (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE)
        {
            break;
        }
        else if (event.type == ALLEGRO_EVENT_KEY_DOWN || event.type == ALLEGRO_EVENT_KEY_UP)
        {
            ALLEGRO_KEYBOARD_STATE keyboard_state;
            al_get_keyboard_state(&keyboard_state);
            handle_input_pong(&pong, &keyboard_state);
        }

        if (redraw && al_is_event_queue_empty(queue))
        {
            double current_frame_time = al_get_time();
            double dt = current_frame_time - last_frame_time;

            al_clear_to_color(al_map_rgb(0, 0, 0));

            update_pong(&pong, dt);
            render_pong(pong);

            al_flip_display();

            redraw = false;
            last_frame_time = current_frame_time;
        }
    }

    al_shutdown_primitives_addon();
    al_destroy_display(display);
    al_destroy_timer(timer);
    al_destroy_event_queue(queue);

    return EXIT_SUCCESS;
}
