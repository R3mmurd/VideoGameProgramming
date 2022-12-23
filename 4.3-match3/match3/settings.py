import pygame

from gale import input_handler

from src.frames_utility import generate_tile_frames

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, 'enter')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, 'up')
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, 'down')
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, 'click')

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

TILE_SIZE = 32

NUM_VARIETIES = 6
NUM_COLORS = 18

BACKGROUND_SCROLL_SPEED = 40
BACKGROUND_LOOPING_POINT = -1024 + VIRTUAL_WIDTH - 4 + 51

TEXTURES = {
    'background': pygame.image.load("graphics/background.png"),
    'tiles': pygame.image.load("graphics/match3.png")
}

FRAMES = {
    'tiles': generate_tile_frames(TEXTURES['tiles'])
}

pygame.mixer.init()

SOUNDS = {
    'clock': pygame.mixer.Sound("sounds/clock.wav"),
    'error': pygame.mixer.Sound("sounds/error.wav"),
    'game-over': pygame.mixer.Sound("sounds/game-over.wav"),
    'match': pygame.mixer.Sound("sounds/match.wav"),
    'music': pygame.mixer.Sound("sounds/music.mp3"),
    'next-level': pygame.mixer.Sound("sounds/next-level.wav"),
    'select': pygame.mixer.Sound("sounds/select.wav")
}

pygame.font.init()

FONTS = {
    'small': pygame.font.Font("fonts/font.ttf", 12),
    'medium': pygame.font.Font("fonts/font.ttf", 24),
    'large': pygame.font.Font("fonts/font.ttf", 48),
    'huge': pygame.font.Font("fonts/font.ttf", 64)
}
