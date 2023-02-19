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
from src.Tilemap import Tilemap
from src.Creature import Creature
from src.GameItem import GameItem
from src.definitions import creatures, items


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = None
        self.creatures = []
        self.items = []
        self.camera = camera
        settings.LevelLoader().load(self, settings.TILEMAPS[num_level])

    def add_item(self, item_data: Dict[str, Any]) -> None:
        item_name = item_data.pop("item_name")
        definition = items.ITEMS[item_name][item_data["frame_index"]]
        definition.update(item_data)
        self.items.append(GameItem(**definition))

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
        for item in self.items:
            if item.in_play:
                item.render(surface)
