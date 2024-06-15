/*
    ISPPJ1 2024
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the main program to run the pong game.
*/

#include <allegro5/allegro5.h>
#include <allegro5/allegro_primitives.h>

#include <settings.h>
#include <src/pong.h>

int main()
{
    al_init();

    al_install_keyboard();
    al_init_primitives_addon();

    ALLEGRO_TIMER* timer = al_create_timer(1.0 / FPS);

    ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();

    ALLEGRO_DISPLAY* display = al_create_display(WINDOW_WIDTH, WINDOW_HEIGHT);

    ALLEGRO_BITMAP* render_surface = al_create_bitmap(TABLE_WIDTH, TABLE_HEIGHT);

    al_register_event_source(queue, al_get_keyboard_event_source());
    al_register_event_source(queue, al_get_display_event_source(display));
    al_register_event_source(queue, al_get_timer_event_source(timer));

    bool redraw = true;
    ALLEGRO_EVENT event;

    al_start_timer(timer);

    struct Pong pong;
    init_pong(&pong);

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

        if (redraw && al_is_event_queue_empty(queue))
        {
            // All of the following draws will be on render_surface
            al_set_target_bitmap(render_surface);
            al_clear_to_color(al_map_rgb(0, 0, 0));
            render_pong(pong);
            
            // Set the display bitmap as current to render
            al_set_target_bitmap(al_get_backbuffer(display));
            
            al_draw_scaled_bitmap(
                render_surface,
                0, 0, TABLE_WIDTH, TABLE_HEIGHT,   // Source x, y, width, height
                0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, // Target x, y, width, height
                0 // flags
            );
            al_flip_display();

            redraw = false;
        }
    }

    al_shutdown_primitives_addon();
    al_destroy_bitmap(render_surface);
    al_destroy_display(display);
    al_destroy_timer(timer);
    al_destroy_event_queue(queue);

    return EXIT_SUCCESS;
}
