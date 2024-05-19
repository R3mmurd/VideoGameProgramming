"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Start state.
"""

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings


class StartState(BaseState):
    def enter(self) -> None:
        self.selected = 1

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_down" and input_data.pressed and self.selected == 1:
            settings.SOUNDS["paddle_hit"].play()
            self.selected = 2
        elif input_id == "move_up" and input_data.pressed and self.selected == 2:
            settings.SOUNDS["paddle_hit"].play()
            self.selected = 1
        elif input_id == "enter" and input_data.pressed:
            settings.SOUNDS["selected"].play()

            if self.selected == 1:
                self.state_machine.change("paddle_select")
            else:
                self.state_machine.change("high_score")

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            "Breakout",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 3,
            (255, 255, 255),
            center=True,
        )

        color = (52, 235, 216) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface,
            "Play Game",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 60,
            color,
            center=True,
        )

        color = (52, 235, 216) if self.selected == 2 else (255, 255, 255)

        render_text(
            surface,
            "High scores",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 30,
            color,
            center=True,
        )
