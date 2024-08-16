/*
    ISPPV1 2024
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a hitbox and a function to determine
    whether two hitboxs collide.
*/

#pragma once

struct Hitbox
{
    float x1;
    float y1;
    float x2;
    float y2;
};

int collides(struct Hitbox hitbox1, struct Hitbox hitbox2);
