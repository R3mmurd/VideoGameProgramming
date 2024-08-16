"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the state to enter high score.
"""
import string

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings
from src.highscores import read_highscores, write_highscores


class EnterHighScoreState(BaseState):
    def enter(self, score: int) -> None:
        self.score = score
        self.hs = read_highscores()

        if self.score > 0 and (
            len(self.hs) < settings.NUM_HIGHSCORES or self.score > self.hs[-1][1]
        ):
            settings.SOUNDS["high_score"].play()
        else:
            self.state_machine.change("start")

        self.name = [0, 0, 0]
        self.selected = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            name = "".join([string.ascii_uppercase[i] for i in self.name])
            self.hs.append([name, self.score])
            self.hs.sort(key=lambda item: item[-1], reverse=True)
            write_highscores(self.hs[: settings.NUM_HIGHSCORES])
            self.state_machine.change("start")

        if input_id == "move_left" and input_data.pressed:
            self.selected = max(0, self.selected - 1)
        elif input_id == "move_right" and input_data.pressed:
            self.selected = min(2, self.selected + 1)
        elif input_id == "move_down" and input_data.pressed:
            self.name[self.selected] = max(0, self.name[self.selected] - 1)
        elif input_id == "move_up" and input_data.pressed:
            self.name[self.selected] = min(
                len(string.ascii_uppercase) - 1, self.name[self.selected] + 1
            )

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            f"Final score: {self.score}",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 - 100,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            f"You are in the top {settings.NUM_HIGHSCORES}!",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 - 70,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            "Enter your name",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2 - 20,
            (255, 255, 255),
            center=True,
        )

        x = settings.VIRTUAL_WIDTH // 2 - 20

        for i in range(3):
            color = (52, 235, 216) if self.selected == i else (255, 255, 255)

            render_text(
                surface,
                string.ascii_uppercase[self.name[i]],
                settings.FONTS["medium"],
                x,
                settings.VIRTUAL_HEIGHT // 2 + 10,
                color,
                center=True,
            )

            x += 20

        render_text(
            surface,
            "Press Enter to finish!",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 50,
            (255, 255, 255),
            center=True,
        )
