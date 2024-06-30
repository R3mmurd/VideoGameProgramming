from typing import Dict, Optional, Tuple

import pygame

from src.Brick import Brick


class Brickset:
    def __init__(self, x: float, y: float, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        width = self.cols * 32
        height = self.rows * 16
        self.collision_rect = pygame.Rect(x, y, width, height)
        self.bricks: Dict[Tuple[int, int], Brick] = {}
        self.size = 0

    def get_collision_rect(self) -> pygame.Rect:
        return self.collision_rect

    def add_brick(self, i: int, j: int, brick: Brick) -> None:
        self.bricks[(i, j)] = brick
        self.size += 1

    def get_brick(self, i: int, j: int) -> Optional[Brick]:
        return self.bricks.get((i, j))

    def __del_brick(self, pos: Tuple[int, int]) -> None:
        self.bricks.pop(pos)
        self.size -= 1

    def get_colliding_brick(self, r: pygame.Rect) -> Optional[Brick]:
        top_row = (r.top - self.collision_rect.y) // 16
        bottom_row = (r.bottom - self.collision_rect.y) // 16
        left_col = (r.left - self.collision_rect.x) // 32
        right_col = (r.right - self.collision_rect.x) // 32

        # check top-left
        brick = self.get_brick(top_row, left_col)
        if brick is not None and not brick.broken:
            return brick

        # check top-right
        brick = self.get_brick(top_row, right_col)
        if brick is not None and not brick.broken:
            return brick

        # check bottom-left
        brick = self.get_brick(bottom_row, left_col)
        if brick is not None and not brick.broken:
            return brick

        # return top-right
        brick = self.get_brick(bottom_row, left_col)
        if brick is not None and not brick.broken:
            return brick

        return None

    def update(self, dt: float) -> None:
        to_del = []
        for pos, brick in self.bricks.items():
            brick.update(dt)
            if not brick.active:
                to_del.append(pos)

        for pos in to_del:
            self.__del_brick(pos)

    def render(self, surface: pygame.Surface) -> None:
        for brick in self.bricks.values():
            brick.render(surface)
