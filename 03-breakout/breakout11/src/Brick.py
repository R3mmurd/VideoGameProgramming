"""
ISPPV1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Brick.
"""

import pygame


from gale.particle_system import ParticleSystem

import settings

COLOR_PALETTE = (
    (99, 155, 255),  # blue
    (106, 190, 47),  # green
    (217, 87, 99),  # red
    (215, 123, 186),  # purple
    (251, 242, 54),  # gold
)


class Brick:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 32
        self.height = 16

        self.texture = settings.TEXTURES["spritesheet"]

        self.tier = 0  # [0, 3]
        self.color = 0  # [0, 4]

        # To decide whether render it or not and collision detection
        self.active = True

        self.particle_system = ParticleSystem(self.x + 16, self.y + 8, 64)
        self.particle_system.set_life_time(0.2, 0.4)
        self.particle_system.set_linear_acceleration(-0.3, 0.5, 0.3, 1)
        self.particle_system.set_area_spread(4, 7)

    def hit(self) -> None:
        settings.SOUNDS["brick_hit_2"].stop()
        settings.SOUNDS["brick_hit_2"].play()

        r, g, b = COLOR_PALETTE[self.color]
        self.particle_system.set_colors([(r, g, b, 10), (r, g, b, 50)])
        self.particle_system.generate()

        if self.tier == 0:
            if self.color == 0:
                self.active = False
                settings.SOUNDS["brick_hit_1"].stop()
                settings.SOUNDS["brick_hit_1"].play()
            else:
                self.tier = 3
                self.color -= 1
        else:
            self.tier -= 1

    def score(self):
        return self.tier * 200 + (self.color + 1) * 25

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        self.particle_system.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        if self.active:
            frame = self.color * 4 + self.tier
            surface.blit(
                self.texture, (self.x, self.y), settings.FRAMES["bricks"][frame]
            )
        self.particle_system.render(surface)
