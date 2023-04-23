"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class WalkState for player.
"""
from gale.input_handler import InputData

import settings
from src.states.player_states.BaseEntityState import BaseEntityState


class WalkState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.flipped = direction == "left"
        self.entity.vx = settings.PLAYER_SPEED
        if self.entity.flipped:
            self.entity.vx *= -1
        self.entity.change_animation("walk")

    def update(self, dt: float) -> None:
        next_x = self.entity.x + self.entity.vx * dt

        if self.entity.vx < 0:
            self.entity.x = max(0, next_x)
        else:
            self.entity.x = min(self.entity.tilemap.width - self.entity.width, next_x)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
            elif input_data.released and self.entity.vx <= 0:
                self.entity.change_state("idle")

        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
            elif input_data.released and self.entity.vx >= 0:
                self.entity.change_state("idle")
