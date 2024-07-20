"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Tilemap.
"""

import xml.etree.ElementTree as ET
from typing import List, Tuple

import pygame

from src.Tile import Tile


class Tilemap:
    def __init__(self, rows, cols, tilewidth, tileheight) -> None:
        self.layers: List[List[List[Tile]]] = []
        self.rows = rows
        self.cols = cols
        self.tilewidth = tilewidth
        self.tileheight = tileheight

    def create_layer(self) -> None:
        layer = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.layers.append(layer)

    def set_new_tile(self, i: int, j: int, frame_index: int) -> None:
        """
        Set a new tile in the position (i, j) of the current (the last added) layer
        """
        self.layers[-1][i][j] = Tile(i, j, self.tilewidth, self.tileheight, frame_index)

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
            for row in layer:
                for tile in row:
                    tile.render(surface)
