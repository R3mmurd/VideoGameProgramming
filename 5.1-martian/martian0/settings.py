import pathlib

import pygame

from gale import frames

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4

NUM_LEVELS = 1

BASE_DIR = pathlib.Path(__file__).parent

TEXTURES = {
    'tiles':  pygame.image.load(BASE_DIR / 'graphics/tileset.png')
}

FRAMES = {
    'tiles': frames.generate_frames(TEXTURES['tiles'], 16, 16)
}
TILEMAPS = {
    f'level{i}': f"{BASE_DIR}/tilemaps/level{i}.tmx" for i in range(1, NUM_LEVELS + 1)
}
