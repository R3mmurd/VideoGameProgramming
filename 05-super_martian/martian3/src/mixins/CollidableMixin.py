"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the CollidableMixin.
"""

from typing import Any

import pygame


class CollidableMixin:
    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())
