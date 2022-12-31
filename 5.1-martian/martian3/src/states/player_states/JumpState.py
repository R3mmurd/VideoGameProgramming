"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class JumpState for player.
"""
from gale.input_handler import InputHandler, InputData

import settings
from src.states.player_states.BaseEntityState import BaseEntityState


class JumpState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation('jump')
        self.entity.vy = -settings.GRAVITY / 3
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        if self.entity.check_collision_on_left() or self.entity.check_collision_on_right():
            pass

        if self.entity.check_collision_on_top():
            self.entity.vy = 0

        if self.entity.vy >= 0:
            self.entity.change_state('fall')

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'move_left':
            if input_data.pressed:
                self.entity.vx = -settings.PLAYER_SPEED
                self.entity.flipped = True
            elif input_data.released and self.entity.vx <= 0:
                self.entity.vx = 0

        elif input_id == 'move_right':
            if input_data.pressed:
                self.entity.vx = settings.PLAYER_SPEED
                self.entity.flipped = False
            elif input_data.released and self.entity.vx >= 0:
                self.entity.vx = 0
