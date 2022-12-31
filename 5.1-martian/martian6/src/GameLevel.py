"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameLevel.
"""
import pygame

import settings
from src.Camera import Camera
from src.TileMap import TileMap
from src.Creature import Creature
from src.GameItem import GameItem
from src.definitions import creatures, items


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = TileMap(settings.TILEMAPS[f'level{num_level}'])
        self.creatures = []
        self._load_creatures()
        self.items = []
        self._load_items()
        self.camera = camera

    def _load_creatures(self) -> None:
        for creature_tile in self.tilemap.creatures:
            definition = creatures.CREATURES[creature_tile['tile_index']]
            self.creatures.append(
                Creature(
                    creature_tile['x'], creature_tile['y'],
                    creature_tile['width'], creature_tile['height'], self,
                    **definition
                )
            )

    def _load_items(self) -> None:
        for item_tile in self.tilemap.items:
            item_name = item_tile.pop('item_name')
            definition = items.ITEMS[item_name][item_tile['frame_index']]
            definition.update(item_tile)
            self.items.append(GameItem(**definition))

    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())

        for creature in self.creatures:
            creature.update(dt)

        # Remove dead creatures
        self.creatures = [
            creature for creature in self.creatures if not creature.is_dead]

    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
        for creature in self.creatures:
            creature.render(surface)
        for item in self.items:
            if item.in_play:
                item.render(surface)
