"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class IdleState for player.
"""

from gale.input_handler import InputData

from src.states.player_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state("walk", "left")
        elif input_id == "move_right" and input_data.pressed:
            self.entity.flipped = False
            self.entity.change_state("walk", "right")
