"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Victory state.
"""
import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings


class VictoryState(BaseState):
    def enter(self, **params: dict) -> None:
        settings.SOUNDS['level_complete'].play()
        self.lives = params['lives']
        self.level = params['level']
        self.score = params['score']
        self.paddle = params['paddle']
        self.ball = params['ball']
        self.live_factor = params['live_factor']
        self.points_to_next_live = params['points_to_next_live']
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'enter' and input_data.pressed:
            self.state_machine.change(
                'serve',
                lives=self.lives,
                level=self.level + 1,
                paddle=self.paddle,
                score=self.score,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor
            )

    def render(self, surface: pygame.Surface) -> None:
        heart_x = settings.VIRTUAL_WIDTH - 120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.TEXTURES['hearts'], (heart_x, 5),
                settings.FRAMES['hearts'][0]
            )
            heart_x += 11
            i += 1

        # Draw empty hearts
        while i < 3:
            surface.blit(
                settings.TEXTURES['hearts'], (heart_x, 5),
                settings.FRAMES['hearts'][1]
            )
            heart_x += 11
            i += 1

        render_text(
            surface, f'Score: {self.score}', settings.FONTS['tiny'],
            settings.VIRTUAL_WIDTH - 80, 5, (255, 255, 255)
        )

        self.paddle.render(surface)

        self.ball.render(surface)

        render_text(
            surface, f'Level {self.level} completed!', settings.FONTS['large'],
            settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2 - 30,
            (255, 255, 255), center=True
        )
        render_text(
            surface, 'Press Enter to continue!', settings.FONTS['medium'],
            settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2,
            (255, 255, 255), center=True
        )
