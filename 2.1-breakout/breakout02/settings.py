import pygame

from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, 'move_up')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, 'move_right')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, 'move_down')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, 'move_left')

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we are trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

pygame.mixer.init()

SOUNDS = {
    'paddle_hit': pygame.mixer.Sound("sounds/paddle_hit.wav"),
    'selected': pygame.mixer.Sound("sounds/selected.wav"),
}

TEXTURES = {
    'background': pygame.image.load("graphics/background.png"),
}

pygame.font.init()

FONTS = {
    'tiny': pygame.font.Font("fonts/font.ttf", 6),
    'small': pygame.font.Font("fonts/font.ttf", 8),
    'medium': pygame.font.Font("fonts/font.ttf", 12),
    'large': pygame.font.Font("fonts/font.ttf", 24),
}
