"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""
import pygame

from gale.input_handler import InputHandler, InputData, Key

InputHandler.set_keyboard_action(Key.KEY_RETURN, 'enter')
InputHandler.set_keyboard_action(Key.KEY_UP, 'move_up')
InputHandler.set_keyboard_action(Key.KEY_RIGHT, 'move_right')
InputHandler.set_keyboard_action(Key.KEY_DOWN, 'move_down')
InputHandler.set_keyboard_action(Key.KEY_LEFT, 'move_left')

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
