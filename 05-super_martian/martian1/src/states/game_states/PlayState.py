"""
ISPPV1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class PlayState.
"""

from typing import Dict, Any

import pygame

from gale.state import BaseState

import settings
from src.Camera import Camera
from src.GameLevel import GameLevel


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 1)
        self.game_level = GameLevel(self.level)
        self.tilemap = self.game_level.tilemap
        self.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        self.camera.set_collision_boundaries(self.game_level.get_rect())

    def update(self, dt: float) -> None:
        self.camera.x += dt * 50
        self.camera.update()
        self.game_level.set_render_boundaries(self.camera.get_rect())
        self.game_level.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))
