import pygame

from gale.input_handler import InputHandler, Key

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

FONTS = {}
