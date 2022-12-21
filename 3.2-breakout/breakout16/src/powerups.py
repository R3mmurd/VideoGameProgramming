from typing import TypeVar, Any
import random

import pygame

import settings
from src.Ball import Ball


class PowerUp:
    """
    The base power-up.
    """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.vy = settings.POWERUP_SPEED
        self.in_play = True
        self.frame = -1
    
    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 16, 16)

    def collides(self, obj: Any) -> bool:
        return self.get_collision_rect().colliderect(obj.get_collision_rect())

    def update(self, dt: float) -> None:
        if self.y > settings.VIRTUAL_HEIGHT:
            self.in_play = False

        self.y += self.vy * dt
    
    def render(self, surface: pygame.Surface) -> None:
        surface.blit(
            settings.TEXTURES['spritesheet'], (self.x, self.y),
            settings.FRAMES['powerups'][self.frame]
        )
    
    def take(self, play_state: TypeVar('PlayState')) -> None:
        raise NotImplementedError
    

class TwoMoreBall(PowerUp):
    """
    Power-up to add two more ball to the game.
    """
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.frame = 8
    
    def take(self, play_state: TypeVar('PlayState')) -> None:
        paddle = play_state.paddle

        for _ in range(2):
            b = Ball(paddle.x + paddle.width // 2 - 4, paddle.y - 8)
            settings.SOUNDS['paddle_hit'].play()

            b.vx = random.randint(-80, 80)
            b.vy = random.randint(-170, -100)
            play_state.balls.append(b)

        self.in_play = False
