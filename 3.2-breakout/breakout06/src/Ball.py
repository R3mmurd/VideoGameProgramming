"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Ball.
"""
import random

import pygame

import settings


class Ball:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8

        self.vx = 0
        self.vy = 0

        self.texture = settings.TEXTURES["spritesheet"]
        self.frame = random.randint(0, 6)
        self.in_play = True

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def solve_world_boundaries(self) -> None:
        r = self.get_collision_rect()

        if r.left < 0:
            settings.SOUNDS["wall_hit"].stop()
            settings.SOUNDS["wall_hit"].play()
            self.x = 0
            self.vx *= -1
        elif r.right > settings.VIRTUAL_WIDTH:
            settings.SOUNDS["wall_hit"].stop()
            settings.SOUNDS["wall_hit"].play()
            self.x = settings.VIRTUAL_WIDTH - self.width
            self.vx *= -1
        elif r.top < 0:
            settings.SOUNDS["wall_hit"].stop()
            settings.SOUNDS["wall_hit"].play()
            self.y = 0
            self.vy *= -1
        elif r.top > settings.VIRTUAL_HEIGHT:
            settings.SOUNDS["hurt"].play()
            self.in_play = False

    def update(self, dt: float) -> None:
        self.x += self.vx * dt
        self.y += self.vy * dt

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y), settings.FRAMES["balls"][self.frame]
        )
