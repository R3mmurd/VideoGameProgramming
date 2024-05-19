"""
ISPPJ1 2023
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that generates 1000 random rectangles and moves them
from the left to the right by interpolating their position through time
by using gale.timer.Timer.tween.
"""
import random

import pygame

from gale.game import Game
from gale.input_handler import InputHandler, KEY_ESCAPE, InputData
from gale.timer import Timer

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

            rect = pygame.Rect(0, y, self.SQUARE_SIZE, self.SQUARE_SIZE)
            rate = random.uniform(0.5, TIMER_MAX)

            self.rects.append(rect)
            Timer.tween(rate, [(rect, {"left": WINDOW_WIDTH - self.SQUARE_SIZE})])

        InputHandler.register_listener(self)

    def render(self, surface: pygame.Surface) -> None:
        for rect in self.rects:
            pygame.draw.rect(surface, (255, 255, 255), rect)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()


if __name__ == "__main__":
    tween_game = TweenGame("Tween Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    tween_game.exec()
