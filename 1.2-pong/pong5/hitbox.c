/*
    ISPPV1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the function to determine
    whether two hitboxs collide.
*/

#include "hitbox.h"

int collides(struct Hitbox hitbox1, struct Hitbox hitbox2)
{
    if (hitbox1.x1 > hitbox2.x2 || hitbox2.x1 > hitbox1.x2)
    {
        return 0;
    }

    if (hitbox1.y1 > hitbox2.y2 || hitbox2.y1 > hitbox1.y2)
    {
        return 0;
    }

    return 1;
}
