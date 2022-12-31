"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains a function to fetch and store the tile frames.
"""
from typing import List

import pygame

import settings


def generate_tile_frames(
        spritesheet: pygame.Surface) -> List[List[pygame.Rect]]:
    frames = []

    x, y = 0, 0

    rows_counter = 0

    # There are 9 rows
    for _ in range(9):

        # There are two sets of 6 tiles of the same color and different
        # variety.
        for _ in range(2):
            frames.append([])

            for _ in range(6):
                frames[rows_counter].append(
                    pygame.Rect(
                        x,
                        y,
                        settings.TILE_SIZE,
                        settings.TILE_SIZE))
                x += settings.TILE_SIZE

            rows_counter += 1

        y += settings.TILE_SIZE
        x = 0

    return frames
