"""
ISPPJ1 2023
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that shows how to create a chain of
interpolated movements.
"""
import pygame

from gale.game import Game
from gale.input_handler import InputHandler, KEY_ESCAPE, InputData

InputHandler.set_keyboard_action(KEY_ESCAPE, 'quit')

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

MOVEMENT_TIME = 2


class ChainGame(Game):

    SQUARE_SIZE = 50

    def init(self) -> None:
        self.rect = pygame.Rect(0, 0, self.SQUARE_SIZE, self.SQUARE_SIZE)
        self.base_left = 0
        self.base_top = 0

        self.timer = 0

        self.destinations = (
            {
                'left': WINDOW_WIDTH - self.SQUARE_SIZE,
                'top': 0,
                'reached': False
            },
            {
                'left': WINDOW_WIDTH - self.SQUARE_SIZE,
                'top': WINDOW_HEIGHT - self.SQUARE_SIZE,
                'reached': False
            },
            {
                'left': 0,
                'top': WINDOW_HEIGHT - self.SQUARE_SIZE,
                'reached': False
            },
            {
                'left': 0,
                'top': 0,
                'reached': False
            }
        )

        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.timer = min(MOVEMENT_TIME, self.timer + dt)

        for d in self.destinations:
            if d['reached']:
                continue

            self.rect.left = self.base_left + \
                (d['left'] - self.base_left) * self.timer / MOVEMENT_TIME
            self.rect.top = self.base_top + \
                (d['top'] - self.base_top) * self.timer / MOVEMENT_TIME

            if self.timer == MOVEMENT_TIME:
                d['reached'] = True
                self.base_left = d['left']
                self.base_top = d['top']
                self.timer = 0

            break

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'quit' and input_data.pressed:
            self.quit()


if __name__ == '__main__':
    chain_game = ChainGame("Chain Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    chain_game.exec()
