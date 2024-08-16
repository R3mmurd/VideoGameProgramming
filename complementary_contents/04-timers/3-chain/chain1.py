"""
ISPPV1 2024
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that shows how to create a chain of
interpolated movements by using gale.timer.Timer.tween and using the on_finish function.
"""

import pygame

from gale.game import Game
from gale.input_handler import InputHandler, KEY_ESCAPE, InputData
from gale.timer import Timer

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

MOVEMENT_TIME = 2


class ChainGame(Game):

    SQUARE_SIZE = 50

    def init(self) -> None:
        self.rect = pygame.Rect(0, 0, self.SQUARE_SIZE, self.SQUARE_SIZE)

        Timer.tween(
            MOVEMENT_TIME,
            [(self.rect, {"left": WINDOW_WIDTH - self.SQUARE_SIZE})],
            on_finish=lambda: Timer.tween(
                MOVEMENT_TIME,
                [(self.rect, {"top": WINDOW_HEIGHT - self.SQUARE_SIZE})],
                on_finish=lambda: Timer.tween(
                    MOVEMENT_TIME,
                    [(self.rect, {"left": 0})],
                    on_finish=lambda: Timer.tween(
                        MOVEMENT_TIME, [(self.rect, {"top": 0})]
                    ),
                ),
            ),
        )

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()


if __name__ == "__main__":
    chain_game = ChainGame("Chain Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    chain_game.exec()
