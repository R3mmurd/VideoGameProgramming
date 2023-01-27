"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Breakout as a specialization of gale.Game
"""
import pygame

from gale.game import Game
from gale.input_handler import InputHandler, InputData
from gale.state_machine import StateMachine


class Breakout(Game):
    def init(self) -> None:
        self.state_machine = StateMachine()
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
