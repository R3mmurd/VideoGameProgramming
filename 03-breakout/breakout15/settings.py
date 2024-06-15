"""
ISPPJ1 2024
Study Case: Breakout

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

from src.frames_utility import (
    generate_paddle_frames,
    generate_ball_frames,
    generate_brick_frames,
)

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "pause")

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

BASE_DIR = Path(__file__).parent

pygame.mixer.init()

SOUNDS = {
    "paddle_hit": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "paddle_hit.wav"),
    "selected": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "selected.wav"),
    "brick_hit_1": pygame.mixer.Sound(
        BASE_DIR / "assets" / "sounds" / "brick_hit_1.wav"
    ),
    "brick_hit_2": pygame.mixer.Sound(
        BASE_DIR / "assets" / "sounds" / "brick_hit_2.wav"
    ),
    "wall_hit": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "wall_hit.wav"),
    "hurt": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "hurt.wav"),
    "level_complete": pygame.mixer.Sound(
        BASE_DIR / "assets" / "sounds" / "level_complete.wav"
    ),
    "high_score": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "high_score.wav"),
    "life": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "life.wav"),
    "grow_up": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "grow_up.wav"),
    "pause": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "pause.wav"),
}

TEXTURES = {
    "background": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "background.png"
    ),
    "spritesheet": pygame.image.load(BASE_DIR / "assets" / "textures" / "breakout.png"),
    "hearts": pygame.image.load(BASE_DIR / "assets" / "textures" / "hearts.png"),
    "arrows": pygame.image.load(BASE_DIR / "assets" / "textures" / "arrows.png"),
}

FRAMES = {
    "paddles": generate_paddle_frames(),
    "balls": generate_ball_frames(),
    "bricks": generate_brick_frames(TEXTURES["spritesheet"]),
    "hearts": generate_frames(TEXTURES["hearts"], 10, 9),
    "arrows": generate_frames(TEXTURES["arrows"], 24, 24),
}

pygame.font.init()

FONTS = {
    "tiny": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 6),
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 12),
    "large": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 24),
}
