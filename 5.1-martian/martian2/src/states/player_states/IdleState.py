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

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'move_left' and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state('walk', 'left')
        elif input_id == 'move_right' and input_data.pressed:
            self.entity.flipped = True
            self.entity.change_state('walk', 'right')
