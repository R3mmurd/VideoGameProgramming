"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_RETURN, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, 'move_up')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_RIGHT, 'move_right')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_DOWN, 'move_down')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_LEFT, 'move_left')
input_handler.InputHandler.set_keyboard_action(
    input_handler.KEY_ESCAPE, 'quit')

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we are trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

SOUNDS = {}

TEXTURES = {}

FRAMES = {}

FONTS = {}
