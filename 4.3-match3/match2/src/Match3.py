"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Match3 as a specialization of gale.Game
"""
"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Match3 as a specialization of gale.Game
"""




import random
import pygame
from gale.game import Game
from gale.input_handler import InputHandler, InputData
from gale.timer import Timer
import settings
from src.Tile import Tile
class Match3(Game):
    def init(self) -> None:
        self.board = [[None for _ in range(settings.BOARD_WIDTH)] for _ in range(
            settings.BOARD_HEIGHT)]
        self._generate_board()

        # Currently selected tile will be swapped with the next tile we choose.
        # We make it a flag instead of a reference so we can remove it later.
        self.highlighted_tile = False
        self.highlighted_i1 = None
        self.highlighted_j1 = None
        self.highlighted_i2 = None
        self.highlighted_j2 = None
        self.active = True

        InputHandler.register_listener(self)

    def render(self, surface: pygame.Surface) -> None:
        for row in self.board:
            for block in row:
                block.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'quit' and input_data.pressed and self.active:
            self.quit()

        if input_id == 'click' and input_data.pressed and self.active:
            pos_x, pos_y = input_data.position
            pos_x = pos_x * settings.VIRTUAL_WIDTH // settings.WINDOW_WIDTH
            pos_y = pos_y * settings.VIRTUAL_HEIGHT // settings.WINDOW_HEIGHT
            i = (pos_y - settings.BOARD_OFFSET_Y) // settings.TILE_SIZE
            j = (pos_x - settings.BOARD_OFFSET_X) // settings.TILE_SIZE

            if 0 <= i < settings.BOARD_HEIGHT and 0 <= j <= settings.BOARD_WIDTH:
                if not self.highlighted_tile:
                    self.highlighted_tile = True
                    self.highlighted_i1 = i
                    self.highlighted_j1 = j
                else:
                    di = abs(i - self.highlighted_i1)
                    dj = abs(j - self.highlighted_j1)
                    self.highlighted_i2 = i
                    self.highlighted_j2 = j

                    if di <= 1 and dj <= 1 and di != dj:
                        self.active = False
                        tile1 = self.board[self.highlighted_i1][self.highlighted_j1]
                        tile2 = self.board[self.highlighted_i2][self.highlighted_j2]

                        def arrive():
                            tile1 = self.board[self.highlighted_i1][self.highlighted_j1]
                            tile2 = self.board[self.highlighted_i2][self.highlighted_j2]
                            self.board[tile1.i][tile1.j], self.board[tile2.i][tile2.j] = self.board[tile2.i][tile2.j], self.board[tile1.i][tile1.j]
                            tile1.i, tile1.j, tile2.i, tile2.j = tile2.i, tile2.j, tile1.i, tile1.j
                            self.active = True

                        # Swap tiles
                        Timer.tween(
                            0.2,
                            [
                                (tile1, {'x': tile2.x, 'y': tile2.y}),
                                (tile2, {'x': tile1.x, 'y': tile1.y}),
                            ],
                            on_finish=arrive
                        )

                    self.highlighted_tile = False

    def _generate_board(self) -> None:
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                self.board[i][j] = Tile(
                    x=j * settings.TILE_SIZE,
                    y=i * settings.TILE_SIZE,
                    frame=random.randint(0, len(settings.FRAMES['tiles']) - 1)
                )
