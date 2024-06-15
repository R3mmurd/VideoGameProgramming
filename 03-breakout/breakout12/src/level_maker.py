"""
ISPPJ1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains a function to generate random levels.
"""

import random
from typing import List

from src.Brick import Brick


def create_level(level: int) -> List[Brick]:
    bricks = []

    num_rows = random.randint(1, 5)
    num_cols = random.randint(7, 13)

    # Ensure odd number of columns
    num_cols = num_cols + 1 if num_cols % 2 == 0 else num_cols

    highest_tier = min(3, (level - 1) % 4)
    highest_color = min(4, (level - 1) // 4)

    x_padding = 8 + (13 - num_cols) * 16
    y_padding = 16

    while not bricks:
        for y in range(num_rows):
            skip_pattern = random.random() < 0.5
            skip_flag = random.random() < 0.5
            alternate_pattern = random.random() < 0.5
            alternate_flag = random.random() < 0.5
            alternate_color_1 = random.randint(0, highest_color)
            alternate_color_2 = random.randint(0, highest_color)
            alternate_tier_1 = random.randint(0, highest_tier)
            alternate_tier_2 = random.randint(0, highest_tier)
            solid_color = random.randint(0, highest_color)
            solid_tier = random.randint(0, highest_tier)

            for x in range(num_cols):
                if skip_pattern and skip_flag:
                    skip_flag = not skip_flag
                    continue

                skip_flag = not skip_flag

                b = Brick(x * 32 + x_padding, y * 16 + y_padding)

                if alternate_pattern and alternate_flag:
                    b.color = alternate_color_1
                    b.tier = alternate_tier_1
                    alternate_flag = not alternate_flag
                else:
                    b.color = alternate_color_2
                    b.tier = alternate_tier_2
                    alternate_flag = not alternate_flag

                if not alternate_pattern:
                    b.color = solid_color
                    b.tier = solid_tier

                bricks.append(b)

    return bricks
