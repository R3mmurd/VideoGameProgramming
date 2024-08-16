"""
ISPPV1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Brick.
"""

import pygame

import settings


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

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, surface: pygame.Surface) -> None:
        if self.active:
            frame = self.color * 4 + self.tier
            surface.blit(
                self.texture, (self.x, self.y), settings.FRAMES["bricks"][frame]
            )
