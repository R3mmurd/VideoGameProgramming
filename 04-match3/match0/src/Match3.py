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

    def render(self, surface: pygame.Surface) -> None:
        for row in self.board:
            for block in row:
                block.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
        else:
            self.state_machine.on_input(input_id, input_data)

    def __generate_board(self) -> None:
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                self.board[i][j] = Tile(
                    x=j * settings.TILE_SIZE,
                    y=i * settings.TILE_SIZE,
                    frame=random.randint(0, len(settings.FRAMES["tiles"]) - 1),
                )
