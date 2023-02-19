"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameLevel.
"""
from typing import Any, Dict

import pygame

import settings
from src.Camera import Camera
from src.Creature import Creature
from src.definitions import creatures


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.creatures = []
        self.camera = camera
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level])

    def add_creature(self, creature_data: Dict[str, Any]) -> None:
        definition = creatures.CREATURES[creature_data["tile_index"]]
        self.creatures.append(
            Creature(
                creature_data["x"],
                creature_data["y"],
                creature_data["width"],
                creature_data["height"],
                self,
                **definition,
            )
        )

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())
        for creature in self.creatures:
            creature.update(dt)

        # Remove dead creatures
        self.creatures = [
            creature for creature in self.creatures if not creature.is_dead
        ]

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
        for creature in self.creatures:
            creature.render(surface)
