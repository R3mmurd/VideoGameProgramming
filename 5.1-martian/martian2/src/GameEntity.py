"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the base class GameEntity.
"""
from typing import TypeVar, Dict, Any, Tuple

from gale.state_machine import StateMachine, BaseState

from src import mixins


class GameEntity(mixins.DrawableMixin, mixins.AnimatedMixin):
    def __init__(
        self, x: float, y: float, width: float, height: float,
        texture_id: str, game_level: TypeVar('GameLevel'),
        states: Dict[str, BaseState], animation_defs: Dict[str, Dict[str, Any]]
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx: float = 0
        self.vy: float = 0
        self.texture_id = texture_id
        self.frame_index = -1
        self.game_level = game_level
        self.tilemap = self.game_level.tilemap
        self.state_machine = StateMachine(states)
        self.current_animation = None
        self.animations = {}
        self._generate_animations(animation_defs)
        self.flipped = False

    def change_state(self, state_id: str, *
                     args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        mixins.AnimatedMixin.update(self, dt)
