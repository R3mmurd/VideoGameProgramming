"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the base class GameEntity.
"""

from typing import TypeVar, Dict, Any, Tuple

from gale.state import StateMachine, BaseState

from src import mixins
from src.GameObject import GameObject


class GameEntity(mixins.DrawableMixin, mixins.AnimatedMixin, mixins.CollidableMixin):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        texture_id: str,
        game_level: TypeVar("GameLevel"),
        states: Dict[str, BaseState],
        animation_defs: Dict[str, Dict[str, Any]],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx: float = 0
        self.vy: float = 0
        self.texture_id = texture_id
        self.frame_index = -1
        self.game_level = game_level
        self.tilemap = self.game_level.tilemap
        self.state_machine = StateMachine(states)
        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
        self.flipped = False
        self.is_dead = False

    def change_state(
        self, state_id: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        mixins.AnimatedMixin.update(self, dt)
        self.y += self.vy * dt

        next_x = self.x + self.vx * dt

        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(self.tilemap.width - self.width, next_x)

    def handle_tilemap_collision_on_top(self) -> bool:
        collision_rect = self.get_collision_rect()

        # Row for the center of the player
        i = self.tilemap.to_i(collision_rect.centery)

        # Left and right columns
        left = self.tilemap.to_j(collision_rect.left)
        right = self.tilemap.to_j(collision_rect.right)

        if self.tilemap.collides_tile_on(
            i - 1, left, self, GameObject.BOTTOM
        ) or self.tilemap.collides_tile_on(i - 1, right, self, GameObject.BOTTOM):
            # Fix the entity position
            self.y = self.tilemap.to_y(i)
            return True

        return False

    def handle_tilemap_collision_on_bottom(self) -> bool:
        collision_rect = self.get_collision_rect()

        # Row for the center of the player
        i = self.tilemap.to_i(collision_rect.centery)

        # Left and right columns
        left = self.tilemap.to_j(collision_rect.left)
        right = self.tilemap.to_j(collision_rect.right)

        if self.tilemap.collides_tile_on(
            i + 1, left, self, GameObject.TOP
        ) or self.tilemap.collides_tile_on(i + 1, right, self, GameObject.TOP):
            # Fix the entity position
            self.y = self.tilemap.to_y(i + 1) - self.height
            return True

        return False

    def handle_tilemap_collision_on_right(self) -> bool:
        collision_rect = self.get_collision_rect()

        # Column for the center of the player
        j = self.tilemap.to_j(collision_rect.centerx)
        # Top and bottom Rows
        top = self.tilemap.to_i(collision_rect.top)
        center = self.tilemap.to_i(collision_rect.centery)

        if self.tilemap.collides_tile_on(
            top, j + 1, self, GameObject.LEFT
        ) or self.tilemap.collides_tile_on(center, j + 1, self, GameObject.LEFT):
            # Fix the entity position
            self.x = self.tilemap.to_x(j + 1) - self.width
            return True

        return False

    def handle_tilemap_collision_on_left(self) -> bool:
        collision_rect = self.get_collision_rect()

        # Column for the center of the player
        j = self.tilemap.to_j(collision_rect.centerx)
        # Top and bottom Rows
        top = self.tilemap.to_i(collision_rect.top)
        center = self.tilemap.to_i(collision_rect.centery)

        if self.tilemap.collides_tile_on(
            top, j - 1, self, GameObject.RIGHT
        ) or self.tilemap.collides_tile_on(center, j - 1, self, GameObject.RIGHT):
            # Fix the entity position
            self.x = self.tilemap.to_x(j)
            return True

        return False

    def check_floor(self) -> bool:
        """
        Check whether the entity is on a solid tile.
        """
        collision_rect = self.get_collision_rect()

        # Row for the center of the player
        i = self.tilemap.to_i(collision_rect.centery)
        # Left and right columns
        left = self.tilemap.to_j(collision_rect.left)
        right = self.tilemap.to_j(collision_rect.right)
        return self.tilemap.check_solidness_on(
            i + 1, left, GameObject.TOP
        ) or self.tilemap.check_solidness_on(i + 1, right, GameObject.TOP)
