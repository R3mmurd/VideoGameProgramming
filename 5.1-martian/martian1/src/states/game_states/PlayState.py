"""
ISPPV1 2023
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
        self.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        self.game_level = GameLevel(self.level, self.camera)
        self.tilemap = self.game_level.tilemap

    def update(self, dt: float) -> None:
        self.game_level.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))
