#pragma once

struct Hitbox
{
    int x1;
    int y1;
    int x2;
    int y2;
};

int collides(struct Hitbox hitbox1, struct Hitbox hitbox2);
