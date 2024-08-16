"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Pause state.
"""
import pygame

from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text

import settings


class PauseState(BaseState):
    def enter(self, **params: dict) -> None:
        self.level = params["level"]
        self.paddle = params["paddle"]
        self.ball = params["ball"]
        self.bricks = params["bricks"]
        self.score = params["score"]
        self.lives = params["lives"]
        self.broken_bricks_counter = params["broken_bricks_counter"]
        self.live_factor = params["live_factor"]
        self.points_to_next_live = params["points_to_next_live"]
        settings.SOUNDS["pause"].play()

    def render(self, surface: pygame.Surface) -> None:
        heart_x = settings.VIRTUAL_WIDTH - 120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][0]
            )
            heart_x += 11
            i += 1

        # Draw empty hearts
        while i < 3:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][1]
            )
            heart_x += 11
            i += 1

        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )

        for brick in self.bricks:
            brick.render(surface)

        self.paddle.render(surface)

        render_text(
            surface,
            "Pause",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 2,
            (255, 255, 255),
            center=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            self.state_machine.change(
                "play",
                level=self.level,
                score=self.score,
                lives=self.lives,
                paddle=self.paddle,
                ball=self.ball,
                bricks=self.bricks,
                broken_bricks_counter=self.broken_bricks_counter,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
                resume=True,
            )
