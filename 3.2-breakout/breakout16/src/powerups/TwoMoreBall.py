"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to add two more ball to the game.
"""
import random
from typing import TypeVar

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class TwoMoreBall(PowerUp):
    """
    Power-up to add two more ball to the game.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.frame = 8

    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle

        for _ in range(2):
            b = Ball(paddle.x + paddle.width // 2 - 4, paddle.y - 8)
            settings.SOUNDS["paddle_hit"].play()

            b.vx = random.randint(-80, 80)
            b.vy = random.randint(-170, -100)
            play_state.balls.append(b)

        self.in_play = False
