"""
ISPPJ1 2024
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that moves a rectangle from the left to the right
by interpolating its position through time.
"""

import pygame

from gale.game import Game
from gale.input_handler import InputHandler, KEY_ESCAPE, InputData

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

MOVE_DURATION = 3


class TweenGame(Game):
    SQUARE_SIZE = 50

    def init(self) -> None:
        self.rect = pygame.Rect(
            0,
            WINDOW_HEIGHT // 2 - self.SQUARE_SIZE // 2,
            self.SQUARE_SIZE,
            self.SQUARE_SIZE,
        )
        # end X position for our interpolation
        self.end_x = WINDOW_WIDTH - self.SQUARE_SIZE
        self.timer = 0

    def update(self, dt: float) -> None:
        self.timer += dt
        self.rect.x = min(self.end_x, self.end_x * (self.timer / MOVE_DURATION))

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()


if __name__ == "__main__":
    tween_game = TweenGame("Tween Game", WINDOW_WIDTH, WINDOW_HEIGHT, fps=60)
    tween_game.exec()
