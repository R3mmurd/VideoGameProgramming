"""
ISPPV1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains some util functions to generate frames for the game textures.
"""

from typing import List

import pygame


def generate_paddle_frames() -> List[List[pygame.Rect]]:
    paddle_base_width = 32
    paddle_height = 16

    x = 0
    y = paddle_height * 4

    frames = []

    for _ in range(4):
        frames.append(
            [
                # The smallest paddle is in (0, y) and its dimensions are 32x16.
                pygame.Rect(x, y, paddle_base_width, paddle_height),
                # The next paddle is in (32, y) and its dimensions are 64x16.
                pygame.Rect(
                    x + paddle_base_width, y, paddle_base_width * 2, paddle_height
                ),
                # The next paddle is in (96, y) and its dimensions are 96x16.
                pygame.Rect(
                    x + paddle_base_width * 3, y, paddle_base_width * 3, paddle_height
                ),
                # The largest paddle is in (0, y + 16) # and its dimensions are
                # 128x16.
                pygame.Rect(x, y + paddle_height, paddle_base_width * 4, paddle_height),
            ]
        )

        y += paddle_height * 2

    return frames
