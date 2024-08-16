"""
ISPPV1 2024
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the main program to build a window an test the
input handler.
"""

import pygame

from Actor import Actor
from InputHandler import InputHandler

if __name__ == "__main__":
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Input Handler Example by Commands")
    actor = Actor("Player")
    while True:
        action = InputHandler.handle_input()
        if action is not None:
            action.execute(actor)
