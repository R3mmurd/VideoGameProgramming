"""
ISPPV1 2024
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that generates 1000 random rectangles and moves them
from the left to the right by interpolating their position through time.
"""

import random

import pygame

from gale.game import Game
from gale.input_handler import InputHandler, KEY_ESCAPE, InputData

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TIMER_MAX = 10


class TweenGame(Game):
    SQUARE_SIZE = 50

    def init(self) -> None:
        self.rects = []

        for _ in range(1000):
            y = random.randint(0, WINDOW_HEIGHT - self.SQUARE_SIZE)
            self.rects.append(
                {
                    "rect": pygame.Rect(0, y, self.SQUARE_SIZE, self.SQUARE_SIZE),
                    "rate": random.uniform(0.5, TIMER_MAX),
                }
            )

        # end X position for our interpolation
        self.end_x = WINDOW_WIDTH - self.SQUARE_SIZE
        self.timer = 0

    def update(self, dt: float) -> None:
        if self.timer < TIMER_MAX:
            self.timer += dt

            for rect in self.rects:
                rect["rect"].x = min(
                    self.end_x, self.end_x * (self.timer / rect["rate"])
                )

    def render(self, surface: pygame.Surface) -> None:
        for rect in self.rects:
            pygame.draw.rect(surface, (255, 255, 255), rect["rect"])

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()


if __name__ == "__main__":
    tween_game = TweenGame("Tween Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    tween_game.exec()
