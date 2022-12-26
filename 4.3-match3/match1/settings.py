from pathlib import Path

import pygame

from gale import input_handler
from gale.frames import generate_frames

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, 'quit')
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, 'click')

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

BOARD_OFFSET_X = 128
BOARD_OFFSET_Y = 16

TILE_SIZE = 32

BASE_DIR = Path(__file__).parent

TEXTURES = {
    'tiles': pygame.image.load(BASE_DIR / "graphics/match3.png")
}

FRAMES = {
    'tiles': generate_frames(TEXTURES['tiles'], TILE_SIZE, TILE_SIZE)
}
