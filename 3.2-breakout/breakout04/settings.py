import pygame

from gale import input_handler
from gale.frames import generate_frames

from src.frames_utility import generate_paddle_frames, generate_ball_frames

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

PADDLE_SPEED = 200

pygame.mixer.init()

SOUNDS = {
    'paddle_hit': pygame.mixer.Sound("sounds/paddle_hit.wav"),
    'selected': pygame.mixer.Sound("sounds/selected.wav"),
}

TEXTURES = {
    'background': pygame.image.load("graphics/background.png"),
    'spritesheet': pygame.image.load("graphics/breakout.png"),
    'hearts': pygame.image.load('graphics/hearts.png'),
    'arrows': pygame.image.load("graphics/arrows.png")
}

FRAMES = {
    'paddles': generate_paddle_frames(),
    'balls': generate_ball_frames(),
    'hearts': generate_frames(TEXTURES['hearts'], 10, 9),
    'arrows': generate_frames(TEXTURES['arrows'], 24, 24)
}

pygame.font.init()

FONTS = {
    'tiny': pygame.font.Font("fonts/font.ttf", 6),
    'small': pygame.font.Font("fonts/font.ttf", 8),
    'medium': pygame.font.Font("fonts/font.ttf", 12),
    'large': pygame.font.Font("fonts/font.ttf", 24),
}
