"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Play state.
"""
import random

import pygame

from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text

import settings


class PlayState(BaseState):
    def enter(self, **params: dict):
        self.level = params["level"]
        self.score = params["score"]
        self.lives = params["lives"]
        self.paddle = params["paddle"]
        self.ball = params["ball"]
        self.bricks = params["bricks"]
        self.broken_bricks_counter = params["broken_bricks_counter"]

        settings.SOUNDS["paddle_hit"].play()

        self.ball.vx = random.randint(-80, 80)
        self.ball.vy = random.randint(-170, -100)

    def update(self, dt: float) -> None:
        self.paddle.update(dt)
        self.ball.update(dt)
        self.ball.solve_world_boundaries()

        if not self.ball.in_play:
            self.lives -= 1
            if self.lives == 0:
                self.state_machine.change("game_over")
            else:
                self.state_machine.change(
                    "serve",
                    level=self.level,
                    score=self.score,
                    lives=self.lives,
                    paddle=self.paddle,
                    bricks=self.bricks,
                    broken_bricks_counter=self.broken_bricks_counter,
                )

        # Check collision with the paddle
        if self.ball.collides(self.paddle):
            settings.SOUNDS["paddle_hit"].stop()
            settings.SOUNDS["paddle_hit"].play()
            self.ball.rebound(self.paddle)
            self.ball.push(self.paddle)

        # Check collision with bricks
        for brick in self.bricks:
            if not (brick.in_play and self.ball.collides(brick)):
                continue

            brick.hit()
            self.ball.rebound(brick)

            if not brick.in_play:
                self.broken_bricks_counter += 1

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
        self.ball.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.paddle.vx = -settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx < 0:
                self.paddle.vx = 0
        elif input_id == "move_right":
            if input_data.pressed:
                self.paddle.vx = settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx > 0:
                self.paddle.vx = 0
