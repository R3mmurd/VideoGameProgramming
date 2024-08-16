"""
ISPPV1 2024
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Match3 as a specialization of gale.Game
"""

import random

import pygame

from gale.game import Game
from gale.input_handler import InputData

import settings
from src.Tile import Tile


class Match3(Game):
    def init(self) -> None:
        self.board = [
            [None for _ in range(settings.BOARD_WIDTH)]
            for _ in range(settings.BOARD_HEIGHT)
        ]
        self.__generate_board()

        # Currently selected tile will be swapped with the next tile we choose.
        # We make it a flag instead of a reference so we can remove it later.
        self.highlighted_tile = False
        self.highlighted_i = None
        self.highlighted_j = None

    def render(self, surface: pygame.Surface) -> None:
        for row in self.board:
            for block in row:
                block.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()

        if input_id == "click" and input_data.pressed:
            pos_x, pos_y = input_data.position
            pos_x = pos_x * settings.VIRTUAL_WIDTH // settings.WINDOW_WIDTH
            pos_y = pos_y * settings.VIRTUAL_HEIGHT // settings.WINDOW_HEIGHT
            i = (pos_y - settings.BOARD_OFFSET_Y) // settings.TILE_SIZE
            j = (pos_x - settings.BOARD_OFFSET_X) // settings.TILE_SIZE

            if not self.highlighted_tile:
                self.highlighted_tile = True
                self.highlighted_i = i
                self.highlighted_j = j
            else:
                tile1 = self.board[i][j]
                tile2 = self.board[self.highlighted_i][self.highlighted_j]

                # Swap tiles
                self.board[tile1.i][tile1.j], self.board[tile2.i][tile2.j] = (
                    self.board[tile2.i][tile2.j],
                    self.board[tile1.i][tile1.j],
                )
                tile1.x, tile1.y, tile2.x, tile2.y = tile2.x, tile2.y, tile1.x, tile1.y
                tile1.i, tile1.j, tile2.i, tile2.j = tile2.i, tile2.j, tile1.i, tile1.j

                self.highlighted_tile = False

    def __generate_board(self) -> None:
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                self.board[i][j] = Tile(
                    x=j * settings.TILE_SIZE,
                    y=i * settings.TILE_SIZE,
                    frame=random.randint(0, len(settings.FRAMES["tiles"]) - 1),
                )
