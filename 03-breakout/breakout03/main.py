"""
ISPPJ1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the main program to run the game.
"""

import settings
from src.Breakout import Breakout

if __name__ == "__main__":
    game = Breakout(
        "Breakout",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
    )
    game.exec()
