import pygame

import settings
from src.Camera import Camera
from src.TileMap import TileMap


class GameLevel:
    def __init__(self, num_level: int, camera: Camera) -> None:
        self.tilemap = TileMap(settings.TILEMAPS[f'level{num_level}'])
        self.camera = camera
    
    def update(self, dt: float) -> None:
        self.tilemap.set_render_boundaries(self.camera.get_rect())
    
    def render(self, surface: pygame.Surface) -> None:
        self.tilemap.render(surface)
