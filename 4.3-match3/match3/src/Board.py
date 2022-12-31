"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Board.
"""
from typing import List, Optional, Tuple, Any, Dict

import pygame

import random

import settings
from src.Tile import Tile


class Board:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.matches: List[List[Tile]] = []
        self.tiles: List[List[Tile]] = []
        self._initialize_tiles()

    def render(self, surface: pygame.Surface) -> None:
        for row in self.tiles:
            for tile in row:
                tile.render(surface, self.x, self.y)

    def _is_match_generated(self, i: int, j: int, color: int) -> bool:
        if i >= 2 and self.tiles[i -
                                 1][j].color == color and self.tiles[i -
                                                                     2][j].color:
            return True

        return j >= 2 and self.tiles[i][j -
                                        1].color == color and self.tiles[i][j -
                                                                            2].color

    def _initialize_tiles(self) -> None:
        self.tiles = [[None for _ in range(settings.BOARD_WIDTH)] for _ in range(
            settings.BOARD_HEIGHT)]
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                color = random.randint(0, settings.NUM_COLORS - 1)
                while self._is_match_generated(i, j, color):
                    color = random.randint(0, settings.NUM_COLORS - 1)

                self.tiles[i][j] = Tile(
                    i, j, color, random.randint(
                        0, settings.NUM_VARIETIES - 1))

        assert (not self.calculate_matches())

    def calculate_matches(self) -> Optional[List[List[Tile]]]:
        match_num: int

        # Horizontal matches
        for y in range(settings.BOARD_HEIGHT):
            color_to_match = self.tiles[y][0].color

            match_num = 1

            for x in range(1, settings.BOARD_WIDTH):
                if self.tiles[y][x].color == color_to_match:
                    match_num += 1
                else:
                    color_to_match = self.tiles[y][x].color

                    if match_num >= 3:
                        match: List[Tile] = []

                        for x2 in range(x - 1, x - match_num - 1, -1):
                            match.append(self.tiles[y][x2])

                        self.matches.append(match)

                    # We don't need to check last two if they won't be in a
                    # match
                    if x >= settings.BOARD_WIDTH - 2:
                        break

                    match_num = 1

            # account for the last row ending with a match
            if match_num >= 3:
                match = []

                for x in range(settings.BOARD_WIDTH - 1,
                               settings.BOARD_WIDTH - 1 - match_num, -1):
                    match.append(self.tiles[y][x])

                self.matches.append(match)

        # Vertical matches
        for x in range(settings.BOARD_WIDTH):
            color_to_match = self.tiles[0][x].color

            match_num = 1

            for y in range(1, settings.BOARD_HEIGHT):
                if self.tiles[y][x].color == color_to_match:
                    match_num += 1
                else:
                    color_to_match = self.tiles[y][x].color

                    if match_num >= 3:
                        match: List[Tile] = []

                        for y2 in range(y - 1, y - match_num - 1, -1):
                            match.append(self.tiles[y2][x])

                        self.matches.append(match)

                    # We don't need to check last two if they won't be in a
                    # match
                    if y >= settings.BOARD_HEIGHT - 2:
                        break

                    match_num = 1

            # account for the last column ending with a match
            if match_num >= 3:
                match = []

                for y in range(settings.BOARD_HEIGHT - 1,
                               settings.BOARD_HEIGHT - 1 - match_num, -1):
                    match.append(self.tiles[y][x])

                self.matches.append(match)

        # Returns a list of matches or None
        return self.matches if len(self.matches) > 0 else None

    def remove_matches(self) -> None:
        for match in self.matches:
            for tile in match:
                self.tiles[tile.i][tile.j] = None

        self.matches = []

    def get_falling_tiles(self) -> Tuple[Any, Dict[str, Any]]:
        # List of tweens to create
        tweens: Tuple[Any, Dict[str, Any]] = []

        # for each column, go up tile by tile unill we hit a space
        for j in range(settings.BOARD_WIDTH):
            space = False
            space_i = -1
            i = settings.BOARD_HEIGHT - 1

            while i >= 0:
                tile = self.tiles[i][j]

                # if our previous tile was a space
                if space:
                    # if the current tile is not a space
                    if tile is not None:
                        self.tiles[space_i][j] = tile
                        tile.i = space_i

                        # set its prior position to None
                        self.tiles[i][j] = None

                        tweens.append(
                            (tile, {'y': tile.i * settings.TILE_SIZE}))
                        space = False
                        i = space_i
                        space_i = -1
                elif tile is None:
                    space = True

                    if space_i == -1:
                        space_i = i

                i -= 1

        # create a replacement tiles at the top of the screen
        for j in range(settings.BOARD_WIDTH):
            for i in range(settings.BOARD_HEIGHT):
                tile = self.tiles[i][j]

                if tile is None:
                    tile = Tile(
                        i,
                        j,
                        random.randint(
                            0,
                            settings.NUM_COLORS -
                            1),
                        random.randint(
                            0,
                            settings.NUM_VARIETIES -
                            1))
                    tile.y -= settings.TILE_SIZE
                    self.tiles[i][j] = tile
                    tweens.append((tile, {'y': tile.i * settings.TILE_SIZE}))

        return tweens
