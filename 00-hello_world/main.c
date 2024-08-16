/*
    ISPPV1 2024
    Hello World

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains an example of using Allegro to setup a window
    and draw the text "Hello World" in the center.
*/

#include <allegro5/allegro5.h>
#include <allegro5/allegro_font.h>

#define FPS 60.0

int main()
{
    //---------------------- Initialization ------------------------------//
    // Set up the bits of Allegro that are necessary to display the window
    al_init();

    // Enable keyboard input.
    al_install_keyboard();

    // Timer to ensure the game runs at a consistent speed.
    ALLEGRO_TIMER* timer = al_create_timer(1 / FPS);

    // Event queue to register the game events.
    ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();

    // Create a 320x200 pixel window
    ALLEGRO_DISPLAY* display = al_create_display(320, 200);

    // Build a built-in pixel font that comes with the library by default.
    ALLEGRO_FONT* font = al_create_builtin_font();

    // Tell Allegro that we are interested in reacting to keyboard, display, and timer events.
    al_register_event_source(queue, al_get_keyboard_event_source());
    al_register_event_source(queue, al_get_display_event_source(display));
    al_register_event_source(queue, al_get_timer_event_source(timer));

    //---------------------- The Main Loop ------------------------------//
    bool redraw = true;
    ALLEGRO_EVENT event;

    al_start_timer(timer);

    while (true)
    {
        al_wait_for_event(queue, &event);

        if (event.type == ALLEGRO_EVENT_TIMER)
        {
            redraw = true;
        }
        else if (event.type == ALLEGRO_EVENT_KEY_DOWN || event.type == ALLEGRO_EVENT_DISPLAY_CLOSE)
        {
            break;
        }

        if (redraw && al_is_event_queue_empty(queue))
        {
            // Clear the screen to black
            al_clear_to_color(al_map_rgb(0, 0, 0));

            // Draw Hello world!
            al_draw_text(font, al_map_rgb(255, 255, 255), 160, 100, ALLEGRO_ALIGN_CENTER, "Hello world!");

            // Commit the result.
            al_flip_display();

            redraw = false;
        }
    }

    //---------------------- Shutdown ------------------------------//
    al_destroy_font(font);
    al_destroy_display(display);
    al_destroy_timer(timer);
    al_destroy_event_queue(queue);

    return EXIT_SUCCESS;
}