import pygame

import settings

class Brick:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 32
        self.height = 16

        self.texture = settings.TEXTURES['spritesheet']

        self.tier = 0   # [0, 3]
        self.color = 0  # [0, 4]

        # To decide whether render it or not and collision detection
        self.in_play = True
    
    def hit(self) -> None:
        settings.SOUNDS['brick_hit_2'].stop()
        settings.SOUNDS['brick_hit_2'].play()

        if self.tier == 0:
            if self.color == 0:
                self.in_play = False
                settings.SOUNDS['brick_hit_1'].stop()
                settings.SOUNDS['brick_hit_1'].play()
            else:
                self.tier = 3
                self.color -= 1
        else:
            self.tier -= 1

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, surface: pygame.Surface) -> None:
        if self.in_play:
            frame = self.color * 4 + self.tier
            surface.blit(self.texture, (self.x, self.y), settings.FRAMES['bricks'][frame])
