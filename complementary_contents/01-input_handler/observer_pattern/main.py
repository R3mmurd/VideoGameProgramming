"""
ISPPJ1 2024
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
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Input Handler Example by Observers")
    screen.fill((255, 255, 255))
    pygame.display.update()
    actor = Actor("Player")
    InputHandler.register(actor)
    while True:
        InputHandler.handle_input()
