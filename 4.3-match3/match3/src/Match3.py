import pygame

from gale.game import Game
from gale.input_handler import InputHandler, InputData
from gale.state_machine import StateMachine

import settings
from src import states


class Match3(Game):
    def init(self) -> None:
        settings.SOUNDS['music'].play(loops=-1)
        self.state_machine = StateMachine({
            'start': lambda sm: states.StartState(sm, self),
            'begin': states.BeginGameState,
            'play': states.PlayState,
            'game-over': states.GameOverState
        })
        self.state_machine.change('start')
        self.background_x = 0
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.background_x -= settings.BACKGROUND_SCROLL_SPEED * dt

        if self.background_x <= settings.BACKGROUND_LOOPING_POINT:
            self.background_x = 0
        
        self.state_machine.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES['background'], (self.background_x, 0))
        self.state_machine.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == 'quit' and input_data.pressed:
            self.quit()
