"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the base class SuperMartian as a specialization of gale.Game
"""
import pygame

from gale.game import Game
from gale.input_handler import InputData, InputHandler, InputListener
from gale.state_machine import StateMachine

from src.states import game_states


class SuperMartian(Game, InputListener):
    def init(self) -> None:
        self.state_machine = StateMachine({"play": game_states.PlayState})
        self.state_machine.change("play")
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "quit" and input_data.pressed:
            self.quit()
