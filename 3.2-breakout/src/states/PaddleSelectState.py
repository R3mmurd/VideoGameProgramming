"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the state to show select the paddle to play.
"""

import pygame

from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text

import settings
from src.Paddle import Paddle


class PaddleSelectState(BaseState):
    def enter(self) -> None:
        self.paddle = Paddle(
            settings.VIRTUAL_WIDTH // 2 - 32, settings.VIRTUAL_HEIGHT - 64
        )
        self.arrows_texture = settings.TEXTURES["arrows"]
        self.gray_scale_surface = pygame.Surface((24, 24), pygame.SRCALPHA)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("serve", level=1, paddle=self.paddle)

        if input_id == "move_right" and input_data.pressed:
            self.paddle.skin = min(3, self.paddle.skin + 1)
        elif input_id == "move_left" and input_data.pressed:
            self.paddle.skin = max(0, self.paddle.skin - 1)

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            "Select a paddle color with left and right",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            20,
            (255, 255, 255),
            center=True,
        )
        render_text(
            surface,
            "Press Enter to continue!",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            50,
            (255, 255, 255),
            center=True,
        )

        self.paddle.render(surface)

        surface.blit(
            self.arrows_texture,
            (settings.VIRTUAL_WIDTH // 2 - 72 - 24, settings.VIRTUAL_HEIGHT - 68),
            settings.FRAMES["arrows"][0],
        )

        if self.paddle.skin == 0:
            pygame.draw.circle(self.gray_scale_surface, (40, 40, 40, 150), (12, 12), 12)
            surface.blit(
                self.gray_scale_surface,
                (settings.VIRTUAL_WIDTH // 2 - 72 - 24, settings.VIRTUAL_HEIGHT - 68),
            )

        surface.blit(
            self.arrows_texture,
            (settings.VIRTUAL_WIDTH // 2 + 72, settings.VIRTUAL_HEIGHT - 68),
            settings.FRAMES["arrows"][1],
        )

        if self.paddle.skin == 3:
            pygame.draw.circle(self.gray_scale_surface, (40, 40, 40, 150), (12, 12), 12)
            surface.blit(
                self.gray_scale_surface,
                (settings.VIRTUAL_WIDTH // 2 + 72, settings.VIRTUAL_HEIGHT - 68),
            )
