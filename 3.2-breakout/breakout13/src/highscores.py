"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains util functions to load and store highscores.
"""
import os
from typing import List, Any

import settings

# Path of home user directory
USER_HOME = os.path.expanduser('~')

BREAKOUT_DIR = os.path.join(USER_HOME, '.breakout')

HIGHSCORES_PATH = os.path.join(BREAKOUT_DIR, 'highscores.dat')


def read_highscores() -> List[List[Any]]:
    if not os.path.exists(BREAKOUT_DIR):
        os.mkdir(BREAKOUT_DIR)

    with open(HIGHSCORES_PATH, 'a'):
        pass

    highscores = []

    with open(HIGHSCORES_PATH, 'r') as f:
        for line in f:
            line = line[:-1]
            line = line.split(':')
            line[-1] = int(line[-1])
            highscores.append(line)

    return highscores


def write_highscores(highscores: List[List[Any]]) -> None:
    with open(HIGHSCORES_PATH, 'w') as f:
        for line in highscores:
            line[-1] = str(line[-1])
            line = ':'.join(line)
            f.write(f'{line}\n')
