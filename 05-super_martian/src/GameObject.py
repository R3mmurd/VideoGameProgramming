"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the base class GameObject.
"""

from typing import Dict

from src import mixins


class GameObject(mixins.DrawableMixin, mixins.CollidableMixin):
    # Object sides
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"

    DEFAULT_SOLIDNESS = {TOP: False, RIGHT: False, BOTTOM: False, LEFT: False}

    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        texture_id: str,
        frame_index: int,
        solidness: Dict[str, bool],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture_id = texture_id
        self.frame_index = frame_index
        self.solidness = solidness
        self.flipped = False

    def collides_on(self, another: mixins.CollidableMixin, side: str) -> bool:
        return self.is_solid_on(side) and self.collides(another)

    def is_solid_on(self, side: str) -> bool:
        return self.solidness[side]
