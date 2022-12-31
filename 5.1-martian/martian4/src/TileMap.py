"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class TileMap.
"""
import xml.etree.ElementTree as ET
from typing import List, Tuple, Dict

import pygame

from src import mixins
from src.Tile import Tile
from src.definitions import tiles


class TileMap:
    def __init__(self, filename: str) -> None:
        self.creatures: List[Dict[str, int]] = []
        self.layers: List[List[List[Tile]]] = []
        self.rows = 0
        self.cols = 0
        self.tilewidth = 0
        self.tileheight = 0
        self._load(filename)
        self.width = self.cols * self.tilewidth
        self.height = self.rows * self.tileheight
        self.render_rows_range = (0, self.rows)
        self.render_cols_range = (0, self.cols)

    def _load(self, filename: str) -> None:
        tree = ET.parse(filename)
        root = tree.getroot()

        self.rows = int(root.attrib['height'])
        self.cols = int(root.attrib['width'])
        self.tilewidth = int(root.attrib['tilewidth'])
        self.tileheight = int(root.attrib['tileheight'])

        for child in root.findall('layer'):
            data = [s for s in child.find(
                'data').text.split('\n') if len(s) > 0]

            if child.attrib['name'] == "creatures":
                for i in range(self.rows):
                    line = [s for s in data[i].split(',') if len(s) > 0]
                    for j in range(self.cols):
                        value = int(line[j])

                        if value == 0:
                            continue

                        self.creatures.append({
                            'tile_index': value - 1,
                            'x': j * self.tilewidth,
                            'y': i * self.tileheight,
                            'width': self.tilewidth,
                            'height': self.tileheight
                        })
            else:
                layer: List[List[Tile]] = [
                    [None for _ in range(self.cols)] for _ in range(self.rows)]

                for i in range(self.rows):
                    line = [s for s in data[i].split(',') if len(s) > 0]
                    for j in range(self.cols):
                        frame_index = int(line[j]) - 1
                        tile_def = tiles.TILES.get(frame_index)
                        solidness = tile_def['solidness'] if tile_def is not None else Tile.DEFAULT_SOLIDNESS
                        layer[i][j] = Tile(
                            i, j, self.tilewidth, self.tileheight, frame_index, solidness)

                self.layers.append(layer)

    def set_render_boundaries(self, render_rect: pygame.Rect) -> None:
        self.render_rows_range = (
            max(render_rect.y // self.tileheight, 0),
            min(render_rect.bottom // self.tileheight + 1, self.rows)
        )
        self.render_cols_range = (
            max(render_rect.x // self.tilewidth, 0),
            min(render_rect.right // self.tilewidth + 1, self.cols)
        )

    def to_x(self, j: int) -> int:
        return j * self.tilewidth

    def to_y(self, i: int) -> int:
        return i * self.tileheight

    def to_i(self, y: int) -> int:
        return y // self.tileheight

    def to_j(self, x: int) -> int:
        return x // self.tilewidth

    def to_screen(self, i: int, j: int) -> Tuple[int, int]:
        return self.to_x(j), self.to_y(i)

    def to_tilemap(self, x: int, y: int) -> Tuple[int, int]:
        return self.to_i(y), self.to_j(x)

    def render(self, surface: pygame.Surface) -> None:
        for layer in self.layers:
            for i in range(*self.render_rows_range):
                for j in range(*self.render_cols_range):
                    layer[i][j].render(surface)

    def collides_tile_on(
            self,
            i: int,
            j: int,
            another: mixins.CollidableMixin,
            side: str) -> bool:
        if 0 <= i < self.rows and 0 <= j < self.cols:
            for layer in self.layers:
                if layer[i][j].collides_on(another, side):
                    return True
        return False

    def check_solidness(self, i: int, j: int, side: str) -> bool:
        if 0 <= i < self.rows and 0 <= j < self.cols:
            for layer in self.layers:
                if layer[i][j].solidness[side]:
                    return True
        return False
