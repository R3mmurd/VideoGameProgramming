/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of a hitbox and a function to determine
    whether two hitboxs collide.
*/

#pragma once

struct Hitbox
{
    int x1;
    int y1;
    int x2;
    int y2;
};

int collides(struct Hitbox hitbox1, struct Hitbox hitbox2);
