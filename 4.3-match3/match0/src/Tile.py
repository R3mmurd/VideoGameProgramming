import pygame

import settings

class Tile:
    def __init__(self, x: int, y: int, frame: int) -> None:
        self.x = x
        self.y = y
        self.frame = frame
    
    def render(self, surface: pygame.Surface) -> None:
        surface.blit(
            settings.TEXTURES['tiles'],
            (self.x + settings.BOARD_OFFSET_X, self.y + settings.BOARD_OFFSET_Y),
            settings.FRAMES['tiles'][self.frame]
        )
