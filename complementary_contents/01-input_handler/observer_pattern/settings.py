"""
ISPPJ1 2023
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the input binding set up.
"""
import pygame

input_binding = {
    "keyboard": {
        pygame.K_SPACE: "jump",
    },
    "mouse": {1: "shoot", 3: "jump"},
    "motion": {
        (0, 1): "rotate_down",
        (0, -1): "rotate_up",
        (-1, 0): "rotate_left",
        (1, 0): "rotate_right",
    },
}
