"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""
from pathlib import Path

import pygame

from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we are trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

BASE_DIR = Path(__file__).parent

pygame.mixer.init()

SOUNDS = {
    "paddle_hit": pygame.mixer.Sound(BASE_DIR / "sounds" / "paddle_hit.wav"),
    "selected": pygame.mixer.Sound(BASE_DIR / "sounds" / "selected.wav"),
}

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "graphics" / "background.png"),
}

FRAMES = {}

pygame.font.init()

FONTS = {
    "tiny": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 6),
    "small": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 12),
    "large": pygame.font.Font(BASE_DIR / "fonts" / "font.ttf", 24),
}
