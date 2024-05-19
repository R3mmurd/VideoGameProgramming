"""
ISPPJ1 2023
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the input binding set up.
"""
import pygame

from ActionJump import ActionJump
from ActionShoot import ActionShoot

input_binding = {
    "keyboard": {
        pygame.K_SPACE: ActionJump,
    },
    "mouse": {1: ActionShoot, 3: ActionJump},
}
