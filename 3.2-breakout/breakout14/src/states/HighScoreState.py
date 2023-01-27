"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the state to show the high score list.
"""
import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings
from src.highscores import read_highscores


class HighScoreState(BaseState):
    def enter(self) -> None:
        self.hs = read_highscores()
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def on_input(self, input_id: str, input_data: InputData):
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("start")

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            "High Scores",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            20,
            (255, 255, 255),
            center=True,
        )

        for i in range(settings.NUM_HIGHSCORES):
            name = "---"
            score = "---"

            if i < len(self.hs):
                item = self.hs[i]
                name = item[0]
                score = str(item[1])

            render_text(
                surface,
                f"{i + 1}.",
                settings.FONTS["small"],
                settings.VIRTUAL_WIDTH // 2 - 60,
                50 + i * 17,
                (255, 255, 255),
                center=True,
            )
            render_text(
                surface,
                name,
                settings.FONTS["small"],
                settings.VIRTUAL_WIDTH // 2,
                50 + i * 17,
                (255, 255, 255),
                center=True,
            )
            render_text(
                surface,
                score,
                settings.FONTS["small"],
                settings.VIRTUAL_WIDTH // 2 + 60,
                50 + i * 17,
                (255, 255, 255),
                center=True,
            )
