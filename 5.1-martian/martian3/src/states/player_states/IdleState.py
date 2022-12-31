"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class IdleState for player.
"""
from gale.input_handler import InputHandler, InputData

from src.states.player_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation('idle')
        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        if self.entity.check_collision_on_bottom():
            self.entity.vy = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'move_left' and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state('walk', 'left')
        elif input_id == 'move_right' and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state('walk', 'right')
        elif input_id == 'jump' and input_data.pressed:
            self.entity.change_state('jump')
