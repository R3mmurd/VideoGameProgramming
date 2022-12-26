from typing import TypeVar

from src.GameEntity import GameEntity


class Creature(GameEntity):
    def __init__(
        self, x: float, y, width: float, height: float,
        game_level: TypeVar('GameLevel'), **definition
    ) -> None:
        super().__init__(
            x, y, width, height, 
            definition['texture_id'],
            game_level,
            states={
                state_name: lambda sm: state_class(self, sm)
                for state_name, state_class in definition['states'].items()
            },
            animation_defs=definition['animation_defs']
        )
        self.walk_speed = definition['walk_speed']
        self.state_machine.change(definition['first_state'], self.flipped)
