import pygame

from gale import input_handler
from gale.frames import generate_frames

from src.frames_utility import generate_paddle_frames, generate_ball_frames, generate_brick_frames

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, 'move_up')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, 'move_right')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, 'move_down')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, 'move_left')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, 'pause')

# Size of our actual window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Size we are trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200

NUM_HIGHSCORES = 10

# Num points base to recover a live
LIVE_POINTS_BASE = 2000

PADDLE_GROW_UP_POINTS = 200

pygame.mixer.init()

SOUNDS = {
    'paddle_hit': pygame.mixer.Sound("sounds/paddle_hit.wav"),
    'selected': pygame.mixer.Sound("sounds/selected.wav"),
    'brick_hit_1': pygame.mixer.Sound("sounds/brick_hit_1.wav"),
    'brick_hit_2': pygame.mixer.Sound("sounds/brick_hit_2.wav"),
    'wall_hit': pygame.mixer.Sound("sounds/wall_hit.wav"),
    'hurt': pygame.mixer.Sound("sounds/hurt.wav"),
    'level_complete': pygame.mixer.Sound("sounds/level_complete.wav"),
    'high_score': pygame.mixer.Sound("sounds/high_score.wav"),
    'life': pygame.mixer.Sound("sounds/life.wav"),
    'grow_up': pygame.mixer.Sound("sounds/grow_up.wav"),
    'pause': pygame.mixer.Sound("sounds/pause.wav"),
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
    'bricks': generate_brick_frames(TEXTURES['spritesheet']),
    'hearts': generate_frames(TEXTURES['hearts'], 10, 9),
    'arrows': generate_frames(TEXTURES['arrows'], 24, 24)
}

pygame.font.init()

FONTS = {
    'tiny': pygame.font.Font("fonts/font.ttf", 6),
    'small': pygame.font.Font("fonts/font.ttf", 8),
    'medium': pygame.font.Font("fonts/font.ttf", 12),
    'large': pygame.font.Font("fonts/font.ttf", 24)
}
