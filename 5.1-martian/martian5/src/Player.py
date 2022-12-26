from typing import TypeVar

from src.GameEntity import GameEntity
from src.states.entities import player_states

class Player(GameEntity):
    def __init__(self, x: int, y: int, game_level: TypeVar('GameLevel')) -> None:            
        super().__init__(
            x, y, 16, 20, 'martian', game_level,
            states={
                'idle': lambda sm: player_states.IdleState(self, sm),
                'walk': lambda sm: player_states.WalkState(self, sm),
                'jump': lambda sm: player_states.JumpState(self, sm),
                'fall': lambda sm: player_states.FallState(self, sm),
            },
            animation_defs={
                'idle': {
                    'frames': [0]
                },
                'walk': {
                    'frames': [9, 10],
                    'interval': 0.15
                },
                'jump': {
                    'frames': [2]
                }
            }
        )
