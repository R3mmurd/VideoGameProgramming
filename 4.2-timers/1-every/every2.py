"""
ISPPJ1 2023
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example of how to create three timers that increment
counters every one, two, and four seconds respectively by using gale.timer.Timer.every.
"""
from typing import Callable

import pygame

from gale.input_handler import InputHandler, KEY_ESCAPE, InputData
from gale.game import Game
from gale.text import render_text
from gale.timer import Timer

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")


class TimerGame(Game):
    def init(self) -> None:
        self.intervals = [1, 2, 4]
        self.counters = [0, 0, 0]

        def inc(i: int) -> Callable[[], None]:
            def inc_i():
                self.counters[i] += 1
            return inc_i

        for i in range(len(self.intervals)):
            Timer.every(self.intervals[i], inc(i))

        self.font = pygame.font.Font("font.ttf", 64)
        InputHandler.register_listener(self)

    def render(self, surface: pygame.Surface) -> None:
        for i in range(len(self.counters)):
            render_text(surface,
                        str(self.counters[i]),
                        self.font,
                        640,
                        i * 100 + 260,
                        (255,
                         255,
                         255),
                        center=True)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'quit' and input_data.pressed:
            self.quit()


if __name__ == '__main__':
    timer_game = TimerGame("Timer 0", 1280, 720)
    timer_game.exec()
