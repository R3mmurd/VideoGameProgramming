"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameLevel.
"""

import pygame

import settings


class GameLevel:
    def __init__(self, num_level: int) -> None:
        self.tilemap = None
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level])

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(0, 0, self.tilemap.width, self.tilemap.height)

    def set_render_boundaries(self, rect: pygame.Rect) -> None:
        self.tilemap.set_render_boundaries(rect)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
