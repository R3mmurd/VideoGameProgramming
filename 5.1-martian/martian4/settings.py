"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""
import pathlib
import sys

import pygame

from gale import frames
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_RIGHT, 'move_right')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_d, 'move_right')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_LEFT, 'move_left')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_a, 'move_left')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, 'jump')
input_handler.InputHandler.set_mouse_click_action(
    input_handler.MOUSE_BUTTON_1, 'jump')

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4

PLAYER_SPEED = 80

GRAVITY = 980

NUM_LEVELS = 1

BASE_DIR = pathlib.Path(__file__).parent

TEXTURES = {
    'tiles': pygame.image.load(BASE_DIR / 'graphics/tileset.png'),
    'martian': pygame.image.load(BASE_DIR / 'graphics/martian.png'),
    'creatures': pygame.image.load(BASE_DIR / 'graphics/creatures.png')
}

FRAMES = {
    'tiles': frames.generate_frames(TEXTURES['tiles'], 16, 16),
    'martian': frames.generate_frames(TEXTURES['martian'], 16, 20),
    'creatures': frames.generate_frames(TEXTURES['creatures'], 16, 16)
}


TILEMAPS = {
    f'level{i}': f"{BASE_DIR}/tilemaps/level{i}.tmx" for i in range(1, NUM_LEVELS + 1)
}
