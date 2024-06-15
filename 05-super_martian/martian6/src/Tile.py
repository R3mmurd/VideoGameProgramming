"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the base class Tile.
"""

from typing import Dict

from src.GameObject import GameObject


class Tile(GameObject):
    def __init__(
        self,
        i: int,
        j: int,
        width: int,
        height: int,
        frame_index: int,
        soliness: Dict[str, bool],
    ) -> None:
        self.i = i
        self.j = j
        super().__init__(
            self.j * width,
            self.i * height,
            width,
            height,
            "tiles",
            frame_index,
            soliness,
        )
