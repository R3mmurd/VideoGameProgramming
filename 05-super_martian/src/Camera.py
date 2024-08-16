"""
ISPPV1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Camera.
"""

import pygame

from src.GameEntity import GameEntity


class Camera:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision_boundaries = None
        self.following = None

    def attach_to(self, entity: GameEntity) -> None:
        self.following = entity

    def set_collision_boundaries(self, rect: pygame.Rect) -> None:
        self.collision_boundaries = rect

    def update(self) -> None:
        if self.following is not None:
            self.x = self.following.x + self.following.width // 2 - self.width // 2
            self.y = self.following.y + self.following.height // 2 - self.height // 2

        if self.collision_boundaries is not None:
            self.x = max(
                self.collision_boundaries.x,
                min(
                    self.x,
                    self.collision_boundaries.x
                    + self.collision_boundaries.width
                    - self.width,
                ),
            )
            self.y = max(
                self.collision_boundaries.y,
                min(
                    self.y,
                    self.collision_boundaries.y
                    + self.collision_boundaries.height
                    - self.height,
                ),
            )

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
