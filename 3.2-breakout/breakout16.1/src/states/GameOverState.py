"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Game Over state.
"""
import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings


class GameOverState(BaseState):
    def enter(self, score: int) -> None:
        self.score = score
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("enter_high_score", score=self.score)

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            "Game Over",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 - 30,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            f"Final Score: {self.score}",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            "Press Enter!",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 + 20,
            (255, 255, 255),
            center=True,
        )
