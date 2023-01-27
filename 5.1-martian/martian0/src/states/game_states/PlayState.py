"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class PlayState.
"""
from typing import Dict, Any

import pygame

from gale.state_machine import BaseState

import settings
from src.TileMap import TileMap


class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 1)
        self.tilemap = TileMap(settings.TILEMAPS[f"level{self.level}"])

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
