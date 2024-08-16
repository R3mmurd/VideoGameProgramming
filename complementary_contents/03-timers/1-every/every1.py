"""
ISPPV1 2023
Timers, every

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example of how to create three timers that increment
counters every one, two, and four seconds respectively.
"""
import pygame

from gale.input_handler import InputHandler, KEY_ESCAPE, InputData
from gale.game import Game
from gale.text import render_text

InputHandler.set_keyboard_action(KEY_ESCAPE, "quit")


class TimerGame(Game):
    def init(self) -> None:
        self.timer1 = 0
        self.interval1 = 1
        self.counter1 = 0
        self.timer2 = 0
        self.interval2 = 2
        self.counter2 = 0
        self.timer3 = 0
        self.interval3 = 4
        self.counter3 = 0
        self.font = pygame.font.Font("font.ttf", 64)
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.timer1 += dt
        self.timer2 += dt
        self.timer3 += dt

        if self.timer1 >= self.interval1:
            self.timer1 %= self.interval1
            self.counter1 += 1

        if self.timer2 >= self.interval2:
            self.timer2 %= self.interval2
            self.counter2 += 1

        if self.timer3 >= self.interval3:
            self.timer3 %= self.interval3
            self.counter3 += 1

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            str(self.counter1),
            self.font,
            640,
            260,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            str(self.counter2),
            self.font,
            640,
            360,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            str(self.counter3),
            self.font,
            640,
            460,
            (255, 255, 255),
            center=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()


if __name__ == "__main__":
    timer_game = TimerGame("Timer 0", 1280, 720)
    timer_game.exec()
