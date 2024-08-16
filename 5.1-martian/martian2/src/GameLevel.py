"""
ISPPV1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameLevel.
"""
import pygame

import settings
from src.Camera import Camera


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.camera = camera
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level])

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
