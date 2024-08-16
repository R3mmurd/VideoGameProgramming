"""
ISPPV1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the game settings that include the association of the
inputs with an their ids, constants of values to set up the game, sounds,
textures, frames, and fonts.
"""
from pathlib import Path

import pygame

from gale import input_handler
from gale.frames import generate_frames

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")

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

TEXTURES = {"tiles": pygame.image.load(BASE_DIR / "graphics" / "match3.png")}

FRAMES = {"tiles": generate_frames(TEXTURES["tiles"], TILE_SIZE, TILE_SIZE)}

SOUNDS = {}

FONTS = {}
