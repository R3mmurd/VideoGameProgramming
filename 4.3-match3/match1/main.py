"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the main program to run the game.
"""
"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the main program to run the game.
"""

import settings
from src.Match3 import Match3
if __name__ == '__main__':
    match3 = Match3(
        "Match 3",
        settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT
    )
    match3.exec()
